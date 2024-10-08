<script setup>
import {computed, ref} from "vue";
import {useRoute} from 'vue-router'

import MainLogo from '../../components/logos/MainLogo.vue'
import MainAside from '../../components/asides/MainAside.vue'
import MainUserAvatar from '../../components/avatars/MainUserAvatar.vue'
import {Lightning, Search, MessageBox, Plus} from "@element-plus/icons-vue";

const route = useRoute()
const searchDialog = ref(false)


let breadcrumbList = computed(() => {
  let uniqueTitles = new Set();
  return route.matched.map(route => {
    // 只返回有 meta.title 的路由，并且过滤重复的标题
    if (route.meta.title && !uniqueTitles.has(route.meta.title)) {
      uniqueTitles.add(route.meta.title);
      return route;
    }
    return null;
  }).filter(
      item => item !== null // 过滤掉 null 值
  )
})

</script>

<template>
  <div class="main-menu">
    <div class="main-menu-left">
      <MainAside/>
      <div class="main-menu-left-logo">
        <MainLogo/>
      </div>
      <div class="main-menu-left-breadcrumb">
        <el-breadcrumb separator="|">
          <el-breadcrumb-item
              :to="{ path: item.path }"
              :key="item.path"
              v-for="item in breadcrumbList"
          >{{ item.meta.title }}
          </el-breadcrumb-item>
        </el-breadcrumb>
      </div>
    </div>
    <div class="main-menu-right">
      <div class="search-button-container" @click="searchDialog=true">
        <el-icon style="font-weight: bold;">
          <Search/>
        </el-icon>
      </div>

      <el-divider direction="vertical"/>

      <el-dropdown trigger="click">
        <div class="right-button-container">
          <el-icon style="font-weight: bold;">
            <Plus/>
          </el-icon>
        </div>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item>新建缺陷</el-dropdown-item>
            <el-dropdown-item divided>新建测试用例</el-dropdown-item>
            <el-dropdown-item>新建测试集合</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>

      <el-dropdown trigger="click">
        <el-badge class="item" type="danger" :offset="[-12, 2]" is-dot>
          <div class="right-button-container">
            <el-icon style="font-weight: bold;">
              <Lightning/>
            </el-icon>
          </div>
        </el-badge>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item>Action 1</el-dropdown-item>
            <el-dropdown-item>Action 2</el-dropdown-item>
            <el-dropdown-item>Action 4</el-dropdown-item>
            <el-dropdown-item divided>我的所有缺陷</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>

      <el-dropdown trigger="click">
        <el-badge class="item" type="danger" :offset="[-12, 2]" is-dot>
          <div class="right-button-container">
            <el-icon style="font-weight: bold;">
              <MessageBox/>
            </el-icon>
          </div>
        </el-badge>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item>Action 1</el-dropdown-item>
            <el-dropdown-item>Action 2</el-dropdown-item>
            <el-dropdown-item>Action 4</el-dropdown-item>
            <el-dropdown-item divided>查看所有消息</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
      <div class="main-menu-right-logo">
        <MainUserAvatar/>
      </div>
    </div>
  </div>

  <el-dialog
      width="75%"
      v-model="searchDialog"
  >
    <div>
      qwertyu
    </div>
  </el-dialog>
</template>


<style scoped>

.main-menu {
  display: flex;
  width: 100%;
  height: 60px;
  align-items: center;
  justify-content: space-between;
}

.main-menu-left {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.main-menu-left-logo {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin: 0 15px;
}

.main-menu-right {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.main-menu-right-logo {
  width: 30px;
  height: 30px;
  border-radius: 50%;
}

.right-button-container {
  width: 30px;
  height: 30px;
  border: 1px solid #3d444c;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 8px;
}

.search-button-container {
  width: 30px;
  height: 30px;
  border: 1px solid #3d444c;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
