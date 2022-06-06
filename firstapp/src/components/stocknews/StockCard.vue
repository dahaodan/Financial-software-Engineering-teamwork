<template>
  <!-- <div class="dashboard-editor-container"> -->
  <div>
    <el-input
      placeholder="请输入内容"
      v-model="fieldInput"
      class="input-with-select"
      style="margin-left: 580px; width: 500px"
      clearable
    >
      <el-button
        slot="append"
        icon="el-icon-search"
        @click="mysearch()"
      ></el-button>
    </el-input>

    <el-row :span="20" :xs="24" style="margin-bottom: 32px"> </el-row>

    <el-row style="background: #fff; padding: 16px 16px 0; margin-bottom: 32px">
      <el-table :data="tableData" ref="singleTable" style="width: 100%" stripe>
        <el-table-column type="expand">
          <template slot-scope="scope">
            <KChart :chart-data="scope.row.chartdata"></KChart>
          </template>
        </el-table-column>

        <el-table-column label="股票代码" width="150">
          <template slot-scope="scope">
            <strong>{{ scope.row.code }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="股票名称" width="150">
          <template slot-scope="scope">
            <strong>{{ scope.row.name }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="最新价（元）" width="150">
          <template slot-scope="scope">
            <strong>{{ scope.row.price }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="涨跌额（元）" width="150">
          <template slot-scope="scope">
            <strong>{{ scope.row.changeamount }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="涨跌幅（%）" width="150">
          <template slot-scope="scope">
            <strong>{{ scope.row.changerate }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="加入自选交易" width="150">
          <template slot-scope="scope">
            <el-button @click="addStock(scope.row.code)">加入</el-button>
          </template>
        </el-table-column>
        <el-table-column label="预测">
          <template slot-scope="scope">
            <el-button @click="(dialog = true), predict(scope.row.code)"
              >预测</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-row>

    <el-drawer
      title="预测设置"
      :visible.sync="dialog"
      destroy-on-close="true"
      direction="rtl"
      custom-class="demo-drawer"
      ref="drawer"
      :size="size"
    >
      <div class="demo-drawer__content">
        <el-form :model="form" ref="form">
          <el-form-item label="预测方法" :label-width="formLabelWidth">
            <el-radio v-model="form.ways" label="1">GRU</el-radio>
            <el-radio v-model="form.ways" label="2">LSTM</el-radio>
          </el-form-item>

          <el-form-item label="预测天数" :label-width="formLabelWidth">
            <el-input v-model="form.days" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div class="demo-drawer__footer">
          <el-button type="primary" @click="handlePredict">确认</el-button>
          <el-button @click="handleCancel">取消</el-button>
        </div>

        <PredictChart :chart-data="this.predictdata"></PredictChart>
      </div>
    </el-drawer>
  </div>
</template>

<script>
import { Message } from "element-ui";
import Cookies from "js-cookie";
import KChart from "@/charts/KChart";
import PredictChart from "@/charts/PredictChart";
export default {
  name: "stockcard",
  components: {},
  data() {
    return {
      size:"800px",
      radio: "",
      dialog: false,
      loading: false,
      formLabelWidth: "80px",
      timer: null,
      latestdata: [],
      historydata: [],
      tableData: [],
      fieldInput: "",
      form: {
        days: "",
        ways: "",
      },
      predictcode: "",
      predictdata: [],
    };
  },
  methods: {
    handlePredict() {
      Message.success("请稍等!");
      let config = {
        headers: {
          "Content-Type": "application/json",
        },
      };

      let data = {
        type: "predict",
        ways: this.form.ways,
        days: this.form.days,
        code: this.predictcode,
      };
      this.$axios
        .post("/stocknews", data, config)
        .then((response) => {
          this.predictdata = response.data["predictdata"];
        })
        .catch((error) => {
          console.log(error);
        });
      // this.loading = false;
      // this.dialog = false;
      // this.form.days = "";
      // this.form.ways = "";
      // clearTimeout(this.timer);
    },
    handleCancel() {
      this.loading = false;
      this.dialog = false;
      this.form.days = "";
      this.form.ways = "";
      clearTimeout(this.timer);
    },
    getData() {
      this.$axios
        .get("./stocknews")
        .then((response) => {
          this.latestdata = response.data["latestdata"];
          this.historydata = response.data["kchartdata"];
          this.pushData(this.latestdata, this.historydata);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    pushData(val1, val2) {
      for (var i = 0; i < val1.length; ++i) {
        var dt = {
          code: val1[i][0],
          name: val1[i][1],
          price: val1[i][2],
          changeamount: val1[i][3],
          changerate: val1[i][4],
          chartdata: val2[i],
        };
        this.tableData.push(dt);
      }
    },
    mysearch() {
      let config = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      let data = {
        type: "search",
        data: this.fieldInput,
      };
      this.$axios
        .post("/stocknews", data, config)
        .then((response) => {
          if (response.data["auth"] === 0) {
            this.latestdata = response.data["latestdata"];
            this.historydata = response.data["kchartdata"];
            this.tableData = [];
            this.pushData(this.latestdata, this.historydata);
            console.log(this.tableData);
          } else {
            Message.error("搜索失败");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addStock(code) {
      let config = {
        headers: {
          "Content-Type": "application/json",
        },
      };

      let data = {
        type: "add",
        username: Cookies.get("username"),
        symbol: code,
      };
      this.$axios
        .post("/stocknews", data, config)
        .then((response) => {
          if (response.data["auth"] === 0) {
            Message.success("收藏成功");
          } else if (response.data["auth"] === 1) {
            Message.error("股票已收藏");
          } else {
            Message.error("收藏失败");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    predict(code) {
      this.predictcode = code;
    },
  },
  mounted: function () {
    this.getData();
  },
  components: {
    KChart,
    PredictChart,
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
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}
.demo-drawer__footer {
  width: 100%;
  position: absolute;
  bottom: 0;
  left: 0;
  border-top: 1px solid #e8e8e8;
  padding: 10px 16px;
  text-align: center;
  background-color: white;
}

@media (max-width: 1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>