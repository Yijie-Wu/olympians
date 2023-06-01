<template>
  <div class="index-nav-body">
    <div class="ufo-container">
      <div class="ufo">
        <img src="@/assets/image/hero-drone.webp" alt="">
      </div>
    </div>
    <div class="index-dash-container">
      <div class="index-dash">

      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.index-nav-body {
  height: 700px;
  margin-top: 50px;
  /*border: 2px solid orangered;*/
  background: url("@/assets/image/lines-hero.svg");
  background-repeat: no-repeat;
}

.ufo-container {
  /*border: 1px solid pink;*/
  height: 280px;
}

.ufo {
  height: 280px;
  width: 430px;
  /*border: 1px solid blue;*/
  float: right;
}

.ufo img {
  height: 70%;
  width: 70%;
  float: right;
}

.index-dash-container {
  height: 160px;
  /*border: 1px solid seagreen;*/
}

.index-dash {
  float: left;
  height: 80px;
  width: 400px;
  border-radius: 40px;
  margin-left: 80px;
  margin-top: 40px;
  border: 1px solid rgba(148, 191, 173, 0.38);

}


</style>
