<!-- 用于检验是否能实现点击页面左边,页面右侧出现相应的画面 -->
<template>
  <div class="app-container">
    <el-form
      ref="passwordForm"
      :model="passwordForm"
      :rules="rules"
      label-width="120px"
    >
      <el-form-item label="新密码" prop="passWord">
        <el-input
          type="password"
          autocomplete="off"
          v-model="passwordForm.passWord"
          prefix-icon="el-icon-lock"
          placeholder="请输入新密码"
        ></el-input>
      </el-form-item>
      <el-form-item label="再次输入新密码" prop="checkPass">
        <el-input
          type="password"
          autocomplete="off"
          v-model="passwordForm.checkPass"
          prefix-icon="el-icon-lock"
          placeholder="请再次输入新密码"
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit('passwordForm')"
          >提交</el-button
        >
        <el-button @click="onReset">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import Cookies from "js-cookie";
import { Message } from "element-ui";
export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.passwordForm.checkPass !== "") {
          if (value.length < 6 || value.length > 16) {
            callback(new Error("密码长度在6到16个字符"));
          }
          this.$refs.passwordForm.validateField("checkPass");
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.passwordForm.passWord) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    return {
      passwordForm: {
        passWord: "",
        checkPass: "",
      },
      rules: {
        passWord: [
          { required: false, validator: validatePass, trigger: "blur" },
        ],
        checkPass: [
          { required: false, validator: validatePass2, trigger: "blur" },
        ],
      },
    };
  },
  methods: {
    onSubmit(formName) {
      this.$refs["passwordForm"].validate((valid) => {
        if (valid) {
          let config = {
            headers: {
              "Content-Type": "application/json",
            },
          };

          let data = {
            type: "password",
            username: Cookies.get("username"),
            password: this.passwordForm.passWord,
          };

          this.$axios
            .post("/userinfo", data, config)
            .then((response) => {
              console.log(response.data);
              if (response.data["auth"] === 0) {
                localStorage.clear();
                localStorage.setItem("token", response.data);
                Cookies.set("username", response.data["username"]);
                Cookies.set("email", response.data["email"]);
                Cookies.set("money", response.data["money"]);
                Cookies.set("profile", response.data["profile"]);
                Message.success("修改成功");
                window.location.reload();
              } else {
                Message.error("修改失败");
              }
            })
            .catch((error) => {
              console.log(error);
              Message.error("修改失败");
            });
        }
      });
    },
    onReset() {
      this.$refs["passwordForm"].resetFields();
    },
  },
};
</script>

<style scoped>
.line {
  text-align: center;
}
</style>


