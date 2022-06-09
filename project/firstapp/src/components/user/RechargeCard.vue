<!-- 用于检验是否能实现点击页面左边,页面右侧出现相应的画面 -->
<template>
  <div class="app-container">
    <el-form
      ref="rechargeForm"
      :model="rechargeForm"
      :rules="rules"
      label-width="120px"
    >
      <el-form-item label="充值金额" prop="money">
        <el-input
          type="text"
          autocomplete="off"
          v-model="rechargeForm.money"
          prefix-icon="el-icon-money"
          placeholder="请输入充值金额"
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit('rechargeForm')">充值</el-button>
        <el-button @click="onReset">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import Cookies from 'js-cookie';
import { Message } from "element-ui";
export default {
  data() {
    return {
      rechargeForm: {
        money: "",
      },
      rules: {
        money: [
          { required: false, message: "请输入充值金额", trigger: "blur" },
        ],
      },
    };
  },
  methods: {
    onSubmit(formName) {
      this.$refs["rechargeForm"].validate((valid) => {
        if (valid) {
          let config = {
            headers: {
              "Content-Type": "application/json",
            },
          };

          let data = {
            type: "money",
            username: Cookies.get("username"),
            money: this.rechargeForm.money,
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
                Message.success("充值成功");
                window.location.reload();
              } else if (response.data["auth"] === 1) {
                Message.error("充值失败,充值格式不正确");
              } else {
                Message.error("充值失败");
              }
            })
            .catch((error) => {
              console.log(error);
              Message.error("充值失败");
            });
        }
      });
    },
    onReset() {
      this.$refs["rechargeForm"].resetFields();
    },
    handleClick() {},
  },
};
</script>

<style scoped>
.line {
  text-align: center;
}
</style>


