// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Langing.vue'
import Auth from './views/Auth.vue'
import JobSearch from './views/JobSearch.vue'
import Upload from './views/Upload.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/auth', component: Auth },
  { path: '/upload-resume',component:Upload},
  {path:'/jobs',component:JobSearch}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 
