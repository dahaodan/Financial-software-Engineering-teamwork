// AppMain.vue -----------------------
<template>
  <section class="app-main">
    <transition name="fade" mode="out-in">
      <!-- 这里是子路径view，也就是会将子页面的内容展示在这里 -->
      <router-view></router-view>
    </transition>
  </section>
</template>
 
<script>
export default {
  name: 'AppMain',
  computed: {
  }
}
</script>