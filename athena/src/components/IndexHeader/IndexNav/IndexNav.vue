<template>
  <div>
    <el-row>
      <el-col :span="16" class="menu-container">
        <div class="menu">
          <span>1</span>
        </div>
      </el-col>
      <el-col :span="8" class="info-container">
        <div class="info">
          <input v-model="q" type="text" class="index-search" placeholder="Search Olympians" />
          <button type="button" class="login-button">Sign In</button>
          <button type="button" class="signup-button">Sign Up</button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import {Search} from '@element-plus/icons-vue'

const q = ref('')
</script>

<style scoped>
.index-search {
  display: inline-block;
  width: 200px;
  border: 1px solid white;
  height: 30px;
  border-radius: 5px;
  outline: none;
  background: rgba(163, 200, 143, 0.2);
  color: white;
  font-weight: bold;
  margin-right: 10px;
  padding: 0 10px;
}

.index-search:focus {
  border: 1px solid dodgerblue;
}

.menu {
  float: left;
  margin: 18px 0;
}

.info {
  float: right;
  margin: 18px 0;
}

.login-button {
  background: rgba(255, 255, 255, 0);
  color: white;
  font-weight: bold;
  padding: 5px;
  border: none;
  outline: none;
}

.login-button:hover {
  color: gray;
}


.signup-button {
  background: rgba(255, 255, 255, 0);
  color: white;
  font-weight: bold;
  padding: 5px 10px;
  border: 1px solid white;
  border-radius: 5px;
  margin-left: 10px;
}

.signup-button:hover {
  color: grey;
  border: 1px solid dodgerblue;
}


</style>
