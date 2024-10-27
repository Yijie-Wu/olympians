<script setup>
import AdminAside from '../../components/asides/AdminAside.vue'
</script>


<template>
  <div class="admin-container">
    <div class="admin-aside">
      <AdminAside/>
    </div>
    <div class="admin-body">
      <router-view/>
    </div>
  </div>
</template>

<style scoped>
.admin-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  margin: 0;
  padding: 0;
  overflow-y: scroll;
  box-sizing: border-box;
}

.admin-aside {
  height: 100vh;
  width: 240px;
  background-color: #03070CFF;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  border-right: 1px solid #3d444c;
}

.admin-body {
  flex: 1;
  margin: 0;
  padding: 5px 10px;
  box-sizing: border-box;
  height: 100vh;
  overflow-y: scroll;
}


</style>
