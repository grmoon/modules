<template>
  <div class='container'>
    <ModuleCreationForm />
    <div class='modules'>
      <Module
        @show_module_inputs='module_onShowModuleInputs'
        @show_module_outputs='module_onShowModuleOutputs'
        v-for='(module, moduleId) in modules'
        :key='moduleId'
        :module='module'
      />
    </div>
    <ModuleInputDialog
      v-if='showInputDialog'
      :module='focusedModule'
      @cancel='inputDialog_onCancel'
    />
    <ModuleOutputDialog
      v-if='showOutputDialog'
      :module='focusedModule'
      @cancel='outputDialog_onCancel'
    />
  </div>
</template>

<style>
.container {
  position: relative;
}

.modules {
  height: 1000px;
  position: relative;
  width: 100%;
}
</style>

<script>
import ModuleInputDialog from '@components/ModuleInputDialog';
import ModuleOutputDialog from '@components/ModuleOutputDialog';
import ModuleCreationForm from '@components/ModuleCreationForm';
import Module from '@components/Module';
import { mapState } from 'vuex';

export default {
  components: { Module, ModuleInputDialog, ModuleOutputDialog, ModuleCreationForm },
  data() {
    return {
      focusedModule: undefined,
      selectedModuleClassId: -1,
      showInputDialog: false,
      showOutputDialog: false,
    }
  },
  computed: mapState(['moduleClasses', 'showingDialogBox', 'modules']),
  watch: {
    showingDialogBox() {
      if (!this.showingDialogBox) {
        this.showInputDialog = false;
        this.showOutputDialog = false;
      }
    }
  },
  methods: {
    inputDialog_onCancel() {
      this.showInputDialog = false;
    },
    outputDialog_onCancel() {
      this.showOutputDialog = false;
    },
    module_onShowModuleInputs(module) {
      this.focusedModule = module;
      this.showInputDialog = true;
    },
    module_onShowModuleOutputs(module) {
      this.focusedModule = module;
      this.showOutputDialog = true;
    }
  },
  created() {
    this.$store.dispatch('initialize');
  }
}
</script>
