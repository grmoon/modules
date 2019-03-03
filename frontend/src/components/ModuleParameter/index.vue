<template>
  <input
    v-if="isFloatType"
    type="number"
  >
  <input
    v-else
    type="text"
  >
</template>

<script>
export default {
    props: {
        parameter: {
            required: true,
            type: Object
        }
    },
    computed: {
        isFloatType() {
            return this.parameter.type == 'FloatType';
        }
    }
}
</script>