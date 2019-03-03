<template>
  <form @submit.prevent="form_onSubmit">
    <label>
      <div>Module Name</div>
      <input
        v-model="moduleName"
        type="text"
      >
    </label>
    <label>
      <div>Module Class</div>
      <select
        v-model="selectedModuleClassId"
        required
      >
        <option
          disabled
          value="-1"
        >Select a Module Class:</option>
        <option
          v-for="(moduleClass, index) in moduleClasses"
          :key="index"
          :value="index"
        >{{ moduleClass.type }}</option>
      </select>
    </label>
    <div>
      <input
        type="submit"
        value="Create Module"
        required
      >
    </div>
  </form>
</template>



<script>
import { mapState } from 'vuex';

export default {
  data() {
    return {
      selectedModuleClassId: -1,
      moduleName: ''
    }
  },
  computed: mapState(['moduleClasses']),
  methods: {
    form_onSubmit() {
      const moduleParams = Object.assign(
        { name: this.moduleName },
        this.moduleClasses[this.selectedModuleClassId]
      );

      this.$store.commit('createModule', moduleParams);
    }
  }
}
</script>
