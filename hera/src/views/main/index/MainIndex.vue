<script setup>
import MainIndexFooter from '../../../components/footers/MainIndexFooter.vue'
</script>

<template>
  <div style="padding: 0 10px;">
    <el-row :gutter="10">
      <el-col :span="24">
        <div class="carousel-container">
          hhaha
        </div>
      </el-col>
    </el-row>

    <el-row :gutter="10" style="margin-top: 10px;margin-bottom: 10px;">
      <el-col :span="6">
        <el-card shadow="hover" style="height: 200px;">
          qwer
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" style="height: 200px;">
          qwer
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" style="height: 200px;">
          qwer
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" style="height: 200px;">
          qwer
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="10" style="margin-top: 10px;margin-bottom: 10px;height: 800px;">

    </el-row>

    <MainIndexFooter/>
  </div>
</template>

<style scoped>
.carousel-container {
  height: 600px;
  margin-top: 5px;
  border: 1px solid lightgrey;
  border-radius: 3px;
}
</style>
