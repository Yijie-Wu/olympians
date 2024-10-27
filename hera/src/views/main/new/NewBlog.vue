<script setup>
import {ref, reactive, onMounted} from 'vue'

import BasicWangEditor from '../../../components/editor/BasicWangEditor.vue'


const title = ref('')


</script>

<template>
  <div class="blog-container">
    <div class="blog-body-container">
      <div class="blog-title">
        <div style="margin: 10px 0;">
          <strong style="color: red;">* </strong><strong>文章标题</strong>
        </div>
        <el-input v-model="title" placeholder="请输入文章标题" size="large"/>
      </div>
      <div class="blog-body">
        <div style="margin: 10px 0;">
          <strong style="color: red;">* </strong><strong>文章正文</strong>
        </div>
        <BasicWangEditor/>
      </div>
    </div>

    <div class="blog-items-container">
      items
    </div>
  </div>
</template>

<style scoped>
.blog-container {
  width: 1200px;
  max-width: 90%;
  margin: 0 auto;
}

.blog-title {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  width: 100%;
}


</style>


