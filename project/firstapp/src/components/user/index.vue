<template>
  <div class="app-container">
    <el-row :gutter="20">
      <el-col :span="6" :xs="24">
        <user-card :user="user" />
      </el-col>

      <el-col :span="18" :xs="24">
        <el-card>
          <el-tabs v-model="activeTab">
            <el-tab-pane label="密码更新" name="activity">
              <password-card />
            </el-tab-pane>
            <el-tab-pane label="充值" name="timeline">
              <recharge-card />
            </el-tab-pane>
          </el-tabs>
        </el-card>
      </el-col>

    </el-row>
  </div>
</template>

<script>
// import { mapGetters } from 'vuex'
import UserCard from "./UserCard";
import PasswordCard from './PasswordCard'
import RechargeCard from './RechargeCard'
// import Activity from './components/Activity'
// import Timeline from './components/Timeline'
// import Account from './components/Account'

export default {
  name: "UserInfo",
  components: { PasswordCard, UserCard, RechargeCard},
  data() {
    return {
      activeTab: "activity",
    };
  },
};
</script>


<style scoped>
.line {
  text-align: center;
}
</style>


