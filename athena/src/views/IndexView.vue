<template>
  <div class="main-layout">
    <el-container>
      <el-header>
        <IndexHeader />
      </el-header>
      <el-main>
        <IndexBody />
      </el-main>
      <el-footer>
        <IndexFooter />
      </el-footer>
    </el-container>
  </div>
</template>

<script setup>
import IndexHeader from '@/components/IndexHeader/IndexHeader.vue'
import IndexBody from '@/components/IndexBody/IndexBody.vue'
import IndexFooter from '@/components/IndexFooter/IndexFooter.vue'
</script>

<style scoped>

.main-layout {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}


.el-header {
  background: url("@/assets/image/hero-bg.webp");
  margin: 0;
  padding: 0;
  height: 800px;
  background-repeat: no-repeat;
  background-position-x: -1950px;
}

.el-main {
  /*background-color: deeppink;*/
}

.el-footer {
  /*background-color: cadetblue;*/
}

</style>
