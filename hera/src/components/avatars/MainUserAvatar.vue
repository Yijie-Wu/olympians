<script setup>
import {ref, onMounted, computed} from 'vue'
import {useRouter} from 'vue-router'
import {Close, Service, House, Setting, SwitchButton, DataBoard} from "@element-plus/icons-vue";
import {removeToken} from "../../utils/token.js";
import {showMessage} from "../../utils/message.js";
import {useUserStore} from "../../stores/user/user.js";
import {get_userinfo} from "../../apis/user.js";
import {calcAvatar} from "../../utils/common.js";

let user_store = useUserStore()
let route = useRouter()
let rightMenuDrawOpen = ref(false)


onMounted(async () => {
  await get_userinfo().then((res) => {
    user_store.setUserInfo(res.data);
  });
});

const avatar_url = computed(() => {
  if (user_store.userInfo.avatar === undefined) {
    return calcAvatar();
  } else {
    return calcAvatar(user_store.userInfo.avatar);
  }
});


function logout() {
  removeToken();
  user_store.setUserInfo({});
  user_store.isLogin = false;
  showMessage('success', '登出成功');
  route.push('/auth/login');
}


function goTo(path) {
  route.push(path);
}

</script>


<template>
  <el-badge class="item" type="success" :offset="[-5, 2]" is-dot>
    <el-avatar
        :src="avatar_url"
        :size="30"
        @click="rightMenuDrawOpen = true"
        class="avatar-logo"
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
            <el-avatar :src="avatar_url" :size="45" shape="square"/>
            <div style="margin-left: 10px;">
              <div style="font-weight: bold;">{{ user_store.userInfo.username }}</div>
              <div style="width:180px;">
                <el-text truncated size="small">{{ user_store.userInfo.email }}</el-text>
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
                <el-icon>
                  <Service/>
                </el-icon>
                <span class="ml-1">设置状态</span>
              </div>
              <div>
                <el-button size="small" round type="success">{{user_store.userInfo.status}}</el-button>
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
          <div class="user-item" v-if="user_store.userInfo.role === '超级管理员'" @click="goTo('/admin')">
            <el-icon>
              <DataBoard/>
            </el-icon>
            <span class="ml-1">后台管理</span>
          </div>
          <div class="user-item" @click="logout()">
            <el-icon>
              <SwitchButton/>
            </el-icon>
            <span class="ml-1">登出系统</span>
          </div>

          <div>
            {{user_store.userInfo}}
          </div>
        </div>
      </div>
    </template>
  </el-drawer>
</template>


<style scoped>
.avatar-logo {
  border: 2px solid lightseagreen;
  box-sizing: border-box;
}

.avatar-logo:hover {
  border: 2px solid darkorange;
  transition: 1s;
}


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
