<template>
  <div>
    <el-row :gutter="40" class="show-index">
      <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
        <div class="chart-wrapper"><strong>OPEN</strong> {{ this.open }}</div>
      </el-col>
      <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
        <div class="chart-wrapper"><strong>CLOSE</strong> {{ this.close }}</div>
      </el-col>
      <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
        <div class="chart-wrapper"><strong>HIGH</strong> {{ this.high }}</div>
      </el-col>
      <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
        <div class="chart-wrapper"><strong>LOW</strong> {{ this.low }}</div>
      </el-col>
    </el-row>

    <el-row :gutter="40" class="show-index">
      <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
        <div class="chart-wrapper"><strong>VOL</strong> {{ this.vol }}</div>
      </el-col>
      <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
        <div class="chart-wrapper"><strong>MACD</strong> {{ this.macd }}</div>
      </el-col>
      <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
        <div class="chart-wrapper"><strong>DIFF</strong> {{ this.diff }}</div>
      </el-col>
      <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
        <div class="chart-wrapper"><strong>DEA</strong> {{ this.dea }}</div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  props: {
    chartData: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      open: "",
      close: "",
      high: "",
      low: "",
      vol: "",
      macd: "",
      diff: "",
      dea: "",
    };
  },
  watch: {
    immediate: true,
    chartData: {
      deep: true,
      handler(val) {
        console.log(val);
        this.setData(val);
      },
    },
  },
  methods: {
    setData(rawData) {
      this.open = rawData[rawData.length - 1][1];
      this.close = rawData[rawData.length - 1][2];
      this.high = rawData[rawData.length - 1][3];
      this.low = rawData[rawData.length - 1][4];
      this.vol = rawData[rawData.length - 1][5];
      this.macd = rawData[rawData.length - 1][6];
      this.diff = rawData[rawData.length - 1][7];
      this.dea = rawData[rawData.length - 1][8];
    },
  },
};
</script>

<style lang="scss" scoped>
.show-index{
  .card-panel-col {
    font-size: 18px;
    margin-bottom: 32px;
  }
}

@media (max-width: 1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>