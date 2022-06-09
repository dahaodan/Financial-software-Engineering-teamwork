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
      default: "600px",
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
      let data2 = [];
      let data3 = [];
      let data4 = [];
      let data5 = [];
      let data6 = [];
      let data7 = [];
      for (let i = 1; i < rawData.length; i++) {
        categoryData.push(rawData[i][0]);
        data1.push(rawData[i][1]);
        data2.push(rawData[i][2]);
        data3.push(rawData[i][3]);
        data4.push(rawData[i][4]);
        data5.push(rawData[i][5]);
        data6.push(rawData[i][6]);
        data7.push(rawData[i][7]);
      }
      return {
        categoryData: categoryData,
        data1: data1,
        data2: data2,
        data3: data3,
        data4: data4,
        data5: data5,
        data6: data6,
        data7: data7,
      };
    },
    setOptions(rawData) {
      var data = this.splitData(rawData);
      var option = {
        title: {
            text: "Cumulative return graphics"
        },
        animation: false,
        legend: {
          bottom: 10,
          left: "center",
          data: [
            "Group1",
            "Group2",
            "Group3",
            "Group4",
            "Group5",
            "long-short",
            "long-average",
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
            height: "75%",
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
            name: "Group1",
            type: "line",
            data: data.data1,
            smooth: true,
            lineStyle: {
              opacity: 5,
            },
          },
          {
            name: "Group2",
            type: "line",
            data: data.data2,
            smooth: true,
            lineStyle: {
              opacity: 5,
            },
          },
          {
            name: "Group3",
            type: "line",
            data: data.data3,
            smooth: true,
            lineStyle: {
              opacity: 5,
            },
          },
          {
            name: "Group4",
            type: "line",
            data: data.data4,
            smooth: true,
            lineStyle: {
              opacity: 5,
            },
          },
          {
            name: "Group5",
            type: "line",
            data: data.data5,
            smooth: true,
            lineStyle: {
              opacity: 5,
            },
          },
          {
            name: "long-short",
            type: "line",
            data: data.data6,
            smooth: true,
            lineStyle: {
              opacity: 5,
            },
          },
          {
            name: "long-average",
            type: "line",
            data: data.data7,
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
