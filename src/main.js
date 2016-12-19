// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import VueResource from 'vue-resource';
import VueRouter from 'vue-router';

import App from './App';
import router from './router';

Vue.use(VueResource);
Vue.use(VueRouter);

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  template: '<App/>',
  components: { App },
  http: {
    root: 'http://localhost:3000/',
  },
});
