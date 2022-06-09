<template>
  <div class="app-wrapper" :class="classObj">
    <!-- 左侧导航栏 -->
    <sidebar class="sidebar-container"></sidebar>
    <div class="main-container">
      <!-- 上部导航栏 -->
      <navbar></navbar>
      <!-- 中间内容 -->
      <app-main></app-main>
    </div>
  </div>
</template>
 
<script>
import { Navbar, Sidebar, AppMain } from "./components";
 
export default {
  name: "Layout",
  components: {
    Navbar,
    Sidebar,
    AppMain,
  },
  computed: {
    classObj() {
      return {
        hideSidebar: true,
        withoutAnimation: false,
        mobile: false,
      };
    },
  },
};
</script>


<style rel="stylesheet/scss" lang="scss" scoped>
 @import "src/styles/mixin.scss";
  .app-wrapper {
    @include clearfix;
    position: relative;
    height: 100%;
    width: 100%;
  }
</style>