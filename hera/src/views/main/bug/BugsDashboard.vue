<script setup>
</script>

<template>
  <el-row>
    <el-col :span="24">
      <div class="bug-board">
        kkk
      </div>
    </el-col>
  </el-row>

  <el-row style="margin-top: 10px;">
    <el-col :span="18" class="current-bugs-container">
      current bugs
    </el-col>

    <el-col :span="6" class="bugs-calc-container">
      calc
    </el-col>
  </el-row>


</template>

<style scoped>
.bug-board {
  background-color: #03f2f8;
  height: 500px;
  margin-top: 5px;
  border-radius: 5px;
  padding: 5px;
}

.current-bugs-container {
  height: 600px;
  overflow-y: scroll;
  background-color: #888888;
}

.bugs-calc-container {
  height: 600px;
  overflow-y: scroll;
  background-color: red;
}


</style>
