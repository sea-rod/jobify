// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Langing.vue'
import Auth from './views/Auth.vue'
import Upload from './views/Upload.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/auth', component: Auth },
  { path: '/upload-resume',component:Upload}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
