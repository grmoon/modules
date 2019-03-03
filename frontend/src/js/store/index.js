import Module from '@js/Module';
import Vue from 'vue';
import Vuex from 'vuex';
import ModuleState from '@js/ModuleState';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    moduleClasses: [],
    modules: {},
    showingDialogBox: false
  },
  mutations: {
    setWebSocket(state, webSocket) {
      state.webSocket = webSocket;
    },
    setModuleClasses(state, moduleClasses) {
      state.moduleClasses = moduleClasses;
    },
    setShowingDialogBox(state, showingDialogBox) {
      state.showingDialogBox = showingDialogBox;
    },
    setModuleState(state, { moduleId, moduleState }) {
      Vue.set(state.modules[moduleId], 'state', moduleState);
    },
    setModuleOutputs(state, moduleOutputs) {
        Object.entries(moduleOutputs).forEach(([moduleId, outputs]) => {
          const _module = state.modules[moduleId];

          Object.entries(outputs).forEach(([name, value]) => {
            Vue.set(_module.outputs[name], 'value', value);
          });

          console.log(outputs);
        });
    },
    createModule(state, moduleParams) {
      const module = new Module(moduleParams);

      state.modules = Object.assign({
        [module.id]: module
      }, state.modules);
    }
  },
  actions: {
    calculate({ state }) {
      let canCalculate = true;

      Object.values(state.modules).every(_module => {
        Object.values(_module.inputs).every(input => {
          canCalculate = input.source !== undefined && input.value !== undefined;

          return canCalculate;
        });

        return canCalculate;
      });

      if (canCalculate) {
        socket.sendJSON({
          command: 'calculate',
          modules: state.modules
        });
      }
    },
    initialize() {
      return Promise.all([]);
    }
  }
});

const socket = new WebSocket('ws://localhost:5000');

socket.onopen = () => {
  socket.sendJSON({ command: 'get_available_modules' });
}

socket.onclose = (event) => {
  debugger;
}

socket.onerror = (event) => {
  debugger;
}

socket.onmessage = (event) => {
  const message = JSON.parse(event.data);
  console.log(message);
  const command = message.command;
  const content = message.content;

  switch (command) {
    case 'get_available_modules':
        store.commit('setModuleClasses', content);
        break;
      case 'module_calculation_started': {
        const moduleId = content['module_id'];

        store.commit('setModuleState', {
          moduleId,
          moduleState: ModuleState.calculating
        });
        break;
      }
      case 'module_calculation_finished': {
        const moduleId = content['module_id'];

        store.commit('setModuleState', {
          moduleId,
          moduleState: ModuleState.complete
        });
        break;
      }
      case 'calculations':
        store.commit('setModuleOutputs', content.outputs);
        break;
  }
}

socket.sendJSON = (message) => {
  socket.send(JSON.stringify(message));
}

export default store;