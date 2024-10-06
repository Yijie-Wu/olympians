<script setup>
import {PictureRounded, Key, Lightning, Notebook, Box, Postcard} from "@element-plus/icons-vue";
</script>

<template>
  <div class="home-container">
    <div class="home-aside">
      <el-menu
          active-text-color="#ffd04b"
          class="main-aside-menu"
          default-active="/"
          text-color="#fff"
          router
      >
        <el-menu-item index="/" style="padding: 0;">
          <el-icon>
            <Postcard/>
          </el-icon>
          <span>基本设置</span>
        </el-menu-item>
        <el-menu-item index="/testcase/product" style="padding: 0;">
          <el-icon>
            <PictureRounded/>
          </el-icon>
          <span>修改头像</span>
        </el-menu-item>
        <el-menu-item index="/bugs/dashboard" style="padding: 0;">
          <el-icon>
            <Key/>
          </el-icon>
          <span>修改密码</span>
        </el-menu-item>
        <el-menu-item index="/resource/categories" style="padding: 0;">
          <el-icon>
            <Box/>
          </el-icon>
          <span>令牌管理</span>
        </el-menu-item>
        <el-menu-item index="/blog/categories" style="padding: 0;">
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
  border-right: 1px solid #3d444c;
}

.home-body {
  flex: 1;
}

.main-aside-menu {
  border: none;
}


</style>
