<script setup>
import {House, Collection, Lightning, Notebook, Box, Notification} from "@element-plus/icons-vue";
</script>

<template>
  <div class="home-container">
    <div class="home-aside">
      <el-menu
          active-text-color="#ffd04b"
          class="custom-menu"
          default-active="/home/index"
          text-color="#fff"
          router
      >
        <el-menu-item index="/home/index">
          <el-icon>
            <House/>
          </el-icon>
          <span>我的主页</span>
        </el-menu-item>
        <el-menu-item index="/home/notifications">
          <el-icon>
            <Notification/>
          </el-icon>
          <span>我的通知</span>
        </el-menu-item>
        <el-menu-item index="tests">
          <el-icon>
            <Box/>
          </el-icon>
          <span>我的测试</span>
        </el-menu-item>
        <el-menu-item index="blogs">
          <el-icon>
            <Notebook/>
          </el-icon>
          <span>我的文章</span>
        </el-menu-item>
        <el-menu-item index="videos">
          <el-icon>
            <Lightning/>
          </el-icon>
          <span>我的视频</span>
        </el-menu-item>
        <el-menu-item index="apps">
          <el-icon>
            <Lightning/>
          </el-icon>
          <span>我的程序</span>
        </el-menu-item>
        <el-menu-item index="books">
          <el-icon>
            <Lightning/>
          </el-icon>
          <span>我的书籍</span>
        </el-menu-item>
        <el-menu-item index="tools">
          <el-icon>
            <Lightning/>
          </el-icon>
          <span>我的工具</span>
        </el-menu-item>
        <el-menu-item index="reports">
          <el-icon>
            <Lightning/>
          </el-icon>
          <span>我的报告</span>
        </el-menu-item>
        <el-menu-item index="pictures">
          <el-icon>
            <Lightning/>
          </el-icon>
          <span>我的图片</span>
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
  width: 150px;
  height: calc(100vh - 62px);
  box-sizing: border-box;
  border-right: 1px solid #3d444c;
  overflow-y: scroll;
}

.home-body {
  flex: 1;
}

.custom-menu {
  padding-left: 0 !important;
  padding-right: 0 !important;
  border: none;
}

.custom-menu .el-menu-item {
  padding-left: 0 !important;
  padding-right: 0 !important;
  margin-right: 8px;
}


</style>
