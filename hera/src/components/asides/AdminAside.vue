<script setup>
import {Sunny, Location, Setting, CirclePlus, Postcard, User, Tickets, Link, List} from "@element-plus/icons-vue";
import Logo from '../../assets/images/logo.png'
</script>

<template>
  <div style="width:100%;height:100%;display: flex;flex-direction: column;">
    <div class="admin-logo-container">
      <el-image :src="Logo" style="height: 30px;width:50px;border-radius: 8px;border: 2px solid darkorange;"/>
      <span style="margin-left: 10px;font-weight: bold;font-size: 18px;" @click="$router.push('/')">华峰测控测试系统</span>
    </div>
    <div style="flex: 1;box-sizing: border-box;">
      <el-menu
          :default-active="$route.path"
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
        <el-sub-menu index="role">
          <template #title>
            <el-icon>
              <Postcard/>
            </el-icon>
            <span>角色管理</span>
          </template>
          <el-menu-item index="/admin/roles/list">
            <el-icon>
              <Tickets/>
            </el-icon>
            系统角色列表
          </el-menu-item>
          <el-menu-item index="/admin/system-roles/list">
            <el-icon>
              <Tickets/>
            </el-icon>
            工作角色列表
          </el-menu-item>
          <el-menu-item index="/admin/system-roles/add">
            <el-icon>
              <CirclePlus/>
            </el-icon>
            新增工作角色
          </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="user">
          <template #title>
            <el-icon>
              <User/>
            </el-icon>
            <span>用户管理</span>
          </template>
          <el-menu-item index="/admin/users">
            <el-icon>
              <Tickets/>
            </el-icon>
            用户列表
          </el-menu-item>
          <el-menu-item index="/admin/users/add">
            <el-icon>
              <CirclePlus/>
            </el-icon>
            新增用户
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
            测试用例管理
          </el-menu-item>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            测试小组管理
          </el-menu-item>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            测试报告管理
          </el-menu-item>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            测试日志管理
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
            系统文档管理
          </el-menu-item>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            系统视频管理
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
            封页图片管理
          </el-menu-item>
          <el-menu-item index="1-4-1">
            <el-icon>
              <location/>
            </el-icon>
            系统链接管理
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
