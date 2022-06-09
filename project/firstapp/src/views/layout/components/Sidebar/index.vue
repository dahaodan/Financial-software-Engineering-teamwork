<!-- 对sidebaritem当中menu的总体设置 -->
<template>
    <el-menu
      :default-active="this.$route.path"            
      mode="vertical"
      background-color="#304156"
      text-color="#bfcbd9"
      active-text-color="#409EFF"
      router
    >
      <sidebar-item></sidebar-item>
    </el-menu>
</template>
 
<script>
import SidebarItem from './SidebarItem'
 
export default {
  components: { SidebarItem },
}
</script>
 
