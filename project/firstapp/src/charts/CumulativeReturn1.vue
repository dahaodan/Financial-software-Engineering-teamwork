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
      for (let i = 1; i < rawData.length; i++) {
        categoryData.push(rawData[i][0]);
        data1.push(rawData[i][1]);
        data2.push(rawData[i][2]);
        data3.push(rawData[i][3]);
        data4.push(rawData[i][4]);
        data5.push(rawData[i][5]);
      }
      return {
        categoryData: categoryData,
        data1: data1,
        data2: data2,
        data3: data3,
        data4: data4,
        data5: data5,
      };
    },
    setOptions(rawData) {
      var data = this.splitData(rawData);
      var option = {
        title: {
            text: "Graph1 for cumulative return and max drawdown"
        },
        animation: false,
        legend: {
          bottom: 10,
          left: "center",
          data: [
            "cum_bench",
            "cum_return_wo_cost",
            "cum_return_w_cost",
            "return_wo_mdd",
            "return_w_cost_mdd",
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
            height: "45%",
          },
          {
            left: "10%",
            right: "8%",
            top: "60%",
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
            name: "cum_bench",
            type: "line",
            data: data.data1,
            smooth: true,
            lineStyle: {
              opacity: 5,
            },
          },
          {
            name: "cum_return_wo_cost",
            type: "line",
            data: data.data2,
            smooth: true,
            lineStyle: {
              opacity: 5,
            },
          },
          {
            name: "cum_return_w_cost",
            type: "line",
            data: data.data3,
            smooth: true,
            lineStyle: {
              opacity: 5,
            },
          },
          {
            name: "return_w_cost_mdd",
            type: "line",
            symbol: "none",
            xAxisIndex: 1,
            yAxisIndex: 1,
            sampling: "lttb",
            itemStyle: {
              color: "rgb(0,191,255)",
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                
                {
                  offset: 0,
                  color: "rgb(135,206,235)",
                },
                {
                  offset: 1,
                  color: "rgb(30,144,255)",
                },
              ]),
            },
            data: data.data4,
          },
          {
            name: "return_wo_mdd",
            type: "line",
            symbol: "none",
            xAxisIndex: 2,
            yAxisIndex: 2,
            sampling: "lttb",
            itemStyle: {
              color: "rgb(125, 150, 255)",
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: "rgb(150, 150, 255)",
                },
                {
                  offset: 1,
                  color: "rgb(200, 150, 255)",
                },
              ]),
            },
            data: data.data5,
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
