import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import Projects from './Projects.vue'

// This is imported globally on the website so no need to include it again in this view
// import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);

new Vue({
  el: '#projects',
  template: '<projects/>',
  components: {
      Projects
  },
})
