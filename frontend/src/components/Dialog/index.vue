<template>
  <div class='dialog-container'>
    <div class='dialog'>
      <slot />
      <div class='dialog--close-btn' @click='close_onClick'>&times;</div>
    </div>
  </div>
</template>

<style>
.dialog-container {
  align-items: center;
  background-color: rgba(lightgray, 0.5);
  display: flex;
  height: 100vh;
  justify-content: center;
  position: fixed;
  top: 0;
  width: 100vw;
}

.dialog {
  background-color: white;
  border: 1px solid black;
  padding: 5em;
  position: relative;
}

.dialog--close-btn {
  cursor: pointer;
  font-weight: bold;
  height: 10px;
  line-height: 10px;
  position: absolute;
  right: .25em;
  top: .25em;
  width: 10px;
}
</style>

<script>
export default {
  mounted() {
    this.$store.commit('setShowingDialogBox', true);
  },
  methods: {
    close_onClick(event) {
      this.$store.commit('setShowingDialogBox', false);
    }
  }
}
</script>
