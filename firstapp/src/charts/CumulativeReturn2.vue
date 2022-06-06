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
      let data6 = [];
      let data7 = [];
      let data8 = [];
      let data9 = [];
      let data10 = [];
      for (let i = 1; i < rawData.length; i++) {
        categoryData.push(rawData[i][0]);
        data6.push(rawData[i][6]);
        data7.push(rawData[i][7]);
        data8.push(rawData[i][8]);
        data9.push(rawData[i][9]);
        data10.push(rawData[i][10]);
      }
      return {
        categoryData: categoryData,
        data6: data6,
        data7: data7,
        data8: data8,
        data9: data9,
        data10: data10,
      };
    },
    setOptions(rawData) {
      var data = this.splitData(rawData);
      var option = {
        title: {
            text: "Graph2 for cumulative return and max drawdown"
        },
        animation: false,
        legend: {
          bottom: 10,
          left: "center",
          data: [
            "cum_ex_return_wo_cost",
            "cum_ex_return_w_cost",
            "cum_ex_return_wo_cost_mdd",
            "cum_ex_return_w_cost_mdd",
            "turnover",
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
            height: "36%",
          },
          {
            left: "10%",
            right: "8%",
            top: "50%",
            height: "13%",
          },
          {
            left: "10%",
            right: "8%",
            top: "65%",
            height: "13%",
          },
          {
            left: "10%",
            right: "8%",
            top: "80%",
            height: "13%",
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
          {
            type: "category",
            gridIndex: 1,
            data: data.categoryData,
            boundaryGap: false,
            axisLine: {
              onZero: false,
            },
            axisTick: { show: false },
            splitLine: { show: false },
            axisLabel: { show: false },
            min: "dataMin",
            max: "dataMax",
          },
          {
            type: "category",
            gridIndex: 2,
            data: data.categoryData,
            boundaryGap: false,
            axisLine: {
              onZero: false,
            },
            axisTick: { show: false },
            splitLine: { show: false },
            axisLabel: { show: false },
            min: "dataMin",
            max: "dataMax",
          },
          {
            type: "category",
            gridIndex: 3,
            data: data.categoryData,
            boundaryGap: false,
            axisLine: {
              onZero: false,
            },
            axisTick: { show: false },
            splitLine: { show: false },
            axisLabel: { show: false },
            min: "dataMin",
            max: "dataMax",
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
          {
            scale: true,
            gridIndex: 1,
            splitNumber: 2,
            axisLine: {
              lineStyle: {
                color: "black",
              },
            },
          },
          {
            scale: true,
            gridIndex: 2,
            splitNumber: 2,
            axisLine: {
              lineStyle: {
                color: "black",
              },
            },
          },
          {
            scale: true,
            gridIndex: 3,
            splitNumber: 2,
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
        //     xAxisIndex: [0, 1, 2, 3],
        //     start: 0,
        //     end: 100,
        //   },
        //   {
        //     show: true,
        //     xAxisIndex: [0, 1, 2, 3],
        //     type: "slider",
        //     top: "85%",
        //     start: 50,
        //     end: 100,
        //   },
        // ],
        series: [
          {
            name: "cum_ex_return_wo_cost",
            type: "line",
            data: data.data6,
            smooth: true,
            lineStyle: {
              opacity: 5,
              color: "rgb(255, 120, 120)",
            },
            itemStyle: {
              color: "rgb(255, 120, 120)",
            },
          },
          {
            name: "cum_ex_return_w_cost",
            type: "line",
            data: data.data7,
            smooth: true,
            lineStyle: {
              opacity: 5,
              color: "rgb(200, 150, 200)",
            },
            itemStyle: {
              color: "rgb(200, 150, 200)",
            },
          },
          {
            name: "cum_ex_return_wo_cost_mdd",
            type: "line",
            symbol: "none",
            xAxisIndex: 1,
            yAxisIndex: 1,
            sampling: "lttb",
            itemStyle: {
              color: "rgb(255, 70, 131)",
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: "rgb(255, 158, 68)",
                },
                {
                  offset: 1,
                  color: "rgb(255, 70, 131)",
                },
              ]),
            },
            data: data.data8,
          },
          {
            name: "cum_ex_return_w_cost_mdd",
            type: "line",
            symbol: "none",
            xAxisIndex: 2,
            yAxisIndex: 2,
            sampling: "lttb",
            itemStyle: {
              color: "rgb(139, 0, 0)",
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: "rgb(139, 50, 50)",
                },
                {
                  offset: 1,
                  color: "rgb(139, 100, 100)",
                },
              ]),
            },
            data: data.data9,
          },
          {
            name: "turnover",
            type: "line",
            xAxisIndex: 3,
            yAxisIndex: 3,
            data: data.data10,
            smooth: true,
            lineStyle: {
              opacity: 5,
              color: "rgb(255, 193, 193)",
            },
            itemStyle: {
              color: "rgb(255, 193, 193)",
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