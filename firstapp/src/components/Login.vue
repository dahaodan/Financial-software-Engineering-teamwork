// 登录界面
<template>
  <div class="body">
    <div class="stars" ref="starsRef">
      <div
        class="star"
        v-for="(item, index) in starsCount"
        :key="index"
        ref="star"
      ></div>
    </div>

    <div class="login">
      <div class="login_form">
        <p>Welcome!</p>
        <el-form :model="loginForm" :rules="rules" ref="loginForm">
          <el-form-item label="" prop="userName">
            <el-input
              type="text"
              autocomplete="off"
              v-model="loginForm.userName"
              prefix-icon="el-icon-user-solid"
              placeholder="请输入用户名"
            ></el-input>
          </el-form-item>
          <el-form-item label="" prop="passWord">
            <el-input
              type="password"
              autocomplete="off"
              v-model="loginForm.passWord"
              prefix-icon="el-icon-lock"
              placeholder="请输入密码"
            ></el-input>
          </el-form-item>
          <el-form-item class="btns1">
            <el-button type="primary" @click="submitForm('loginForm')"
              >登录</el-button
            >
            <el-button @click="resetLoginForm">重置</el-button>
          </el-form-item>
          <el-form-item class="btns2">
            <router-link style="text-decoration: none" to="/">
              <el-link :underline="false" type="primary">返回首页</el-link>
            </router-link>
            <router-link style="text-decoration: none" to="/register">
              <el-link :underline="false" type="primary">注册</el-link>
            </router-link>
            <router-link style="text-decoration: none" to="/forgetpassword">
              <el-link :underline="false" type="primary">忘记密码</el-link>
            </router-link>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      starsCount: 2000,
      distance: 800,
      vedioCanPlay: false,
      fixStyle: "",
      form: { role: 1 },
      loginForm: {
        userName: "",
        passWord: "",
      },
      rules: {
        userName: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          {
            min: 3,
            max: 8,
            message: "用户名长度在3到8个字符",
            trigger: "blur",
          },
        ],
        passWord: [
          { required: true, message: "请输入密码", trigger: "blur" },
          {
            min: 6,
            max: 16,
            message: "密码长度在6到16个字符",
            trigger: "blur",
          },
        ],
      },
    };
  },
  mounted() {
    let starArr = this.$refs.star;
    starArr.forEach((item) => {
      let speed = 0.2 + Math.random() * 1;
      let thisDistance = this.distance + Math.random() * 300;
      item.style.transformOrigin = `0 0 ${thisDistance}px`;
      item.style.transform = `translate3d(0, 0, -${thisDistance}px) rotateY(${
        Math.random() * 360
      }deg) rotateX(${Math.random() * -50}deg) scale(${speed}, ${speed})`;
    });
  },
  methods: {
    // 提交登录信息
    submitForm(formName) {
      this.$refs["loginForm"].validate((valid) => {
        // 验证用户名和密码输入是否符合规范
        if (valid) {
          let config = {
            // 关于comnteng-type，看https://www.jb51.net/article/145209.htm
            headers: {
              "Content-Type": "application/json", //默认
              // 'Content-Type': 'multipart/form-data'
              // 'Content-Type': 'application/x-www-form-urlencoded'
            },
          };

          let data = {
            username: this.loginForm.userName,
            password: this.loginForm.passWord,
          };

          // axios方式发送请求
          this.$axios
            .post("/login", data, config)
            .then((response) => {
              console.log(response.data);
              // 管理员登录成功 code返回值为-1
              // 普通用户登录成功 code返回值为0
              // 登录失败 code返回值为1
              if (response.data["code"] === 0) {
                // 普通用户模式
                this.$message.success("登录成功");
                this.$router.push("/");
              } else {
                if (response.data["code"] === -1) {
                  // 管理员模式
                  this.$message.success("登录成功");
                  this.$router.push("/");
                }
                else {
                  this.$message.error("登录失败");
                }
              }
            })
            .catch(function (error) {
              console.log(error);
              this.$message.error("登录失败");
            });
        } else {
          this.$message.error("登录失败");
          return false;
        }
      });
    },
    // 重置
    resetLoginForm() {
      this.$refs["loginForm"].resetFields();
    },
    handleClick() {},
  },
};
</script>

<style lang="css" scoped>
.body {
  position: sticky;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  border: 0;
  background: radial-gradient(
    200% 100% at bottom center,
    #f7f7b6,
    #e96f92,
    #1b2947
  );
  background: radial-gradient(
    200% 105% at top center,
    #1b2947 10%,
    #072485 40%,
    #30649b 65%,
    #039ce8
  );
  background-attachment: fixed;
  overflow: hidden;
}

@keyframes rotate {
  0% {
    transform: perspective(400px) rotateZ(20deg) rotateX(-40deg) rotateY(0);
  }
  100% {
    transform: perspective(400px) rotateZ(20deg) rotateX(-40deg)
      rotateY(-360deg);
  }
}
.stars {
  transform: perspective(500px);
  transform-style: preserve-3d;
  position: absolute;
  perspective-origin: 50% 100%;
  left: 45%;
  animation: rotate 90s infinite linear;
  bottom: 0;
}
.star {
  width: 2px;
  height: 2px;
  background: #f7f7b6;
  position: absolute;
  left: 0;
  top: 0;
  backface-visibility: hidden;
}
.login_form {
  width: 400px;
  height: 360px;
  position: absolute;
  left: 50%;
  top: 45%;
  margin-left: -200px;
  margin-top: -150px;
  padding: 10px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px #ddd;
}
.btns1 {
  align-items: center;
  justify-content: flex-end;
}
.btns2 {
  display: flex;
  justify-content: flex-end;
}
p {
  font-size: 24px;
  text-align: center;
  font-weight: 600;
}
</style>
