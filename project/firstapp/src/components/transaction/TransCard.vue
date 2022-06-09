<template>
  <div>
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
        <el-table-column label="最新价（元）" width="120">
          <template slot-scope="scope">
            <strong>{{ scope.row.price }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="涨跌额（元）" width="120">
          <template slot-scope="scope">
            <strong>{{ scope.row.changeamount }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="涨跌幅（%）" width="120">
          <template slot-scope="scope">
            <strong>{{ scope.row.changerate }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="持有量" width="150">
          <template slot-scope="scope">
            <strong>{{ scope.row.quant }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="交易" width="120">
          <template slot-scope="scope">
            <el-button @click="(dialog = true), mytrade(scope.row.code)"
              ><strong>进行交易</strong></el-button
            >
          </template>
        </el-table-column>
        <el-table-column label="取消自选">
          <template slot-scope="scope">
            <el-button @click="mydelete(scope.row.code)"
              ><strong>取消</strong></el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-row>

    <el-drawer
      title="自选交易"
      :visible.sync="dialog"
      destroy-on-close="true"
      direction="rtl"
      custom-class="demo-drawer"
      ref="drawer"
    >
      <div class="demo-drawer__content">
        <el-form :model="form" ref="form">
          <el-form-item label="请选择" :label-width="formLabelWidth">
            <el-radio v-model="form.transtype" label="1">买入</el-radio>
            <el-radio v-model="form.transtype" label="2">卖出</el-radio>
          </el-form-item>

          <el-form-item label="交易量" :label-width="formLabelWidth">
            <el-input v-model="form.transvol" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div class="demo-drawer__footer">
          <el-button type="primary" @click="handleTrade">确认</el-button>
          <el-button @click="handleCancel">取消</el-button>
        </div>
      </div>
    </el-drawer>
  </div>
</template>

<script>
import { Message } from "element-ui";
import Cookies from "js-cookie";
import KChart from "@/charts/KChart";
export default {
  name: "transcard",
  components: {},
  data() {
    return {
      radio: "",
      dialog: false,
      loading: false,
      transcode: "",
      form: {
        transtype: "",
        transvol: "",
      },
      formLabelWidth: "80px",
      timer: null,
      latestdata: [],
      historydata: [],
      tableData: [],
      quantlist: [],
      fieldInput: "",
    };
  },
  methods: {
    mytrade(code) {
      this.transcode = code;
    },
    handleTrade() {
      let config = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      let data = {
        type: "transact",
        username: Cookies.get("username"),
        money: Cookies.get("money"),
        symbol: this.transcode,
        transtype: this.form.transtype,
        transvol: this.form.transvol,
      };
      console.log(data);
      this.$axios
        .post("/transaction", data, config)
        .then((response) => {
          if (response.data["auth"] === 0) {
            Message.success("交易成功");
            Cookies.set("money", response.data["money"])
            window.location.reload();
          } else if (response.data["auth"] === 1) {
            Message.error("交易失败，交易量格式错误");
          } else if (response.data["auth"] === 2) {
            Message.error("交易失败，交易量大于持有量");
          } else if (response.data["auth"] === 3) {
            Message.error("交易失败，余额不足");
          } else {
            Message.error("取消失败");
          }
        })
        .catch((error) => {
          console.log(error);
          Message.error("交易失败");
        });
      this.loading = false;
      this.dialog = false;
      this.form.transtype = "";
      this.form.transvol = "";
      clearTimeout(this.timer);
    },
    handleCancel() {
      this.loading = false;
      this.dialog = false;
      this.form.transtype = "";
      this.form.transvol = "";
      clearTimeout(this.timer);
    },
    getData() {
      let config = {
        headers: {
          "Content-Type": "application/json",
        },
      };

      let data = {
        type: "init",
        username: Cookies.get("username"),
      };
      this.$axios
        .post("/transaction", data, config)
        .then((response) => {
          this.latestdata = response.data["latestdata"];
          this.historydata = response.data["kchartdata"];
          this.quantlist = response.data["quantlist"];
          this.pushData(this.latestdata, this.historydata, this.quantlist);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    pushData(val1, val2, val3) {
      for (var i = 0; i < val1.length; ++i) {
        var dt = {
          code: val1[i][0],
          name: val1[i][1],
          price: val1[i][2],
          changeamount: val1[i][3],
          changerate: val1[i][4],
          quant: val3[i],
          chartdata: val2[i],
        };
        this.tableData.push(dt);
      }
    },
    mydelete(code) {
      let config = {
        headers: {
          "Content-Type": "application/json",
        },
      };

      let data = {
        type: "delete",
        username: Cookies.get("username"),
        symbol: code,
      };
      this.$axios
        .post("/transaction", data, config)
        .then((response) => {
          if (response.data["auth"] === 0) {
            Message.success("取消成功");
            window.location.reload();
          } else if (response.data["auth"] === 1) {
            Message.error("取消失败，持有量大于0");
          } else {
            Message.error("取消失败");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted: function () {
    this.getData();
  },
  components: {
    KChart,
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