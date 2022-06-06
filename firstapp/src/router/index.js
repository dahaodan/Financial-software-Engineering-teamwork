import Vue from "vue";
import Router from "vue-router";
import Login from "../components/Login";
import ForgetPassword from "../components/ForgetPassword";
import Register from "../components/Register";
import Layout from '../views/layout/Layout';


Vue.use(Router);

const routes = [
  {
    path: "/",
    name: "Layout",
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: '/dashboard',
      name: 'Dashboard',
      component: () => import('@/components/dashboard'),
      meta: { title: 'Dashboard', icon: 'dashboard' }
    }]
  },
  
  {
    path: '/userinfo',
    component: Layout,
    children: [
      {
        // 跳转的路径是这里的
        path: '/userinfo',
        name: 'Userinfo',
        component: () => import('@/components/user'),
        meta: { title: 'Form', icon: 'form' }
      },
      {
        path: '/userinfo',
        name: 'RechargeCard',
        component: () => import('@/components/user/RechargeCard'),
        meta: { title: 'Form', icon: 'form' }
      },
      {
        path: '/userinfo',
        name: 'PasswordCard',
        component: () => import('@/components/user/PasswordCard'),
        meta: { title: 'Form', icon: 'form' }
      }
    ]
  },

  {
    path: '/stocknews',
    component: Layout,
    children: [
      {
        // 跳转的路径是这里的
        path: '/stocknews',
        name: 'Stocknews',
        component: () => import('@/components/stocknews'),
        meta: { title: 'Form', icon: 'form' }
      }
    ]
  },

  {
    path: '/simulation',
    component: Layout,
    children: [
      {
        // 跳转的路径是这里的
        path: '/simulation',
        name: 'Simualtion',
        component: () => import('@/components/simulation'),
        meta: { title: 'Simulation', icon: 'simulation' }
      }
    ]
  },

  {
    path: '/research',
    component: Layout,
    children: [
      {
        // 跳转的路径是这里的
        path: '/research',
        name: 'Research',
        component: () => import('@/components/research'),
        meta: { title: 'Research', icon: 'research' }
      }
    ]
  },

  {
    path: '/transaction',
    component: Layout,
    children: [
      {
        // 跳转的路径是这里的
        path: '/transaction',
        name: 'Transaction',
        component: () => import('@/components/transaction'),
        meta: { title: 'Transaction', icon: 'transaction' }
      }
    ]
  },

  {
    path: '/car',
    component: Layout,
    children: [
      {
        // 跳转的路径是这里的
        path: '/car',
        name: 'Car',
        component: () => import('@/components/car'),
        meta: { title: 'Car', icon: 'car' }
      }
    ]
  },

  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/register",
    name: "Register",
    component: Register
  },
  {
    path: "/forgetpassword",
    name: "ForgetPassword",
    component: ForgetPassword
  },
  // {
  //   path: "/form",
  //   name: "form",
  //   component: () =>
  //     import(
  //       /* webpackChunkName: "comanyregister" */
  //       "../components/form/index.vue"
  //     ),
  //   // 重点在此
  //   meta: {
  //     name: "Layout"
  //   },
  // }

]

export default new Router({
  // mode: "history",
  scrollBehavior: () => ({
    y: 0
  }),
  base: process.env.BASE_URL,
  routes: routes
});
