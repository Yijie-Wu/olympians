<script setup>
import {Sunny} from "@element-plus/icons-vue";
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
</script>

<template>
  <div style="width:100%;height:100%;display: flex;flex-direction: column;">
    <div style="background-color: red;height: 60px;box-sizing: border-box;">header</div>
    <div style="flex: 1;box-sizing: border-box;">
      <el-menu
          default-active="/admin"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
      >
        <el-menu-item index="/admin">
          <el-icon><icon-menu /></el-icon>
          <span>后台首页</span>
        </el-menu-item>
        <el-sub-menu index="1">
          <template #title>
            <el-icon><location /></el-icon>
            <span>用户管理</span>
          </template>
          <el-menu-item index="1-4-1"><el-icon><location /></el-icon>item one</el-menu-item>
          <el-menu-item index="1-4-1"><el-icon><location /></el-icon>item one</el-menu-item>
        </el-sub-menu>
        <el-menu-item index="3">
          <el-icon><document /></el-icon>
          <span>Navigator Three</span>
        </el-menu-item>
        <el-menu-item index="4">
          <el-icon><setting /></el-icon>
          <span>Navigator Four</span>
        </el-menu-item>
      </el-menu>
    </div>
  </div>
</template>

<style scoped>
.menu {
  background-color: #03f2f8;
  height: 100vh;
}
</style>
