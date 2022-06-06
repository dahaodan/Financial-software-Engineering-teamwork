import router from "./router";
import { Message } from "element-ui";

const whiteList = ["/dashboard", "/login", "/register", "/forgetpassword"];

router.beforeEach((to, from, next) => {
  // determine whether the user has logged in
  const token = localStorage.getItem("token");

  if (token) {
    if (to.path === "/login") {
      next({ path: "/dashboard" });
    } else {
      next();
    }
  } else {
    if (whiteList.indexOf(to.path) !== -1) {
      next();
    } else {
      // pages that do not have permission redirect to the login page
      Message.warning("请先进行登录！");
      next({ path: "/login" }).catch(err => err);
    }
  }
});
