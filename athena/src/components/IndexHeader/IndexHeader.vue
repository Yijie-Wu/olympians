<template>
<div class="index-header">
  <IndexNav></IndexNav>
  <IndexHeaderBody></IndexHeaderBody>
</div>
</template>

<script setup>
import IndexNav from './IndexNav/IndexNav.vue'
import IndexHeaderBody from './IndexHeaderBody/IndexHeaderBody'

</script>

<style scoped>
.index-header {
  margin: auto;
  height: 60px;
}

@media screen and (min-width: 1300px) {
  .index-header {
    width: 1200px;
  }
}
</style>
