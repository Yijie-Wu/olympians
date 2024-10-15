<script setup>
import {House, VideoPlay, Grape,Lightning, Notebook, Box, Notification, Document, Collection,KnifeFork, DataLine, Picture} from "@element-plus/icons-vue";
</script>

<template>
  <div class="home-container">
    <div class="home-aside">
      <el-menu
          active-text-color="orange"
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
        <el-menu-item index="/home/tests">
          <el-icon>
            <Box/>
          </el-icon>
          <span>我的测试</span>
        </el-menu-item>
        <el-menu-item index="/home/testcases">
          <el-icon>
            <Grape/>
          </el-icon>
          <span>我的用例</span>
        </el-menu-item>
        <el-menu-item index="/home/bugs">
          <el-icon>
            <Lightning/>
          </el-icon>
          <span>我的缺陷</span>
        </el-menu-item>
        <el-menu-item index="/home/blogs">
          <el-icon>
            <Notebook/>
          </el-icon>
          <span>我的文章</span>
        </el-menu-item>
        <el-menu-item index="/home/videos">
          <el-icon>
            <VideoPlay/>
          </el-icon>
          <span>我的视频</span>
        </el-menu-item>
        <el-menu-item index="/home/apps">
          <el-icon>
            <Document/>
          </el-icon>
          <span>我的程序</span>
        </el-menu-item>
        <el-menu-item index="/home/books">
          <el-icon>
            <Collection/>
          </el-icon>
          <span>我的书籍</span>
        </el-menu-item>
        <el-menu-item index="/home/tools">
          <el-icon>
            <KnifeFork/>
          </el-icon>
          <span>我的工具</span>
        </el-menu-item>
        <el-menu-item index="/home/reports">
          <el-icon>
            <DataLine/>
          </el-icon>
          <span>我的报告</span>
        </el-menu-item>
        <el-menu-item index="/home/pictures">
          <el-icon>
            <Picture/>
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
  box-sizing: border-box;
}

.home-aside {
  width: 200px;
  height: calc(100vh - 60px);
  box-sizing: border-box;
  border-right: 1px solid #3d444c;
  overflow-y: scroll;
}

.home-body {
  flex: 1;
}

.custom-menu {
  border: none;
  background-color: #2b2d30;
  height: 100%;
}

.custom-menu .el-menu-item {
  padding-left: 10px !important;
  padding-right: 10px !important;
}


</style>
