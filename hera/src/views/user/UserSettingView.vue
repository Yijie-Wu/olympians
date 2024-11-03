<script setup>
import {PictureRounded, Key, Notebook, Box, Postcard} from "@element-plus/icons-vue";
</script>

<template>
  <div class="home-container">
    <div class="home-aside">
      <el-menu
          active-text-color="#ffd04b"
          class="custom-menu"
          :default-active="$route.path"
          router
      >
        <el-menu-item index="/user/settings/profile">
          <el-icon>
            <Postcard/>
          </el-icon>
          <span>基本设置</span>
        </el-menu-item>
        <el-menu-item index="/user/settings/change-avatar">
          <el-icon>
            <PictureRounded/>
          </el-icon>
          <span>修改头像</span>
        </el-menu-item>
        <el-menu-item index="/user/settings/change-password">
          <el-icon>
            <Key/>
          </el-icon>
          <span>修改密码</span>
        </el-menu-item>
        <el-menu-item index="/user/settings/tokens">
          <el-icon>
            <Box/>
          </el-icon>
          <span>令牌管理</span>
        </el-menu-item>
        <el-menu-item index="/user/settings/test-settings">
          <el-icon>
            <Notebook/>
          </el-icon>
          <span>测试设置</span>
        </el-menu-item>
      </el-menu>
    </div>
    <div class="home-body">
      <router-view/>
    </div>
  </div>

</template>


<style scoped>
.home-container {
  display: flex;
}

.home-aside {
  width: 180px;
  height: calc(100vh - 62px);
  box-sizing: border-box;
  border-right: 1px solid lightgrey;
}

.home-body {
  flex: 1;
}

.custom-menu {
  border: none;
  height: 100%;
}

.custom-menu .el-menu-item {
  padding-left: 10px !important;
  padding-right: 10px !important;
}


</style>
