<template>
  <div class="admin-container">
    <div class="admin-aside">
      head
    </div>
    <div class="admin-body">
      admin body
    </div>
  </div>
</template>

<script setup>

</script>

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
  display: flex;
  align-items: center;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  border-right: 1px solid #3d444c;
}

.admin-body {
  flex: 1;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background-color: lightseagreen;
}



</style>
