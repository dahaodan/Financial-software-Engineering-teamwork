<template>
  <div :class="className" :style="{ height: height, width: width }" />
</template>

<script>
import * as echarts from "echarts";
require("echarts/theme/macarons"); // echarts theme
const month = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"];
const year = ["2017", "2018", "2019", "2020"];
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
      var data = rawData.map(function (item) {
        return [item[1], item[0], item[2] || "-"];
      });
      var option = {
        title: {
            text: "Monthly IC",
        },
        tooltip: {
          position: "top",
        },
        legend: {
          bottom: 10,
          left: "center",
          data: ["Monthly IC"],
        },
        grid: {
          height: "60%",
          top: "10%",
        },
        xAxis: {
          type: "category",
          data: month,
          splitArea: {
            show: true,
          },
        },
        yAxis: {
          type: "category",
          data: year,
          splitArea: {
            show: true,
          },
        },
        visualMap: {
          min: -0.1,
          max: 0.1,
          calculable: true,
          orient: "horizontal",
          left: "center",
          bottom: "10%",
        },
        series: [
          {
            name: "Monthly IC",
            type: "heatmap",
            data: data,
            label: {
              show: true,
            },
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
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
