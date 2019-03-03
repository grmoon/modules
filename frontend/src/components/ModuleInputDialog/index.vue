<template>
  <Dialog>
    <form @submit.prevent='form_onSubmit'>
      <div v-for='(input, name) in module.inputs' :key='name'>
        <label>
          <div>{{ name }}</div>
          <ModuleParameter :parameter='input' />
          <input
            class='module-input'
            v-if="shouldShowManualInput(input.type, name)"
            type='number'
            :name='name'
            required
          />
          <select
            :name='name'
            class='module-input'
            v-else
          >
            <option disabled selected>Select a Module Output</option>
            <optgroup
              v-for='(outputs, outputModuleName) in modulesByOutputType[input.type]'
              :key='outputModuleName'
              :label='outputModuleName'
            >
              <option
                v-for='(output, index) in outputs'
                :key='index'
                :data-module-id='output.moduleId'
                :value='`${output.moduleId}_${output.name}`'
              >
              {{ outputModuleName }}: {{ output.name }}
              </option>
            </optgroup>
          </select>
        </label>
        <label v-if='shouldShowManualInputOption(input.type)'>
          Manual Input: <input
            @change='radio_onChange'
            type='radio'
            :name='`input_method-${name}`'
            value='manual'
            :data-name='name'
            checked
          />
        </label>
        <label v-if='shouldShowInputFromModuleOption(input.type)'>
          Input From Module: <input
            @change='radio_onChange'
            type='radio'
            :name='`input_method-${name}`'
            value='from_module'
            :data-name='name'
          />
        </label>
      </div>
      <input type='submit' value='Save Inputs' />
    </form>
  </Dialog>
</template>

<script>
import Dialog from '@components/Dialog';
import ModuleParameter from '@components/ModuleParameter';
import { mapState } from 'vuex';

export default {
  components: { Dialog, ModuleParameter },
  props: ['module'],
  computed: {
    ...mapState(['modules']),
  },
  data() {
    const inputMethods = {};
    const modulesByOutputType = {};

    Object.entries(this.module.inputs).forEach(([name, input]) => {
      inputMethods[name] = 'manual';
    });

    return {
      inputMethods,
      modulesByOutputType
    }
  },
  created() {
    const modulesByOutputType = {};

    Object.values(this.modules).forEach((module) => {
      if (module.id === this.module.id) {
        return;
      }

      Object.entries(module.outputs).forEach(([name, output]) => {
        const type = output.type;

        if (!(type in modulesByOutputType)) {
          modulesByOutputType[type] = {};
        }

        if (!(module.name in modulesByOutputType[type])) {
          modulesByOutputType[type][module.name] = [];
        }

        modulesByOutputType[type][module.name].push({
          moduleId: module.id,
          name,
          type: output.type
        });
      });
    });

    this.modulesByOutputType = modulesByOutputType;
  },
  methods: {
    shouldShowInputFromModuleOption(type) {
      return type in this.modulesByOutputType;
    },
    shouldShowManualInputOption(type) {
      return this.shouldShowInputFromModuleOption(type);
    },
    shouldShowManualInput(type, name) {
      const shouldShowInputFromModuleOption = this.shouldShowInputFromModuleOption(type);

      return this.inputMethods[name] == 'manual' || !shouldShowInputFromModuleOption;
    },
    modulesWithOutputTypeExist(outputType) {
      return outputType in this.modulesByOutputType;
    },
    radio_onChange(event) {
      const target = event.currentTarget;
      const name = target.getAttribute('data-name');

      this.inputMethods[name] = target.value;
    },
    form_onSubmit(event) {
      const form = event.currentTarget;
      const inputs = form.querySelectorAll('input.module-input');

      for (let inputIdx = 0; inputIdx < inputs.length; inputIdx++) {
        const input = inputs[inputIdx];

        this.module.inputs[input.name].source = 'constant';
        this.module.inputs[input.name].value = input.value;
      }

      const selects = form.querySelectorAll('select.module-input');

      for (let selectIdx = 0; selectIdx < selects.length; selectIdx++) {
        const select = selects[selectIdx];
        const [moduleId, outputName] = select.value.split('_')

        this.module.inputs[select.name].source = moduleId;
        this.module.inputs[select.name].value = outputName;
      }

      this.$store.commit('setShowingDialogBox', false);
      this.$store.dispatch('calculate');
    }
  }
}
</script>
