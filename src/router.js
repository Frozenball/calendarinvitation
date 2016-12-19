import VueRouter from 'vue-router';

import CreateEvent from './components/CreateEvent';
import NotFound from './components/NotFound';
import ViewEvent from './components/ViewEvent';

export default new VueRouter({
  mode: 'history',
  routes: [
    { name: 'index', path: '/', component: CreateEvent },
    { name: 'view', path: '/:slug', component: ViewEvent },
    { name: '404', path: '*', component: NotFound },
  ],
});
