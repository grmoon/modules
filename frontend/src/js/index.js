import Vue from 'vue';
import App from '@components/App/index';
import store from '@store';
import '@css/index';

new Vue({
  el: '#app',
  store,
  render(createElement) {
    return createElement(App);
  }
});
