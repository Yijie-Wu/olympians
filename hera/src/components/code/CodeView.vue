<script setup>
import {ref, onMounted, watch, toRef} from 'vue';

import {Codemirror} from 'vue-codemirror';
import {javascript} from '@codemirror/lang-javascript';
import {css} from '@codemirror/lang-css';
import {html} from '@codemirror/lang-html';
import {json} from '@codemirror/lang-json';
import {python} from '@codemirror/lang-python';
import {oneDark} from '@codemirror/theme-one-dark';
import {basicSetup} from 'codemirror'


const props = defineProps(['code', 'language', 'name', 'show_title', 'height']);
let extensions = [];
let mode = ref('');
let code_content = ref('');


onMounted(() => {
  code_content.value = props.code
  if (props.language === 'javascript') {
    mode.value = 'text/javascript';
    extensions = [javascript(), oneDark.basicSetup];
  } else if (props.language === 'css') {
    mode.value = 'text/css';
    extensions = [css(), oneDark, basicSetup];
  } else if (props.language === 'html') {
    mode.value = 'text/html';
    extensions = [html(), oneDark, basicSetup];
  } else if (props.language === 'python') {
    mode.value = 'text/x-python';
    extensions = [python(), oneDark, basicSetup];
  }else if (props.language === 'json') {
    mode.value = 'text/x-json';
    extensions = [json(), oneDark, basicSetup];
  }
});

const getCode = () => {
  return code_content.value
}

defineExpose({ getCode });

watch(toRef(props, 'code'), (newValue) => {
  code_content.value = newValue;
});

</script>

<template>
  <div class="code-container">
    <div class="code-header" v-if="props.show_title">
      <div class="items">
        <div class="item" style="background-color:green;"></div>
        <div class="item" style="background-color:orange;"></div>
        <div class="item" style="background-color:red;"></div>
      </div>
      <div class="code-info">
        <div>
          <el-tag type="primary" style="margin-right:10px;">{{ props.name }}</el-tag>
          <el-tag type="success">{{ props.language }}</el-tag>
        </div>
      </div>
    </div>
    <div class="code-body">
      <Codemirror
          v-model="code_content"
          :autofocus="false"
          :indent-with-tab="true"
          :tabSize="4"
          :mode="mode"
          :extensions="extensions"/>
    </div>
  </div>
</template>

<style scoped>

.code-body {
  font-family: 'Microsoft YaHei', 'SimSun', monospace; /* 确保这里也有字体设置 */
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.code-container {
  width: 100%;
  max-height: 600px;
  min-height: 40px;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background-color: #272822FF;
  border: 1px solid #454640;
  border-radius: 5px;
}

.code-header {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 36px;
  display: flex;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.76);
}

.items {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 60px;
}

.item {
  width: 12px;
  height: 12px;
  margin: 0 3px;
  padding: 0;
  box-sizing: border-box;
  border-radius: 50%;
}

.code-info {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: right;
  padding: 0 10px;
}

.code-body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.code-container {
  width: 100%;
  max-height: 600px;
  min-height: 40px;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background-color: #272822FF;
  border: 1px solid #454640;
  border-radius: 5px;
}

.code-header {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 36px;
  display: flex;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.76);
}

.items {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 60px;
}

.item {
  width: 12px;
  height: 12px;
  margin: 0 3px;
  padding: 0;
  box-sizing: border-box;
  border-radius: 50%;
}

.code-info {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: right;
  padding: 0 10px;
}

.code-body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

</style>