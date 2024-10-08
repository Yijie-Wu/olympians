<script setup>
import {ref} from 'vue'
import {useRouter} from 'vue-router'
import {Close, Service, House, Setting, SwitchButton, DataBoard} from "@element-plus/icons-vue";
import Avatar from '../../assets/images/avatar.png'

let route = useRouter()
let rightMenuDrawOpen = ref(false)


function goTo(path) {
  route.push(path);
}

</script>


<template>
  <el-badge class="item" type="success" :offset="[-5, 2]" is-dot>
    <el-avatar
        :src="Avatar"
        :size="30"
        @click="rightMenuDrawOpen = true"
    />
  </el-badge>

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
              <div>
                <el-text truncated size="small">yijie.wu@pegatestme.com</el-text>
              </div>
            </div>
          </div>
          <div class="aside-action">
            <el-button circle plain :icon="Close" size="small" type="success"
                       @click="rightMenuDrawOpen=false"></el-button>
          </div>
        </div>
        <div class="aside-body">
          <div class="user-item" style="margin-top: 20px;">
            <div style="display:flex;align-items: center;justify-content: space-between;width: 100%;">
              <div>
                <el-icon><Service/></el-icon><span class="ml-1">设置状态</span>
              </div>
              <div>
                <el-button size="small" round type="success">在线</el-button>
              </div>
            </div>
          </div>
          <div class="user-item" @click="goTo('/home/index');rightMenuDrawOpen=false">
            <el-icon>
              <House/>
            </el-icon>
            <span class="ml-1">我的主页</span>
          </div>
          <div class="user-item" @click="goTo('/user/settings/profile');rightMenuDrawOpen=false">
            <el-icon>
              <Setting/>
            </el-icon>
            <span class="ml-1">我的设置</span>
          </div>
          <div class="user-item">
            <el-icon>
              <DataBoard/>
            </el-icon>
            <span class="ml-1" @click="goTo('/admin')">后台管理</span>
          </div>
          <div class="user-item">
            <el-icon>
              <SwitchButton/>
            </el-icon>
            <span class="ml-1" @click="rightMenuDrawOpen=false">登出系统</span>
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
  margin-top: 5px;
  align-items: center;
  justify-content: flex-start;
}

.user-item:hover {
  background-color: #2b2d30;
  border-radius: 5px;
  transition: .5s;
}

.ml-1 {
  margin-left: 5px;
}

</style>
