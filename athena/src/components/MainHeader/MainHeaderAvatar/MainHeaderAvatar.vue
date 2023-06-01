<template>
  <el-dropdown trigger="click">
      <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"/>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item>SignIn As: Yijie, Wu</el-dropdown-item>
        <el-dropdown-item divided>
          <el-button @click="visible = true" :icon="Headset" style="width: 100%;">Set Status</el-button>
        </el-dropdown-item>
        <el-dropdown-item divided><el-icon><Aim /></el-icon> Your Bug</el-dropdown-item>
        <el-dropdown-item><el-icon><Notebook /></el-icon> Your Note</el-dropdown-item>
        <el-dropdown-item><el-icon><Tickets /></el-icon> Your Testcase</el-dropdown-item>
        <el-dropdown-item><el-icon><Folder /></el-icon> Your Testsuite</el-dropdown-item>
        <el-dropdown-item><el-icon><Ship /></el-icon> Your Test Runner</el-dropdown-item>
        <el-dropdown-item><el-icon><OfficeBuilding /></el-icon> Your Team</el-dropdown-item>
        <el-dropdown-item divided><el-icon><User /></el-icon> Profile</el-dropdown-item>
        <el-dropdown-item><el-icon><Setting /></el-icon> Settings</el-dropdown-item>
        <el-dropdown-item divided><el-icon><SwitchButton /></el-icon> Logout</el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
  <el-dialog v-model="visible" :show-close="false" width="60%" :modal="true">
    This is dialog content.

    <el-button @click="visible = false">Cancel</el-button>
    <el-button type="primary" @click="visible = false">
      Confirm
    </el-button>

  </el-dialog>
</template>

<script setup>
import { ref } from 'vue'
import { ElButton, ElDialog } from 'element-plus'
import { Headset, User, SwitchButton, Setting, Notebook, Folder, Ship, Aim, Tickets, OfficeBuilding} from '@element-plus/icons-vue'

const visible = ref(false)
</script>

<style scoped>
.my-header {
  margin: 0;
  padding: 0;
  height: 40px;
  background-color: orange;
}
</style>
