<template>
  <div class="menu-wrapper">
    <!-- <el-row :span="20" :xs="24" style="margin-bottom: 32px"> </el-row> -->
    <el-menu-item index="/dashboard">
      <i class="el-icon-chat-line-square"></i>
      <span slot="title">网站首页</span>
    </el-menu-item>

    <el-menu-item index="/research">
      <i class="el-icon-chat-line-square"></i>
      <span slot="title">宏观研究</span>
    </el-menu-item>

    <el-menu-item index="/stocknews">
      <i class="el-icon-s-data"></i>
      <span slot="title">股市行情</span>
    </el-menu-item>

    <el-menu-item index="/simulation">
      <i class="el-icon-watch"></i>
      <span slot="title">模拟回测</span>
    </el-menu-item>

    <el-menu-item index="/transaction">
      <i class="el-icon-s-platform"></i>
      <span slot="title">自选交易</span>
    </el-menu-item>

    <el-menu-item index="/userinfo">    
      <i class="el-icon-s-custom"></i>
      <span slot="title">个人信息</span>
    </el-menu-item>
  </div>
</template>
 
<script>
export default {
  name: "SidebarItem",
}
</script>