import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView'
import HomeView from '../views/HomeView'

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
