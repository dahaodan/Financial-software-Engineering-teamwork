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
    splitData(rawData) {
      let categoryData = [];
      let data1 = [];
   
      for (let i = 1; i < rawData.length; i++) {
        categoryData.push(rawData[i][0]);
        data1.push(rawData[i][1]);
    
      }
      return {
        categoryData: categoryData,
        data1: data1,
   
      };
    },
    setOptions(rawData) {
      var data = this.splitData(rawData);
      var option = {
        title: {
            text: "Auto Correlation"
        },
        animation: false,
        legend: {
          bottom: 10,
          left: "center",
          data: [
            "Auto Correlation",
        
          ],
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
          seriesIndex: 5,
          dimension: 2,
          pieces: [
            {
              value: 1,
              color: downColor,
            },
            {
              value: -1,
              color: upColor,
            },
          ],
        },
        grid: [
          {
            left: "10%",
            right: "8%",
            height: "60%",
          },
        ],
        xAxis: [
          {
            type: "category",
            data: data.categoryData,
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
              },
            },
          },
        ],
        // dataZoom: [
        //   {
        //     type: "inside",
        //     xAxisIndex: [0],
        //     start: 0,
        //     end: 100,
        //   },
        //   {
        //     show: true,
        //     xAxisIndex: [0],
        //     type: "slider",
        //     top: "85%",
        //     start: 50,
        //     end: 100,
        //   },
        // ],
        series: [
          {
            name: "Auto Correlation",
            type: "line",
            data: data.data1,
            smooth: true,
            lineStyle: {
              opacity: 5,
            },
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
