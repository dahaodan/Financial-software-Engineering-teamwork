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

    <div class="reg">
      <div class="reg_form">
        <p>Welcome!</p>
        <el-form :model="regForm" :rules="rules" ref="regForm">
          <el-form-item label="" prop="userName">
            <el-input
              type="text"
              autocomplete="off"
              v-model="regForm.userName"
              prefix-icon="el-icon-user-solid"
              placeholder="请输入新的用户名"
            ></el-input>
          </el-form-item>
          <el-form-item label="" prop="passWord">
            <el-input
              type="password"
              autocomplete="off"
              v-model="regForm.passWord"
              prefix-icon="el-icon-lock"
              placeholder="请输入新密码"
            ></el-input>
          </el-form-item>
          <el-form-item label="" prop="checkPass">
            <el-input
              type="password"
              autocomplete="off"
              v-model="regForm.checkPass"
              prefix-icon="el-icon-lock"
              placeholder="请再次输入新密码"
            ></el-input>
          </el-form-item>
          <el-form-item label="" prop="userEmail">
            <el-input
              type="email"
              autocomplete="off"
              v-model="regForm.userEmail"
              prefix-icon="el-icon-user-solid"
              placeholder="请输入邮箱"
            ></el-input>
          </el-form-item>
          <el-form-item class="btns1">
            <el-button type="primary" @click="submitForm('regForm')"
              >注册</el-button
            >
            <el-button @click="resetForm">重置</el-button>
          </el-form-item>
          <el-form-item class="btns2">
            <router-link style="text-decoration: none" to="/">
              <el-link :underline="false" type="primary">返回首页</el-link>
            </router-link>
            <router-link
              :underline="false"
              style="text-decoration: none"
              to="/login"
            >
              <el-link :underline="false" type="primary">登录</el-link>
            </router-link>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>
 
<script>
export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.regForm.checkPass !== "") {
          if (value.length < 6 || value.length > 16) {
            callback(new Error("密码长度在6到16个字符"));
          }
          this.$refs.regForm.validateField("checkPass");
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.regForm.passWord) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    var validateEmail = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入邮箱"));
      } else {
        if (value !== "") {
          var reg =
            /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
          if (!reg.test(value)) {
            callback(new Error("请输入有效的邮箱"));
          }
        }
        callback();
      }
    };
    return {
      starsCount: 2000,
      distance: 800,
      vedioCanPlay: false,
      fixStyle: "",
      form: { role: 1 },
      regForm: {
        userName: "",
        passWord: "",
        checkPass: "",
        userEmail: "",
      },
      rules: {
        userName: [
          { required: true, message: "请输入新的用户名", trigger: "blur" },
          {
            min: 3,
            max: 8,
            message: "用户名长度在3到8个字符",
            trigger: "blur",
          },
        ],
        passWord: [
          { required: true, validator: validatePass, trigger: "blur" },
        ],
        checkPass: [
          { required: true, validator: validatePass2, trigger: "blur" },
        ],
        userEmail: [
          { required: true, validator: validateEmail, trigger: "blur" },
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
    submitForm(formName) {
      this.$refs["regForm"].validate((valid) => {
        if (valid) {
          let config = {
            headers: {
              "Content-Type": "application/json",
            },
          };

          let data = {
            username: this.regForm.userName,
            password: this.regForm.passWord,
            email: this.regForm.userEmail,
          };

          this.$axios
            .post("/register", data, config)
            .then((response) => {
              console.log(response.data);
              // 注册成功 auth返回值为0
              // 用户名已被使用 auth返回值为1
              // 注册邮箱已被使用 auth返回值为2
              if (response.data["auth"] == 0) {
                this.$message.success("注册成功 正在前往登录界面");
                // 可以考虑加入适当的延迟
                this.$router.push("/login");
              } else if (response.data["auth"] == 1) {
                this.$message.error("注册失败 用户名已被使用");
              } else if (response.data["auth"] == 2) {
                this.$message.error("注册失败 注册邮箱已被使用");
              } else {
                // this line should not be run
                this.$message.error("注册失败（未知错误）");
              }
            })
            .catch(function (error) {
              console.log(error);
              this.$message.error("注册失败");
            });
        } else {
          this.$message.error("注册失败");
          return false;
        }
      });
    },
    resetForm() {
      this.$refs["regform"].resetFields();
    },
    handleClick() {},
    sleep(numberMillis) {
      var now = new Date();
      var exitTime = now.getTime() + numberMillis;
      while (true) {
        now = new Date();
        if (now.getTime() > exitTime) return;
      }
    },
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

.reg_form {
  width: 400px;
  height: 450px;
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
