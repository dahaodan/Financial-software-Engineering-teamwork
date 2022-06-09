<template>
  <el-table :data="list" style="width: 100%; padding-top: 15px">
    <!-- <el-table-column label="Order_No" width="135">
      <template slot-scope="scope">
        {{ scope.row.order_no | orderNoFilter }}
      </template>
      1
    </el-table-column> -->

    <el-table-column label="Stock_No" width="250" align="left">
      <!-- <template slot-scope="scope">
        ¥{{ scope.row.price | toThousandFilter }}
      </template> -->
      60036
    </el-table-column>

        <el-table-column label="Stock_Name" width="230" align="center">
      <!-- <template slot-scope="scope">
        ¥{{ scope.row.price | toThousandFilter }}
      </template> -->
      test股票
    </el-table-column>

    <el-table-column label="BuyPrice" width="250" align="center">
      ¥39.3
    </el-table-column>

    <!-- <el-table-column label="SellPrice" width="220" align="center">
      ¥45.6
    </el-table-column> -->

    <el-table-column label="Volume" width="250" align="center">
      <!-- <template slot-scope="scope">
        ¥{{ scope.row.price | toThousandFilter }}
      </template> -->
      100
    </el-table-column>

    <el-table-column label="Status" width="250" align="center">
      <!-- <template slot-scope="{row}">
        <el-tag :type="row.status | statusFilter">
          {{ row.status }}
        </el-tag>
      </template> -->
      <el-tag type="success"> success </el-tag>
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  //   filters: {
  //     statusFilter(status) {s
  //       const statusMap = {
  //         success: 'success',
  //         pending: 'danger'
  //       }
  //       return statusMap[status]
  //     },
  //     orderNoFilter(str) {
  //       return str.substring(0, 30)
  //     }
  //   },
  data() {
    return {
      list: [1],
    };
  },
  //   created() {
  //     this.fetchData()
  //   },
  //   methods: {
  //     fetchData() {
  //       transactionList().then(response => {
  //         this.list = response.data.items.slice(0, 8)
  //       })
  //     }
  //   }
};
</script>

<style lang="scss" scoped>
</style>