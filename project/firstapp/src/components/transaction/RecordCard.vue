<template>
  <div>
    <el-row style="background: #fff; padding: 16px 16px 0; margin-bottom: 32px">
      <el-table :data="tableData" ref="singleTable" style="width: 100%" stripe>
        <el-table-column label="股票代码" min-width="300">
          <template slot-scope="scope">
            <strong>{{ scope.row.code }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="股票名称" width="300">
          <template slot-scope="scope">
            <strong>{{ scope.row.name }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="交易类型" width="300">
          <template slot-scope="scope">
            <strong>{{ scope.row.type }}</strong>
          </template>
        </el-table-column>
        <el-table-column label="交易量">
          <template slot-scope="scope">
            <strong>{{ scope.row.vol }}</strong>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
import { Message } from "element-ui";
import Cookies from "js-cookie";
export default {
  name: "recordcard",
  data() {
    return {
      name: [],
      code: [],
      recordData: [],
      tableData: [],
    };
  },
  methods: {
    getData() {
      let config = {
        headers: {
          "Content-Type": "application/json",
        },
      };

      let data = {
        type: "record",
        username: Cookies.get("username"),
      };
      this.$axios
        .post("/transaction", data, config)
        .then((response) => {
          this.code = response.data["code"]
          this.name = response.data["name"];
          this.recordData = response.data["data"];
          this.pushData(this.code, this.name, this.recordData);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    pushData(val1, val2, val3) {
      for (var i = 0; i < val1.length; ++i) {
        var dt = {
          code: val1[i],
          name: val2[i],
          type: val3[i][3],
          vol: val3[i][2],
        };
        this.tableData.push(dt);
      }
    },
  },
  mounted() {
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