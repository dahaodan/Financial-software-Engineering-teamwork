// 忘记密码界面
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

    <div class="forgetPassword">
      <div class="forgetPassword_form">
        <p>Welcome!</p>
        <el-form
          :model="forgetPasswordForm"
          :rules="rules"
          ref="forgetPasswordForm"
        >
          <el-form-item label="" prop="userName">
            <el-input
              type="text"
              autocomplete="off"
              v-model="forgetPasswordForm.userName"
              prefix-icon="el-icon-user-solid"
              placeholder="请输入用户名"
            ></el-input>
          </el-form-item>
          <el-form-item label="" prop="userEmail">
            <el-input
              type="email"
              autocomplete="off"
              v-model="forgetPasswordForm.userEmail"
              prefix-icon="el-icon-message"
              placeholder="请输入注册邮箱"
            ></el-input>
          </el-form-item>
          <el-form-item label="" prop="passWord">
            <el-input
              type="password"
              autocomplete="off"
              v-model="forgetPasswordForm.passWord"
              prefix-icon="el-icon-lock"
              placeholder="请输入新密码"
            ></el-input>
          </el-form-item>
          <el-form-item label="" prop="checkPass">
            <el-input
              type="password"
              autocomplete="off"
              v-model="forgetPasswordForm.checkPass"
              prefix-icon="el-icon-lock"
              placeholder="请再次输入新密码"
            ></el-input>
          </el-form-item>
          <el-form-item class="btns1">
            <el-button type="primary" @click="submitForm('forgetPasswordForm')"
              >修改密码</el-button
            >
            <el-button @click="resetforgetPasswordForm">重置</el-button>
          </el-form-item>
          <el-form-item class="btns2">
            <router-link style="text-decoration: none" to="/">
              <el-link :underline="false" type="primary">返回首页</el-link>
            </router-link>
            <router-link style="text-decoration: none" to="/login">
              <el-link :underline="false" type="primary">登录</el-link>
            </router-link>
            <router-link
              style="text-decoration: none"
              to="/register"
            >
              <el-link :underline="false" type="primary">注册</el-link>
            </router-link>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "forgetPassword",
  data() {
    var validateEmail = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入注册邮箱"));
      } else {
        if (value !== "") {
          var forgetPassword =
            /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
          if (!forgetPassword.test(value)) {
            callback(new Error("请输入有效的邮箱"));
          }
        }
        callback();
      }
    };
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.forgetPasswordForm.checkPass !== "") {
          if (value.length < 6 || value.length > 16) {
            callback(new Error("密码长度在6到16个字符"));
          }
          this.$refs.forgetPasswordForm.validateField("checkPass");
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.forgetPasswordForm.passWord) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    return {
      starsCount: 2000,
      distance: 800,
      vedioCanPlay: false,
      fixStyle: "",
      form: { role: 1 },
      forgetPasswordForm: {
        userName: "",
        userEmail: "",
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
        userEmail: [
          { required: true, validator: validateEmail, trigger: "blur" },
        ],
        passWord: [
          { required: true, validator: validatePass, trigger: "blur" },
        ],
        checkPass: [
          { required: true, validator: validatePass2, trigger: "blur" },
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
      this.$refs["forgetPasswordForm"].validate((valid) => {
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
            username: this.forgetPasswordForm.userName,
            email: this.forgetPasswordForm.userEmail,
            password: this.forgetPasswordForm.passWord,
          };

          // axios方式发送请求
          this.$axios
            .post("/forgetpassword", data, config)
            .then((response) => {
              console.log(response.data);
              // 用户验证成功并且密码修改成功 code返回值为0
              // 用户验证失败 code返回值为1
              if (response.data["auth"] === 0) {
                this.$message.success("密码修改成功");
                this.$router.push("/login");
              } else {
                this.$message.error("用户验证失败");
              }
            })
            .catch(function (error) {
              console.log(error);
              this.$message.error("用户验证失败");
            });
        } else {
          this.$message.error("用户验证失败");
          return false;
        }
      });
    },
    // 重置
    resetforgetPasswordForm() {
      this.$refs["forgetPasswordForm"].resetFields();
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
.forgetPassword_form {
  width: 400px;
  height: 500px;
  position: absolute;
  left: 50%;
  top: 40%;
  margin-left: -200px;
  margin-top: -150px;
  padding: 10px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px #ddd;
}
.btns1 {
  align-items: center;
  text-align: center;
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