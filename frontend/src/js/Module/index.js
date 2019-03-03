import ModuleState from '@js/ModuleState';
import { v4 as uuid }from 'uuid';

const typeCounts = {}

class Module {
  constructor({ name, type, inputs, outputs }) {
    if (!(type in typeCounts)) {
      typeCounts[type] = 0;
    }

    typeCounts[type]++;

    this.id = uuid();
    this.type = type;
    this.state = ModuleState.initialized;
    this.name = name ? name: `${type} ${typeCounts[type]}`;
    this.initializeInputs(inputs);
    this.initializeOutputs(outputs);
  }

  get isCalculating() {
    return this.state === ModuleState.calculating;
  }

  get isErrored() {
    return this.state === ModuleState.error;
  }

  get isComplete() {
    return this.state === ModuleState.complete;
  }

  initializeInputs(inputs) {
    this.inputs = {};

    Object.entries(inputs).forEach(([name, type]) => {
      this.inputs[name] = { type, name };
    });
  }

  initializeOutputs(outputs) {
    this.outputs = {};

    Object.entries(outputs).forEach(([name, type]) => {
      this.outputs[name] = { type, name };
    });
  }
}

export default Module;
