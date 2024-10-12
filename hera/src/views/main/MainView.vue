<script setup>
import MainMenu from '../../components/menus/MainMenu.vue'
</script>

<template>
  <div class="main-container">
    <div class="main-head">
      <MainMenu/>
    </div>
    <div class="main-body">
      <router-view/>
    </div>
  </div>

</template>


<style scoped>
.main-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
  box-sizing: border-box;
}

.main-head {
  height: 60px;
  background-color: #03070CFF;
  display: flex;
  align-items: center;
  margin: 0;
  padding: 0 10px;
  box-sizing: border-box;
  border-bottom: 1px solid #3d444c;
}

.main-body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: calc(100vh - 60px);
  overflow-y: scroll;
}


</style>
