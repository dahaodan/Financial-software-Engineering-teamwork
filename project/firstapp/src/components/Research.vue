<template>
  <div class="dashboard-editor-container">
    <el-row style="background: #fff; padding: 16px 16px 0; margin-bottom: 32px">
      <el-table
        :data="tableData"
        ref="singleTable"
        style="width: 100%"
        height="1000px"
        stripe
      >
        <el-table-column prop="id" label="序号" width="100"></el-table-column>
        <el-table-column prop="title" label="标题">
          <template slot-scope="scope">
            <a @click="mylink(scope.row.url)">
              <strong>{{ scope.row.title }}</strong>
            </a>
          </template>
        </el-table-column>
        <el-table-column prop="orgname" label="机构名称" width="180">
        </el-table-column>
        <el-table-column prop="date" label="日期" width="180">
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "research",
  data() {
    return {
      research: [],
      tableData: [],
    };
  },
  methods: {
    getData() {
      this.$axios
        .get("./research")
        .then((response) => {
          this.research = response.data["Research"];
          this.pushData(this.research);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    pushData(val) {
      console.log(val);
      for (var i = 0; i < val.length; ++i) {
        var dt = {
          id: val[i][0] + 1,
          title: val[i][1],
          orgname: val[i][2],
          date: val[i][3],
          url: val[i][4],
        };
        this.tableData.push(dt);
      }
    },
    mylink(val) {
      window.open(val);
    },
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
