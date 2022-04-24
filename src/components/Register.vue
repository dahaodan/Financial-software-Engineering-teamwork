<template>
  <!-- 注册框 -->
  <el-form
    :model="ruleForm"
    :rules="rules"
    ref="ruleForm"
    class="demo-ruleForm"
  >
    <el-form-item label="" prop="name"
      ><el-input
        type="text"
        autocomplete="off"
        v-model="ruleForm.name"
        prefix-icon="el-icon-user-solid"
        placeholder="请输入新的用户名"
      ></el-input
    ></el-form-item>
    <el-form-item label="" prop="pass"
      ><el-input
        type="password"
        autocomplete="off"
        v-model="ruleForm.pass"
        prefix-icon="el-icon-lock"
        placeholder="请设置密码"
      ></el-input
    ></el-form-item>
    <el-form-item label="" prop="checkPass"
      ><el-input
        type="password"
        autocomplete="off"
        v-model="ruleForm.checkPass"
        prefix-icon="el-icon-lock"
        placeholder="请再次输入密码"
      ></el-input
    ></el-form-item>
    <el-form-item label="" prop="email"
      ><el-input
        type="email"
        autocomplete="off"
        v-model="ruleForm.email"
        prefix-icon="el-icon-user-solid"
        placeholder="请输入邮箱"
      ></el-input
    ></el-form-item>
    <el-form-item class="btns">
      <el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
      <el-button @click="resetForm('ruleForm')">重置</el-button>
    </el-form-item>
  </el-form>
</template>
 
<script>
export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.ruleForm.checkPass !== "") {
          if (value.length < 8 || value.length > 32) {
            callback(new Error("密码长度在 8 到 32 个字符"));
          }
          this.$refs.ruleForm.validateField("checkPass");
        }
        callback();
      }
    };

    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.ruleForm.pass) {
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
      activeName: "second",
      ruleForm: {
        name: "",
        pass: "",
        checkPass: "",
      },
      rules: {
        name: [
          { required: true, message: "请输入新的用户名", trigger: "blur" },
          {
            min: 2,
            max: 32,
            message: "用户名长度在 2 到 32 个字符",
            trigger: "blur",
          },
          // Todo: 需要验证新的用户名是否与已有的用户名重复
        ],
        pass: [{ required: true, validator: validatePass, trigger: "blur" }],
        checkPass: [
          { required: true, validator: validatePass2, trigger: "blur" },
        ],
        email: [
          { required: true, validator: validateEmail, trigger: "blur" },
          // Todo: 需要验证注册邮箱是否与已有的注册邮箱重复
        ],
      },
    };
  },

  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$message({
            type: "success",
            message: "注册成功",
          });
          // Todo: 注册成功，后端传递注册信息
          // this.activeName: 'first',
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },

    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
};
</script>


<style scoped>
.login_container {
  background-color: #42b983;
  height: 100%;
}
