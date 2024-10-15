<script setup>
import {Sunny, Location, Setting} from "@element-plus/icons-vue";
import Logo from '../../assets/images/logo.png'
</script>

<template>
  <div style="width:100%;height:100%;display: flex;flex-direction: column;">
    <div class="admin-logo-container">
      <el-image :src="Logo" style="height: 30px;width:50px;border-radius: 8px;border: 2px solid darkorange;"/>
      <span style="margin-left: 10px;font-weight: bold;font-size: 18px;">华峰测控测试系统</span>
    </div>
    <div style="flex: 1;box-sizing: border-box;">
      <el-menu
          default-active="/admin"
          class="custom-menu"
          router
          unique-opened
      >
        <el-menu-item index="/admin">
          <el-icon>
            <Sunny/>
          </el-icon>
          <span>后台首页</span>
        </el-menu-item>
        <el-sub-menu index="1">
          <template #title>
            <el-icon>
              <location/>
            </el-icon>
            <span>角色管理</span>
          </template>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            item one
          </el-menu-item>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            item one
          </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="2">
          <template #title>
            <el-icon>
              <location/>
            </el-icon>
            <span>用户管理</span>
          </template>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            item one
          </el-menu-item>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            item one
          </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="3">
          <template #title>
            <el-icon>
              <location/>
            </el-icon>
            <span>测试管理</span>
          </template>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            item one
          </el-menu-item>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            item one
          </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="4">
          <template #title>
            <el-icon>
              <location/>
            </el-icon>
            <span>资源管理</span>
          </template>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            item one
          </el-menu-item>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            item one
          </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="5">
          <template #title>
            <el-icon>
              <location/>
            </el-icon>
            <span>系统管理</span>
          </template>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            item one
          </el-menu-item>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            item one
          </el-menu-item>
        </el-sub-menu>
        <el-menu-item index="b">
          <el-icon>
            <setting/>
          </el-icon>
          <span>系统设置</span>
        </el-menu-item>
      </el-menu>
    </div>
  </div>
</template>

<style scoped>
.custom-menu {
  height: calc(100vh - 60px);
  box-sizing: border-box;
  border: none;
  overflow-y: scroll;
}

.admin-logo-container {
  height: 60px;
  box-sizing: border-box;
  border-bottom: 1px solid #3d444c;
  display: flex;
  align-items: center;
  padding: 0 10px;
}


</style>
