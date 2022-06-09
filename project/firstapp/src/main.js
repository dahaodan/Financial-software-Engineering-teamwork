// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App";
import router from "./router";
import ElementUI from "element-ui";
import axios from "axios";

import "./permission";
import "./assets/icons";

import "element-ui/lib/theme-chalk/index.css";
import "./assets/css/global.css";
import "@/styles/index.scss"; // global css
import elTableInfiniteScroll from 'el-table-infinite-scroll';

Vue.use(ElementUI);
Vue.config.productionTip = false;
Vue.prototype.$axios = axios;
Vue.use(elTableInfiniteScroll);
axios.defaults.baseURL = "http://localhost:8080";

/* eslint-disable no-new */
new Vue({
  axios,
  el: "#app",
  router,
  components: { App },
  template: "<App/>"
});
