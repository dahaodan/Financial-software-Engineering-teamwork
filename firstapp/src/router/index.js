import Vue from "vue";
import Router from "vue-router";
import Home from "../components/Home";
import Login from "../components/Login";
import ForgetPassword from "../components/ForgetPassword";
import Register from "../components/Register";

Vue.use(Router);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
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
  }
];

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: routes
});
