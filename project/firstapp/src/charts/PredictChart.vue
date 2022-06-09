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
      // default: "100%",
      default: "800px",
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
      var categoryData = [];
      var data0 = rawData[0];
      var data1 = rawData[1];
      for (var i = 0; i < data1.length; ++i) {
        categoryData.push(i);
      }
      console.log(categoryData);
      var option = {
        animation: false,
        legend: {
          bottom: 10,
          left: "center",
          data: ["Train", "Predict"],
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
          },
          backgroundColor: "white",
          borderWidth: 1,
          borderColor: "#ccc",
          padding: 10,
          textStyle: {
            color: "#000",
          },
          position: function (pos, params, el, elRect, size) {
            const obj = {
              top: 10,
            };
            obj[["left", "right"][+(pos[0] < size.viewSize[0] / 2)]] = 30;
            return obj;
          },
        },
        axisPointer: {
          link: [
            {
              xAxisIndex: "all",
            },
          ],
          label: {
            backgroundColor: "#777",
          },
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: false,
            },
            brush: {
              type: ["lineX", "clear"],
            },
          },
        },
        brush: {
          xAxisIndex: "all",
          brushLink: "all",
          outOfBrush: {
            colorAlpha: 0.1,
          },
        },
        visualMap: {
          show: false,
          seriesIndex: 2,
          dimension: 0,
          pieces: [
            {
              lte: 998,
              color: downColor,
            },
            {
              gt: 998,
              color: upColor,
            },
          ],
        },
        grid: [
          {
            left: "10%",
            right: "5%",
            height: "60%",
          },
        ],
        xAxis: [
          {
            type: "category",
            data: categoryData,
            boundaryGap: false,
            axisLine: {
              onZero: false,
            },
            splitLine: { show: false },
            axisTick: { show: false },
            axisLabel: { show: false },
            min: "dataMin",
            max: "dataMax",
            axisPointer: {
              z: 100,
            },
          },
        ],
        yAxis: [
          {
            scale: true,
            splitArea: {
              show: true,
            },
            axisLine: {
              lineStyle: {
                color: "black",
              },
            },
          },
        ],
        // dataZoom: [
        //   {
        //     type: "inside",
        //     xAxisIndex: [0, 1, 2],
        //     start: 0,
        //     end: 100,
        //   },
        //   {
        //     show: true,
        //     xAxisIndex: [0, 1, 2],
        //     type: "slider",
        //     top: "85%",
        //     start: 50,
        //     end: 100,
        //   },
        // ],
        series: [
          {
            name: "Train",
            type: "line",
            data: data0,
            smooth: true,
            lineStyle: {
              opacity: 5,
              color: "red",
            },
            itemStyle: {
                color: "red",
            }
          },
          {
            name: "Predict",
            type: "line",
            data: data1,
            smooth: true,
            lineStyle: {
              opacity: 5,
              color: "blue",
            },
            itemStyle: {
                color: "blue",
            }
          },
        ],
      };
      this.chart.setOption(option);
    },
  },
};
</script>

<style scoped>
</style>
