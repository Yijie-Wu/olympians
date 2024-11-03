<script setup>
import {ref, onBeforeUnmount, reactive} from 'vue';
import {Key, Lock, Message} from '@element-plus/icons-vue'
import {useUserStore} from "../../stores/user/user.js";
import {setToken} from "../../utils/token.js";
import {showMessage} from "../../utils/message.js";
import {useRouter} from 'vue-router'
import {login_by_basic_auth} from "../../apis/auth.js";

import AuthImage1 from '../../assets/images/auth1.jpeg'
import AuthImage2 from '../../assets/images/auth2.jpeg'
import AuthImage3 from '../../assets/images/auth3.jpg'
import AuthImage4 from '../../assets/images/auth4.jpeg'

const authImages = [
  AuthImage1,
  AuthImage2,
  AuthImage3,
  AuthImage4
]

const formRef = ref(null)
const loading = ref(false)
const auth_message = ref('用户名密码登陆')
const store = useUserStore()
const router = useRouter()
const auth_type = ref(false)
const windowHeight = window.innerHeight + 'px'

const switch_auth_type = (() => {
  if (auth_type.value === true) {
    auth_message.value = 'LDAP 账号登录'
  } else {
    auth_message.value = '用户名密码登陆'
  }
})


const form = reactive({
  username: '',
  password: ''
})

const rules = reactive({
      username: [
        {required: true, message: '用户名不能为空', trigger: 'blur'},
        {min: 2, max: 20, message: '用户名长度必须在2到20之间', trigger: 'blur'},
      ],
      email: [
        {required: true, message: '邮箱不能为空', trigger: 'blur'},
        {min: 15, max: 50, message: '邮箱长度必须在15到50之间', trigger: 'blur'},
      ],
      password: [
        {required: true, message: '密码不能为空', trigger: 'blur'},
        {min: 6, max: 20, message: '密码长度必须在6到20之间', trigger: 'blur'},
      ],
      password2: [
        {required: true, message: '密码不能为空', trigger: 'blur'},
        {min: 6, max: 20, message: '密码长度必须在6到20之间', trigger: 'blur'}
      ]
    }
)


const loginByBasicAuth = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    loading.value = true
    auth_message.value = '登录中...'
    login_by_basic_auth(form).then(res => {
      setToken(res.data.token);
      store.setIsLogin(true);
      router.push({path: '/'})
      showMessage('success', '登录成功')
    }).catch(err => {
      showMessage('error', err.message)
    }).finally(() => {
      loading.value = false
      auth_message.value = '用户名密码登陆'
    })
  })
}


function onKeyUp(e) {
  if (e.key === "Enter") loginByBasicAuth(formRef.value)
}

onBeforeUnmount(() => {
  document.removeEventListener("keyup", onKeyUp)
})

</script>

<template>
  <el-row class="main-container">
    <el-col :xs="0" :sm="0" :md="10" :lg="9" :xl="9">
      <div>
        <el-carousel :height="windowHeight" arrow="never">
          <el-carousel-item v-for="image in authImages" :key="image">
            <div style="width: 100%;height: 100%;display: flex;align-items: center;justify-content: center;">
              <el-image :src="image" style="width: 100%;height: 100%;"></el-image>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
    </el-col>
    <el-col :xs="24" :sm="24" :md="14" :lg="15" :xl="15" class="auth-container">
      <div class="auth-box">
        <div class="auth-header">
          <div class="logo-image">
            <img src="@/assets/images/logo.png" alt="logo"/>
          </div>
          <div class="auth-title">华峰测控测试管理平台</div>
        </div>

        <div class="form-area">
          <el-form ref="formRef" :model="form" :rules="rules">
            <el-form-item prop="email">
              <el-input
                  v-model="form.email"
                  placeholder="输入邮箱"
                  :prefix-icon="Message"
                  size="large"
              />
            </el-form-item>
            <el-row :gutter="10">
              <el-col :span="18">
                <el-form-item prop="email">
                  <el-input
                      v-model="form.email"
                      placeholder="输入验证码"
                      :prefix-icon="Key"
                      size="large"
                  />
                </el-form-item>
              </el-col>
              <el-col :span="6">
                <el-button type="primary" plain size="large" style="width: 100%;">获取验证码</el-button>
              </el-col>
            </el-row>
            <el-form-item prop="password">
              <el-input
                  v-model="form.password"
                  placeholder="输入新密码"
                  :prefix-icon="Lock"
                  size="large"
                  type="password"
                  show-password
              />
            </el-form-item>
            <el-form-item prop="password2">
              <el-input
                  v-model="form.password2"
                  placeholder="确认新密码"
                  :prefix-icon="Lock"
                  size="large"
                  type="password"
                  show-password
              />
            </el-form-item>
            <el-form-item>
              <el-button
                  type="success"
                  size="large"
                  style="width:100%;"
                  @click="loginByBasicAuth(formRef)"
                  :loading="loading">修改密码
              </el-button>
            </el-form-item>
          </el-form>
        </div>
        <div class="auth-footer-container">
          <div>
            <span>没有账号?</span>
            <strong style="color: cadetblue;" @click="$router.push('/auth/register')"> 注册一个</strong>
          </div>
          <div>
            <div>
              已有账户? <strong style="color: cadetblue;" @click="$router.push('/auth/login')">前往登陆</strong>
            </div>
          </div>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<style scoped>
.main-container {
  height: 100vh;
  width: 100vw;
  box-sizing: border-box;
}

.logo-image {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 10px;
}

.logo-image img {
  width: 300px;
}

.auth-title {
  font-size: 30px;
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
}


.auth-container {
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
}

.form-area {
  margin-top: 30px;
  margin-bottom: 10px;
}


.auth-box {
  color: #3d444c;
  width: 600px;
  height: 560px;
  border-radius: 10px;
  max-width: 90%;
  background-color: white;
  padding: 10px 20px;
  border: 1px solid lightgrey;
}

.auth-footer-container {
  display: flex;
  height: 50px;
  align-items: center;
  margin-top: 20px;
  justify-content: space-between;
}


</style>
