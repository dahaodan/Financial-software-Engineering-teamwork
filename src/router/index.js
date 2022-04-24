import Vue from "vue";
import Router from "vue-router";
import Home from "../components/Home";
import Login from "../components/Login";
import ForgetPassword from "../components/ForgetPassword";
import Register from "../components/Register";

Vue.use(Router);

export default new Router({
  routes: [
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
      path: "/forgetpassword",
      name: "ForgetPassword",
      component: ForgetPassword
    },
    {
      path: "/register",
      name: "Register",
      component: Register
    }
  ]
});