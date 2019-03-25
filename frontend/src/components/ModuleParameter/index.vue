<template>
  <input v-bind="attributes">
</template>

<script>
export default {
    props: {
        parameter: {
            required: true,
            type: Object
        }
    },
    data() {
      const attributes = this.getAttributes();

      return { attributes };
    },
    computed: {
        isFloatType() {
            return this.parameter.type == 'FloatType';
        }
    },
    methods: {
      getAttributes() {
        const common = {
          name: this.parameter.name,
          required: 'required' in this.parameter ? this.parameter.required : true
        };

        let other;

        switch (this.parameter.type) {
          case 'FloatType':
            other = this.getFloatTypeAttributes();
            break;
        }

        const attributes = Object.assign({}, common, other);

        return attributes;
      },
      getFloatTypeAttributes() {
        return {
          step: 'any',
          type: 'number',
          value: Number.parseFloat(this.parameter.value)
        };
      }
    }
}
</script>