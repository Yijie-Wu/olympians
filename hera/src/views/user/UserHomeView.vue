<script setup>
import {House, Collection, Lightning, Notebook, Box, Notification} from "@element-plus/icons-vue";
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
        <el-menu-item index="/home/index" style="padding: 0;">
          <el-icon>
            <House/>
          </el-icon>
          <span>我的主页</span>
        </el-menu-item>
        <el-menu-item index="/home/notifications" style="padding: 0;">
          <el-icon>
            <Notification/>
          </el-icon>
          <span>我的通知</span>
        </el-menu-item>
        <el-menu-item index="resources" style="padding: 0;">
          <el-icon>
            <Lightning/>
          </el-icon>
          <span>我的资源</span>
        </el-menu-item>
        <el-menu-item index="tests" style="padding: 0;">
          <el-icon>
            <Box/>
          </el-icon>
          <span>我的测试</span>
        </el-menu-item>
        <el-menu-item index="blogs" style="padding: 0;">
          <el-icon>
            <Notebook/>
          </el-icon>
          <span>我的文章</span>
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
