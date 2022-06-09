<template>
  <el-card style="margin-bottom: 20px">
    <div slot="header" class="clearfix">
      <span><strong style="font-size: 20px">About me</strong></span>
    </div>
    <div class="user-profile">
      <div class="box-center">
        <pan-thumb :height="'100px'" :width="'100px'" :hoverable="false">
          <a>Have a nice day!</a>
        </pan-thumb>
      </div>
      <div class="box-center">
        <div class="user-name text-center">
          {{ showUsername }}
          <el-link icon="el-icon-edit" @click="openUsername"></el-link>
        </div>
        <div class="user-email text-center textmuted">
          <strong>{{ showEmail }}</strong>
          <el-link icon="el-icon-edit" @click="openEmail"></el-link>
        </div>
        <div class="user-money text-center textmuted">
          <strong>账户余额: {{ showMoney }}</strong>
        </div>
      </div>
    </div>
    <div class="user-bio">
      <div class="user-education user-bio-section">
        <div class="user-bio-section-header">
          <svg-icon icon-class="education" /><span>Personal Profile</span>
          <el-link icon="el-icon-edit" @click="openProfile"></el-link>
        </div>
        <div class="user-bio-section-body">
          <div class="text-muted">
            {{ showProfile }}
          </div>
        </div>
      </div>
    </div>
    <div class="user-bio">
      <div class="user-skills user-bio-section">
        <div class="user-bio-section-header">
          <svg-icon icon-class="skill" /><span>Skills</span>
        </div>
        <div class="user-bio-section-body">
          <div class="progress-item">
            <span>Vue</span>
            <el-progress :percentage="40" />
          </div>
          <div class="progress-item">
            <span>JavaScript</span>
            <el-progress :percentage="20" />
          </div>
          <div class="progress-item">
            <span>Css</span>
            <el-progress :percentage="20" />
          </div>
          <div class="progress-item">
            <span>ESLint</span>
            <el-progress :percentage="0" status="fail" />
          </div>
        </div>
      </div>
    </div>
  </el-card>
</template>
<script>
import PanThumb from "./PanThumb";
import Cookies from "js-cookie";
import { Message } from "element-ui";
export default {
  computed: {
    showUsername() {
      const username = Cookies.get("username");
      if (username) {
        return username;
      } else {
        return "暂未填写";
      }
    },
    showEmail() {
      const email = Cookies.get("email");
      if (email) {
        return email;
      } else {
        return "暂未填写";
      }
    },
    showMoney() {
      const money = Cookies.get("money");
      if (money) {
        return money;
      } else {
        return "暂未填写";
      }
    },
    showProfile() {
      const profile = Cookies.get("profile");
      if (profile) {
        return profile;
      } else {
        return "暂未填写";
      }
    },
  },
  methods: {
    openUsername() {
      this.$prompt("请输⼊新的⽤户名", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          let config = {
            headers: {
              "Content-Type": "application/json",
            },
          };
          let data = {
            type: "username",
            oldusername: Cookies.get("username"),
            newusername: value,
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
              } else if (response.data["auth"] === 1) {
                Message.error("修改失败，用户名长度在3到8个字符");
              } else if (response.data["auth"] === 2) {
                Message.error("修改失败，用户名已被使用");
              } else {
                Message.error("修改失败");
              }
            })
            .catch((error) => {
              console.log(error);
              Message.error("修改失败");
            });
        })
        .catch(() => {});
    },
    openEmail() {
      this.$prompt("请输⼊新的邮箱", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          let config = {
            headers: {
              "Content-Type": "application/json",
            },
          };
          let data = {
            type: "email",
            username: Cookies.get("username"),
            email: value,
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
              } else if (response.data["auth"] === 1) {
                Message.error("修改失败，邮箱格式错误");
              } else if (response.data["auth"] === 2) {
                Message.error("修改失败，邮箱已被使用");
              } else {
                Message.error("修改失败");
              }
            })
            .catch((error) => {
              console.log(error);
              Message.error("修改失败");
            });
        })
        .catch(() => {});
    },
    openProfile() {
      this.$prompt("请编辑个人简介", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          let config = {
            headers: {
              "Content-Type": "application/json",
            },
          };
          let data = {
            type: "profile",
            username: Cookies.get("username"),
            profile: value,
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
        })
        .catch(() => {});
    },
  },
  components: { PanThumb },
};
</script>
<style lang="scss" scoped>
.box-center {
  margin: 0 auto;
  display: table;
}
.text-muted {
  color: #777;
}
.user-profile {
  .user-name {
    text-align: center;
    font-weight: bold;
  }
  .box-center {
    padding-top: 10px;
  }
  .user-email {
    text-align: center;
    padding-top: 10px;
    font-weight: 400;
    font-size: 14px;
  }
  .user-money {
    text-align: center;
    padding-top: 10px;
    font-weight: 400;
    font-size: 14px;
  }
  .box-social {
    padding-top: 30px;
    .el-table {
      border-top: 1px solid #dfe6ec;
    }
  }
  .user-follow {
    padding-top: 20px;
  }
}
.user-bio {
  margin-top: 20px;
  color: #606266;
  span {
    padding-left: 4px;
  }
  .user-bio-section {
    font-size: 14px;
    padding: 15px 0;
    .user-bio-section-header {
      border-bottom: 1px solid #dfe6ec;
      padding-bottom: 10px;
      margin-bottom: 10px;
      font-weight: bold;
    }
  }
}
</style>