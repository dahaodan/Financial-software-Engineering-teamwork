<template>
  <div class="app-container">
    <el-col :span="24" :xs="24">
      <el-card>
        <simulation-card />
      </el-card>
    </el-col>
  </div>
</template>

<script>
import SimulationCard from "./SimulationCard";

export default {
  components: { SimulationCard },
  name: "simulation",
};
</script>

<style lang="scss" scoped>
</style>