<script setup>
import MainLogo from '../../components/logos/MainLogo.vue'
import MainAside from '../../components/asides/MainAside.vue'
import MainUserAvatar from '../../components/avatars/MainUserAvatar.vue'
import {Lightning, Search, MessageBox, Plus} from "@element-plus/icons-vue";
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
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        </el-breadcrumb>
      </div>
    </div>
    <div class="main-menu-right">
      <div class="search-button-container">
        <el-icon style="font-weight: bold;">
          <Search/>
        </el-icon>
      </div>
      <el-divider direction="vertical"/>
      <div class="right-button-container">
        <el-icon style="font-weight: bold;">
          <Plus/>
        </el-icon>
      </div>
      <div>
        <el-badge class="item" type="danger" :offset="[-12, 2]" is-dot>
          <div class="right-button-container">
            <el-icon style="font-weight: bold;">
              <Lightning/>
            </el-icon>
          </div>
        </el-badge>
      </div>
      <div>
        <el-badge class="item" type="success" :offset="[-12, 2]" is-dot>
          <div class="right-button-container">
            <el-icon style="font-weight: bold;">
              <MessageBox/>
            </el-icon>
          </div>
        </el-badge>
      </div>
      <div class="main-menu-right-logo">
        <MainUserAvatar/>
      </div>
    </div>
  </div>
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
