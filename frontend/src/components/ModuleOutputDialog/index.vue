<template>
  <Dialog>
    <div v-for='(output, name) in module.outputs' :key='name'>
      <label>
        <div>
          {{ name }}
        </div>
        <input type='number' :value='output.value' disabled />
      </label>
    </div>
  </Dialog>
</template>

<script>
import Dialog from '@components/Dialog';

export default {
  components: { Dialog },
  props: ['module']
}
</script>
