<template>
  <el-row>
    <el-col :xs="16" :sm="12" :md="16" :lg="18" :xl="20">
      <div class="main-nav-left">
        <div style="float: left;">app</div>
      </div>
    </el-col>
    <el-col :xs="8" :sm="12" :md="8" :lg="6" :xl="4">
      <div class="main-nav-right">
        <div style="float: right;">
          <MainHeaderAvatar />
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script setup>
import MainHeaderAvatar from './MainHeaderAvatar/MainHeaderAvatar.vue'

</script>

<style scoped>

.main-nav-left {
  background-color: deeppink;
  height: 60px;
}

.main-nav-right {
  background-color: orange;
  height: 60px;
}

.main-nav-right div:hover {
}
</style>
