<template>
  <div class="app-container">
    <el-col :span="24" :xs="24">
      <el-card>
        <el-tabs v-model="activeTab">
          <el-tab-pane label="自选交易" name="activity">
            <trans-card />
          </el-tab-pane>
          <el-tab-pane label="交易记录" name="timeline">
            <record-card />
          </el-tab-pane>
        </el-tabs>
      </el-card>
    </el-col>
  </div>
</template>

<script>
import TransCard from "./TransCard";
import RecordCard from "./RecordCard";
export default {
  components: { TransCard, RecordCard },
  name: "transaction",
  data() {
    return {
      activeTab: "activity",
    };
  },
};
</script>

<style lang="scss" scoped>
</style>