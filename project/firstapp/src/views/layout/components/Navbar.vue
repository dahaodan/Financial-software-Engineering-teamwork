<template>
  <!-- <el-menu class="navbar" mode="horizontal">
    顶部
  </el-menu> -->
  <div class="navbar">
    <div v-if="params.isLogin" class="right-menu">
      <el-dropdown
        class="avatar-container right-menu-item hover-effect"
        trigger="click"
      >
        <div class="avatar-wrapper">
          <img
            src="https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
            class="user-avatar"
          />
          <i class="el-icon-caret-bottom" />
        </div>
        <el-dropdown-menu slot="dropdown">
          <router-link to="/userinfo">
            <el-dropdown-item>个人信息</el-dropdown-item>
          </router-link>
          <router-link to="/dashboard">
            <el-dropdown-item>返回首页</el-dropdown-item>
          </router-link>
          <a
            target="_blank"
            href="https://github.com/dahaodan/Financial-software-Engineering-teamwork"
          >
            <el-dropdown-item>Github</el-dropdown-item>
          </a>
          <el-dropdown-item divided>
            <span style="display: block" @click="logout()">退出登录</span>
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
    <div v-else class="right-menu">
      <router-link to="/login">
        <el-button class="btsn1">登录</el-button>
      </router-link>
      <router-link to="/register">
        <el-button class="btsn1">注册</el-button>
      </router-link>
    </div>
  </div>
</template>

<script>
import Cookies from "js-cookie";

export default {
  data() {
    return {
      params: {},
    };
  },
  mounted() {
    const token = localStorage.getItem("token");
    this.$set(this.params, "isLogin", Boolean(token));
  },
  methods: {
    logout() {
      this.$message.success("退出成功");
      localStorage.clear();
      this.$set(this.params, "isLogin", false);
      this.$router.push(0);
      this.$router.push("/dashboard");
    },
  },
  components: {},
};
</script>
 
<style lang="scss" scoped>
.navbar {
  // height: 50px;
  // line-height: 50px;
  // border-radius: 0px !important;
  height: 50px;
  overflow: hidden;
  position: relative;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);

  .right-menu {
    float: right;
    height: 100%;
    line-height: 50px;

    &:focus {
      outline: none;
    }

    
    .btsn1 {
      font-size: 18px;
      color: black;
    }

    .right-menu-item {
      display: inline-block;
      padding: 0 8px;
      height: 100%;
      font-size: 18px;
      color: #5a5e66;
      vertical-align: text-bottom;

      &.hover-effect {
        cursor: pointer;
        transition: background 0.3s;

        &:hover {
          background: rgba(0, 0, 0, 0.025);
        }
      }
    }

    .avatar-container {
      margin-right: 30px;

      .avatar-wrapper {
        margin-top: 5px;
        position: relative;

        .user-avatar {
          cursor: pointer;
          width: 40px;
          height: 40px;
          border-radius: 10px;
        }

        .el-icon-caret-bottom {
          cursor: pointer;
          position: absolute;
          right: -20px;
          top: 25px;
          font-size: 12px;
        }
      }
    }
  }
}
</style>
