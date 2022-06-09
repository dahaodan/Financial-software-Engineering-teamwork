<template>
  <div :class="className" :style="{ height: height, width: width }" />
</template>

<script>
import * as echarts from "echarts";
require("echarts/theme/macarons"); // echarts theme
const upColor = "#00da3c";
const downColor = "#ec0000";
export default {
  props: {
    className: {
      type: String,
      default: "chart",
    },
    width: {
      type: String,
      default: "100%",
    },
    height: {
      type: String,
      default: "400px",
    },
    autoResize: {
      type: Boolean,
      default: true,
    },
    chartData: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      chart: null,
    };
  },
  watch: {
    immediate: true,
    chartData: {
      deep: true,
      handler(val) {
        console.log(val);
        this.setOptions(val);
      },
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart();
    });
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, "macarons");
      this.setOptions(this.chartData);
    },
    setOptions(rawData) {
      console.log(rawData);
      var option = {
        title: {
            text: "Risk analysis for excess return without and with cost"
        },
        legend: {
            bottom: 10,
        },
        tooltip: {},
        // dataset: {
        //   source: [
        //     [
        //       "category",
        //       "std",
        //       "annualized return",
        //       "information ratio",
        //       "max drawdown",
        //     ],
        //     [
        //       "excess_return_without_cost",
        //       rawData[0][1],
        //       rawData[0][2],
        //       rawData[0][3],
        //       rawData[0][4],
        //     ],
        //     [
        //       "excess_return_with_cost",
        //       rawData[1][1],
        //       rawData[1][2],
        //       rawData[1][3],
        //       rawData[1][4],
        //     ],
        //     // ["std", rawData[0][1]],
        //     // ["annualized return", rawData[1][1]],
        //     // ["information ratio", rawData[0][3], rawData[1][3]],
        //     // ["max drawdown", rawData[0][4], rawData[1][4]],
        //   ],
        // },
        xAxis: [
          { type: "category", gridIndex: 0, data:["excess_return_wo_cost", "excess_return_w_cost"]},
          { type: "category", gridIndex: 1, data:["excess_return_wo_cost", "excess_return_w_cost"]},
          { type: "category", gridIndex: 2, data:["excess_return_wo_cost", "excess_return_w_cost"]},
          { type: "category", gridIndex: 3, data:["excess_return_wo_cost", "excess_return_w_cost"]},
        ],
        yAxis: [
          { gridIndex: 0 },
          { gridIndex: 1 },
          { gridIndex: 2 },
          { gridIndex: 3 },
        ],
        grid: [
          { bottom: "55%", right: "55%" },
          { bottom: "55%", left: "55%" },
          { top: "55%", right: "55%" },
          { top: "55%", left: "55%" },
        ],
        series: [
          { type: "bar", name: "std", xAxisIndex: 0, yAxisIndex: 0, data:[rawData[0][1], rawData[1][1]]},
          { type: "bar", name: "annualized_return", xAxisIndex: 1, yAxisIndex: 1, data:[rawData[0][2], rawData[1][2]]},
          { type: "bar", name: "information_ratio", xAxisIndex: 2, yAxisIndex: 2, data:[rawData[0][3], rawData[1][3]]},
          { type: "bar", name: "max_drawdown", xAxisIndex: 3, yAxisIndex: 3, data:[rawData[0][4], rawData[1][4]]},
        ],
      };
      this.chart.setOption(option);
    },
  },
};
</script>

<style scoped>
</style>