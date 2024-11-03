<script setup>
import {ref, reactive, onMounted} from 'vue'
import {CirclePlus} from "@element-plus/icons-vue";

import BasicWangEditor from '../../../components/editor/BasicWangEditor.vue'


const title = ref('')
const value = ref('')
const value1 = ref([])
const value2 = ref(false)

const options = [
  {
    value: 'Option1',
    label: 'Option1',
  },
  {
    value: 'Option2',
    label: 'Option2',
  },
  {
    value: 'Option3',
    label: 'Option3',
  },
  {
    value: 'Option4',
    label: 'Option4',
  },
  {
    value: 'Option5',
    label: 'Option5',
  },
]

</script>

<template>
  <div class="blog-container">
    <div class="blog-body-container">
      <div class="blog-title">
        <div style="margin: 10px 0;">
          <strong style="color: red;">* </strong><strong>文章主题</strong>
        </div>
        <div style="display: flex;align-items: center;justify-content: space-between;">
          <div>
            <el-select
                v-model="value"
                placeholder="选择主题"
                size="large"
                style="width: 400px"
            >
              <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
              />
            </el-select>
          </div>
          <div style="margin-left: 6px;">
            <el-button :icon="CirclePlus" size="large" plain circle type="primary"></el-button>
          </div>
        </div>
        <div style="margin: 10px 0;">
          <strong style="color: red;">* </strong><strong>文章标签</strong>
        </div>
        <div style="width: 100%;display: flex;align-items: center;justify-content: space-between;">
          <div style="flex: 1;">
            <el-select
                v-model="value1"
                multiple
                placeholder="选择标签"
                size="large"
            >
              <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
              />
            </el-select>
          </div>
          <div style="width: 45px;display: flex;align-items: center;justify-content: flex-end;">
            <el-button :icon="CirclePlus" size="large" plain circle type="primary"></el-button>
          </div>
        </div>
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
      <div style="margin: 10px 0;">
        <el-switch
            v-model="value2"
            class="ml-2"
            inline-prompt
            style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949"
            active-text="发布"
            inactive-text="不发布"
            size="large"
        />
      </div>

      <div style="margin: 20px 0;">
        <el-button type="success" size="large" plain round style="width:100%;">保存文章</el-button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.blog-container {
  width: 1200px;
  max-width: 90%;
  margin: 10px auto;
  border: 1px solid lightgrey;
  padding: 5px;
  border-radius: 3px;
}

.blog-title {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  width: 100%;
}


</style>


