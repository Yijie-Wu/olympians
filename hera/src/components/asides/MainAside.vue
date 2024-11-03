<script setup>
import {ref} from 'vue'
import {Close, Collection, Sunny, Notebook, Lightning, Box} from "@element-plus/icons-vue";
import Logo from '../../assets/images/logo.png'

let leftMenuDrawOpen = ref(false)
</script>

<template>
  <div class="main-menu-left-button" @click="leftMenuDrawOpen = true">
    <el-icon style="font-weight: bold;">
      <font-awesome-icon :icon="['fas', 'bars']"/>
    </el-icon>
  </div>

  <el-drawer
      v-model="leftMenuDrawOpen"
      direction="ltr"
      :size="300"
      :with-header="false"
  >
    <template #default>
      <div class="aside-container">
        <div class="aside-header">
          <div class="aside-logo">
            <el-image :src="Logo" style="height: 30px;width:50px;border-radius: 8px;border: 2px solid darkorange;"/>
            <span style="margin-left: 10px;font-weight: bold;font-size: 18px;">华峰测控测试系统</span>
          </div>
          <div class="aside-action">
            <el-button circle :icon="Close" size="small" @click="leftMenuDrawOpen=false"></el-button>
          </div>
        </div>
        <div class="aside-body">
          <el-menu
              active-text-color="#ffd04b"
              class="main-aside-menu"
              :default-active="$route.path"
              router
          >
            <el-menu-item index="/" style="padding: 0;" @click="leftMenuDrawOpen=false">
              <el-icon>
                <Sunny/>
              </el-icon>
              <span>系统首页</span>
            </el-menu-item>
            <el-menu-item index="/testcase/product" style="padding: 0;" @click="leftMenuDrawOpen=false">
              <el-icon>
                <Collection/>
              </el-icon>
              <span>测试用例</span>
            </el-menu-item>
            <el-menu-item index="/bugs/dashboard" style="padding: 0;" @click="leftMenuDrawOpen=false">
              <el-icon>
                <Lightning/>
              </el-icon>
              <span>缺陷管理</span>
            </el-menu-item>
            <el-menu-item index="/resource/categories" style="padding: 0;" @click="leftMenuDrawOpen=false">
              <el-icon>
                <Box/>
              </el-icon>
              <span>资源中心</span>
            </el-menu-item>
            <el-menu-item index="/blog/categories" style="padding: 0;" @click="leftMenuDrawOpen=false">
              <el-icon>
                <Notebook/>
              </el-icon>
              <span>知识中心</span>
            </el-menu-item>
          </el-menu>

        </div>
      </div>
    </template>
    <template #footer>
      <div style="display: flex;">
        <el-button type="success" round plain style="width:100%;">当前版本: 1.0.0</el-button>
      </div>
    </template>
  </el-drawer>
</template>


<style scoped>
.aside-container {
  display: flex;
  width: 100%;
  height: 100%;
  overflow-y: scroll;
  flex-direction: column;
}

.aside-header {
  width: 100%;
  height: 50px;
  display: flex;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  border-bottom: 1px solid #3d444c;
}

.aside-logo {
  display: flex;
  flex: 1;
  height: 50px;
  margin: 0;
  padding: 0;
  align-items: center;
  box-sizing: border-box;

}

.aside-action {
  display: flex;
  width: 50px;
  height: 50px;
  align-items: center;
  justify-content: flex-end;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.main-menu-left-button {
  width: 30px;
  height: 30px;
  border: 1px solid lightgrey;
  border-radius: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-menu-left-button:hover {
  border: 1px solid #03f2f8;
  transition: 1s;
}

.aside-body {
  flex: 1;
}

.main-aside-menu {
  border: none;
}


</style>
