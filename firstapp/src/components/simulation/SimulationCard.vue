<!-- 用于检验是否能实现点击页面左边,页面右侧出现相应的画面 -->
<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="请选择交易时间">
        <span :span="11"></span>
        <el-date-picker
          v-model="value1"
          type="datetimerange"
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
        >
        </el-date-picker>
      </el-form-item>

      <el-form-item label="请选择策略">
        <el-select
          v-model="form.strategy"
          clearable
          placeholder="请选择"
          @change="change"
        >
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="请设定交易成本" style="width: 350px">
        <el-input v-model="form.data" />
      </el-form-item>

      <el-form-item label="风险偏好类型">
        <el-radio-group v-model="form.type">
          <el-radio label="保守型" name="type" />
          <el-radio label="稳健型" name="type" />
          <el-radio label="平衡型" name="type" />
          <el-radio label="积极型" name="type" />
          <el-radio label="激进型" name="type" />
        </el-radio-group>
      </el-form-item>

      <el-form-item label="请选择因子库">
        <el-radio-group v-model="form.alpha">
          <el-radio label="Alpha158" name="alpha" />
          <el-radio label="Alpha360" name="alpha" />
        </el-radio-group>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">确定</el-button>
        <el-button @click="onCancel">取消</el-button>
      </el-form-item>
    </el-form>

    <el-row style="background: #fff; padding: 16px 16px 0; margin-bottom: 32px">
      <p style="font-size: 30px">
        <center>
          <strong>Report of {{ this.form.strategy }} model</strong>
        </center>
      </p>

      <p style="font-size: 20px">
        <strong>Part1: Cumulative Return & Maximum Drawdown</strong>
      </p>

      <Cumulative-return1 :chart-data="this.report_info"></Cumulative-return1>

      <Cumulative-return2 :chart-data="this.report_info"></Cumulative-return2>

      <p style="font-size: 20px"><strong>Part2: Risk Analysis</strong></p>

      <RiskAnalysis :chart-data="this.risk_info"></RiskAnalysis>

      <p style="font-size: 20px"><strong>Part3: Score_IC</strong></p>

      <ScoreIC :chart-data="this.scoreic_info"></ScoreIC>

      <p style="font-size: 20px"><strong>Part4: Model Performance</strong></p>

      <PredAutocorr :chart-data="this.pred_autocorr"></PredAutocorr>

      <Group-return :chart-data="this.group_return"></Group-return>

      <MonthlyIC :chart-data="this.monthly_ic"></MonthlyIC>
    </el-row>
  </div>
</template>

<script>
import CumulativeReturn1 from "@/charts/CumulativeReturn1";
import CumulativeReturn2 from "@/charts/CumulativeReturn2";
import RiskAnalysis from "@/charts/RiskAnalysis"
import ScoreIC from "@/charts/ScoreIC";
import GroupReturn from "@/charts/GroupReturn";
import PredAutocorr from "@/charts/PredAutocorr";
import MonthlyIC from "@/charts/MonthlyIC"
export default {
  data() {
    return {
      options: [
        {
          value: "LGBM",
          label: "LGBM",
        },
        {
          value: "Linear",
          label: "Linear",
        },
        {
          value: "MLP",
          label: "MLP",
        },
        {
          value: "GRU",
          label: "GRU",
        },
      ],
      form: {
        name: "",
        region: "",
        date1: "",
        date2: "",
        delivery: false,
        type: [],
        resource: "",
        desc: "",
        strategy: "LGBM",
      },
      report_info: [],
      risk_info: [],
      scoreic_info: [],
      group_return: [],
      pred_autocorr: [],
      monthly_ic: [],
    };
  },
  components: {
    CumulativeReturn1,
    CumulativeReturn2,
    RiskAnalysis,
    ScoreIC,
    GroupReturn,
    PredAutocorr,
    MonthlyIC,
  },
  methods: {
    change() {
      this.getSample();
    },
    onSubmit() {
      console.log(this.form.strategy);
      console.log(this.form.data);
      console.log(this.form.type);
      console.log(this.form.alpha);
      this.$message("submit!");
    },
    onCancel() {
      this.$message({
        message: "cancel!",
        type: "warning",
      });
    },
    getSample() {
      let config = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      let data = {
        type: "sample",
        strategy: this.form.strategy,
      };
      this.$axios
        .post("/simulation", data, config)
        .then((response) => {
          this.report_info = response.data["report_info"];
          this.risk_info = response.data["risk_info"];
          this.scoreic_info = response.data["scoreic_info"];
          this.group_return = response.data["group_return"];
          this.pred_autocorr = response.data["pred_autocorr"];
          this.monthly_ic = response.data["monthly_ic"]
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.getSample();
  },
};
</script>

<style scoped>
.line {
  text-align: center;
}
</style=>


