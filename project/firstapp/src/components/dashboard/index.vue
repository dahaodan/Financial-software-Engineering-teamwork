<template>
  <div class="dashboard-editor-container">
    <panel-group @handleSetKChartData="handleSetKChartData" />

    <el-row style="background: #fff; padding: 16px 16px 0; margin-bottom: 32px">
      <KChart :chart-data="chartData"></KChart>
    </el-row>

    <el-row style="background: #fff; padding: 32px 16px 0; margin-bottom: 32px">
      <ShowIndex :chart-data="chartData"></ShowIndex>
    </el-row>

    <el-row :gutter="24">
      <el-col
        :xs="{ span: 24 }"
        :sm="{ span: 24 }"
        :md="{ span: 24 }"
        :lg="{ span: 24 }"
        :xl="{ span: 8 }"
        style="padding-right: 8px; margin-bottom: 30px"
      >
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="font-size: 32px">宏观研究</span>
            <el-button
              style="font-size: 16px; float: right; padding: 3px 0"
              type="text" @click='gotoResearch'
              >更多</el-button
            >
          </div>
          <div v-for="item in this.research" :key="item" class="text-item">
            <el-link
              @click="mylink(item)"
              style="margin-bottom: 20px; font-size: 16px"
              >{{ item[0] }}</el-link
            >
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import PanelGroup from "./PanelGroup";
import ShowIndex from "./ShowIndex";
import KChart from "@/charts/KChart";

export default {
  name: "DashboardAdmin",
  components: {
    PanelGroup,
    ShowIndex,
    KChart,
  },
  data() {
    return {
      SSEC: {},
      SZI: {},
      GEI: {},
      CSI300: {},
      chartData: [],
      research: "",
    };
  },
  methods: {
    getData() {
      this.$axios
        .get("./dashboard")
        .then((response) => {
          this.SSEC = Object(response.data["SSEC"]);
          console.log(this.SSEC)
          this.SZI = Object(response.data["SZI"]);
          console.log(this.SZI)
          this.GEI = Object(response.data["GEI"]);
          this.CSI300 = Object(response.data["CSI300"]);
          this.research = response.data["Research"];
          this.chartData = this.SSEC;
          this.open = this.SSEC[response.data["SSEC"].length - 1][1];
          this.close = this.SSEC[response.data["SSEC"].length - 1][2];
          this.high = this.SSEC[response.data["SSEC"].length - 1][3];
          this.low = this.SSEC[response.data["SSEC"].length - 1][4];
          this.vol = this.SSEC[response.data["SSEC"].length - 1][5];
          this.macd = this.SSEC[response.data["SSEC"].length - 1][6];
          this.diff = this.SSEC[response.data["SSEC"].length - 1][7];
          this.dea = this.SSEC[response.data["SSEC"].length - 1][8];
        })
        .catch((error) => {
          console.log(error);
        });
    },
    handleSetKChartData(type) {
      if (type === "SZI") {
        this.chartData = this.SZI;
        this.open = this.SZI[response.data["SZI"].length - 1][1];
        this.close = this.SZI[response.data["SZI"].length - 1][2];
        this.high = this.SZI[response.data["SZI"].length - 1][3];
        this.low = this.SZI[response.data["SZI"].length - 1][4];
        this.vol = this.SZI[response.data["SZI"].length - 1][5];
        this.macd = this.SZI[response.data["SZI"].length - 1][6];
        this.diff = this.SZI[response.data["SZI"].length - 1][7];
        this.dea = this.SZI[response.data["SZI"].length - 1][8];
      } else if (type === "GEI") {
        this.chartData = this.GEI;
        this.open = this.GEI[response.data["GEI"].length - 1][1];
        this.close = this.GEI[response.data["GEI"].length - 1][2];
        this.high = this.GEI[response.data["GEI"].length - 1][3];
        this.low = this.GEI[response.data["GEI"].length - 1][4];
        this.vol = this.GEI[response.data["GEI"].length - 1][5];
        this.macd = this.GEI[response.data["GEI"].length - 1][6];
        this.diff = this.GEI[response.data["GEI"].length - 1][7];
        this.dea = this.GEI[response.data["GEI"].length - 1][8];
      } else if (type === "CSI300") {
        this.chartData = this.CSI300;
        this.open = this.CSI300[response.data["CSI300"].length - 1][1];
        this.close = this.CSI300[response.data["CSI300"].length - 1][2];
        this.high = this.CSI300[response.data["CSI300"].length - 1][3];
        this.low = this.CSI300[response.data["CSI300"].length - 1][4];
        this.vol = this.CSI300[response.data["CSI300"].length - 1][5];
        this.macd = this.CSI300[response.data["CSI300"].length - 1][6];
        this.diff = this.CSI300[response.data["CSI300"].length - 1][7];
        this.dea = this.CSI300[response.data["CSI300"].length - 1][8];
      } else {
        this.chartData = this.SSEC;
        this.open = this.SSEC[response.data["SSEC"].length - 1][1];
        this.close = this.SSEC[response.data["SSEC"].length - 1][2];
        this.high = this.SSEC[response.data["SSEC"].length - 1][3];
        this.low = this.SSEC[response.data["SSEC"].length - 1][4];
        this.vol = this.SSEC[response.data["SSEC"].length - 1][5];
        this.macd = this.SSEC[response.data["SSEC"].length - 1][6];
        this.diff = this.SSEC[response.data["SSEC"].length - 1][7];
        this.dea = this.SSEC[response.data["SSEC"].length - 1][8];
      }
    },
    mydecimal(val) {
      return Number(val).toFixed(2);
    },
    mylink(val) {
      window.open(val[1]);
    },
    gotoResearch(){
      this.$router.push('/research')
    }
  },
  mounted: function () {
    this.getData();
  },
};
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .github-corner {
    position: absolute;
    top: 0px;
    border: 0;
    right: 0;
  }

  .chart-wrapper {
    color: rgb(0, 0, 0);
    font-size: 20px;
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}

@media (max-width: 1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>