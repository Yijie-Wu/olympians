<template>
  <div class="main-layout">
    <el-container>
      <el-header>
        <MainHeader />
      </el-header>
      <el-main>
        <MainBody />
      </el-main>
      <el-footer>
        <MainFooter />
      </el-footer>
    </el-container>
  </div>
</template>

<script setup>
import MainHeader from '@/components/MainHeader/MainHeader.vue'
import MainBody from '@/components/MainBody/MainBody.vue'
import MainFooter from '@/components/MainFooter/MainFooter.vue'
</script>

<style scoped>

.main-layout {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.el-header {
  margin: 0;
  padding: 0;
}

.el-main {
  /*background-color: deeppink;*/
}

.el-footer {
  /*background-color: cadetblue;*/
}

</style>
