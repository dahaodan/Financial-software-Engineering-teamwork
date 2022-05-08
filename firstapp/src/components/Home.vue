<template>
  <div class="home">
    <el-button @click="gotoLogin">登录</el-button>
    <el-button @click="gotoRegister">注册</el-button>
  </div>
</template>

<script>
import Login from "./Login.vue";
import Register from "./Register.vue";
export default {
  methods: {
    gotoLogin() {
      this.$router.push("/login");
    },
    gotoRegister() {
      this.$router.push("/register");
    },
  },
  components: {
    Login,
    Register,
  },
};
</script>
