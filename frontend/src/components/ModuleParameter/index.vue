<template>
    <input type='number' v-if='isFloatType' />
    <input type='text' v-else />
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