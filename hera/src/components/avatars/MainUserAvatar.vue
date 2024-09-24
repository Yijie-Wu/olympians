<script setup>
import {ref} from 'vue'
import {Close} from "@element-plus/icons-vue";
import Avatar from '../../assets/images/avatar.png'

const rightMenuDrawOpen = ref(false)
</script>


<template>
  <el-avatar
      :src="Avatar"
      :size="30"
      @click="rightMenuDrawOpen = true"
  />

  <el-drawer
      v-model="rightMenuDrawOpen"
      direction="rtl"
      :size="300"
      style="background-color: #0F1318FF;"
      :with-header="false"
  >
    <template #default>
      <div class="aside-container">
        <div class="aside-header">
          <div class="aside-logo">
            <el-avatar :src="Avatar" :size="45" shape="square"/>
            <div style="margin-left: 10px;">
              <div style="font-weight: bold;">yijie</div>
              <div><el-text truncated>yijie.wu@pegatestme.com</el-text></div>
            </div>
          </div>
          <div class="aside-action">
            <el-button round :icon="Close" size="small" type="success" @click="rightMenuDrawOpen=false"></el-button>
          </div>
        </div>
        <div class="aside-body">
          <div class="user-item" style="margin-top: 20px;">
            <el-icon><Close/></el-icon>设置状态
          </div>
          <div class="user-item">
            <el-icon><Close/></el-icon>我的主页
          </div>
          <div class="user-item">
            <el-icon><Close/></el-icon>我的设置
          </div>
          <div class="user-item">
            <el-icon><Close/></el-icon>后台管理
          </div>
          <div class="user-item">
            <el-icon><Close/></el-icon>登出系统
          </div>
        </div>
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
  box-sizing: border-box;
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
  width: 40px;
  height: 50px;
  align-items: flex-start;
  justify-content: flex-end;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.user-item {
  height: 36px;
  display: flex;
  padding: 0 5px;
  align-items: center;
  justify-content: flex-start;
}

.user-item:hover {
  background-color: #2b2d30;
  border-radius: 5px;
  transition: .5s;
}


</style>
