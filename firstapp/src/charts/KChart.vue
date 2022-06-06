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
      default: "500px",
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
      let values = [];
      let volumes = [];
      for (let i = 0; i < rawData.length; i++) {
        categoryData.push(rawData[i][0]);
        values.push([
          rawData[i][1],
          rawData[i][2],
          rawData[i][3],
          rawData[i][4],
        ]);
        volumes.push([
          i,
          rawData[i][5],
          rawData[i][1] > rawData[i][2] ? 1 : -1,
        ]);
      }
      return {
        categoryData: categoryData,
        values: values,
        volumes: volumes,
      };
    },
    calculateMA(dayCount, data) {
      var result = [];
      for (var i = 0, len = data.values.length; i < len; i++) {
        if (i < dayCount) {
          result.push("-");
          continue;
        }
        var sum = 0;
        for (var j = 0; j < dayCount; j++) {
          sum += data.values[i - j][1];
        }
        result.push(+(sum / dayCount).toFixed(3));
      }
      return result;
    },
    setOptions(rawData) {
      var data = this.splitData(rawData);
      var option = {
        animation: false,
        legend: {
          bottom: 10,
          left: "center",
          data: ["Index", "MA5", "MA10", "MA20"],
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
          },
          backgroundColor: 'white',
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
          // extraCssText: 'width: 170px'
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
          seriesIndex: 4,
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
            height: "50%",
          },
          {
            left: "10%",
            right: "8%",
            top: "70%",
            height: "16%",
          },
        ],
        xAxis: [
          {
            type: "category",
            data: data.categoryData,
            boundaryGap: false,
            axisLine: {
              onZero: false,
              lineStyle: {
                color: "black",
              },
            },
            splitLine: { show: false },
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
            axisLabel: { show: false },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: { show: false },
          },
        ],
        dataZoom: [
          {
            type: "inside",
            xAxisIndex: [0, 1],
            start: 90,
            end: 100,
          },
          {
            show: true,
            xAxisIndex: [0, 1],
            type: "slider",
            top: "85%",
            start: 50,
            end: 100,
          },
        ],
        series: [
          {
            name: "Index",
            type: "candlestick",
            data: data.values,
            itemStyle: {
              color: upColor,
              color0: downColor,
              borderColor: undefined,
              borderColor0: undefined,
            },
            tooltip: {
              formatter: function (param) {
                param = param[0];
                return [
                  "Date: " + param.name + '<hr size=1 style="margin: 3px 0">',
                  "Open: " + param.data[0] + "<br/>",
                  "Close: " + param.data[1] + "<br/>",
                  "Lowest: " + param.data[2] + "<br/>",
                  "Highest: " + param.data[3] + "<br/>",
                ].join("");
              },
            },
          },
          {
            name: "MA5",
            type: "line",
            data: this.calculateMA(5, data),
            smooth: true,
            lineStyle: {
              opacity: 0.5,
            },
          },
          {
            name: "MA10",
            type: "line",
            data: this.calculateMA(10, data),
            smooth: true,
            lineStyle: {
              opacity: 0.5,
            },
          },
          {
            name: "MA20",
            type: "line",
            data: this.calculateMA(20, data),
            smooth: true,
            lineStyle: {
              opacity: 0.5,
            },
          },
          {
            name: "Volume",
            type: "bar",
            xAxisIndex: 1,
            yAxisIndex: 1,
            data: data.volumes,
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
