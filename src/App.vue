<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  components: {},
};
</script>

<style lang="scss">
  @import '../node_modules/bootstrap-sass/assets/stylesheets/_bootstrap-sprockets';
  @import '../node_modules/bootstrap-sass/assets/stylesheets/_bootstrap';

  html, body, body > div {
    min-height: 100%;
  }
</style>
