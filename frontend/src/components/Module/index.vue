<template>
  <div :class="classes">
    <div
      class="module-toggle module-toggle--input"
      @click.prevent="inputToggle_onClick"
    >
      <div class="module-toggle-text--input">
        In
      </div>
    </div>
    {{ module.name }}
    <div
      class="module-toggle module-toggle--output"
      @click.prevent="outputToggle_onClick"
    >
      <div class="module-toggle-text--output">
        Out
      </div>
    </div>
  </div>
</template>

<style>
.module {
  border: 1px solid black;
  display: inline-block;
  min-width: 100px;
  padding: 2.5em;
  position: absolute;
  text-align: center;
}

.module--initialized {
  background-color: lightgray;
}

.module--calculating {
  background-color: darkkhaki;
}

.module--complete {
  background-color: darkseagreen;
}

.module-toggle {
  align-items: center;
  background-color: lightblue;
  cursor: pointer;
  display: flex;
  height: 100%;
  justify-content: center;
  position: absolute;
  top: 0;
  width: 1.5em;
}

.module-toggle--output {
  right: 0;
}

.module-toggle--input {
  left: 0;
}

.module-toggle-text--input {
  transform: rotate(-90deg);
}

.module-toggle-text--output {
  transform: rotate(90deg);
}
</style>

<script>
import interact from 'interactjs';

export default {
  props: {
    module: {
      required: true,
      type: Object
    }
  },
  data() {
    return {
      x: 0,
      y: 0
    }
  },
  computed: {
    classes() {
      return ['module', `module--${this.module.state}`];
    }
  },
  mounted() {
    interact(this.$el)
      .draggable({
        snap: {
          targets: [
            interact.createSnapGrid({ x: 30, y: 30 })
          ],
          range: Infinity,
          relativePoints: [ { x: 0, y: 0 } ]
        },
        onmove: this.module_onMove,
        restrict: {
          restriction: this.$el.parentNode,
          elementRect: { top: 0, left: 0, bottom: 1, right: 1 },
          endOnly: true
        }
      });
  },
  methods: {
    inputToggle_onClick() {
      this.$emit('show_module_inputs', this.module);
    },
    outputToggle_onClick() {
      this.$emit('show_module_outputs', this.module);
    },
    module_onMove(event) {
      this.x += event.dx;
      this.y += event.dy;

      const transform = `translate(${this.x}px, ${this.y}px)`;

      event.target.style.webkitTransform = transform;
      event.target.style.transform = transform;
    }
  }
}
</script>
