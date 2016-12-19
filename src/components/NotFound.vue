<template>
  <div class="centerstuff-container">
    <div class="centerstuff">
        <div>
            <h1>404</h1>
            <p>Requested page was not found.</p>
            <router-link :to="{name: 'index'}">Go back</router-link>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'notFound',
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
.centerstuff-container {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
}
.centerstuff {
    background-color: rgb(192, 57, 43);
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
}
h1 {
    font-size: 80px;
    color: white;
    text-align: center;
}
p {
    color: white;
    font-size: 20px;
    width: 400px;
    text-align: center;
}
a {
    color: rgb(236, 240, 241);
    font-size: 30px;
    text-align: center;
    padding-top: 20px;
    display: block;
}
</style>
