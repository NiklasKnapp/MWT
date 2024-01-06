<template>
  <div id="app">
    <header>
      <h1>Vue.js Frontend</h1>
    </header>
    <main>
      <UploadFile @file-uploaded="handleFileUploaded" />
      <div v-if="selectedHeader">
        <p>Selected Header: {{ selectedHeader }}</p>
        <p>R-Squared Score: {{ rSquaredScore }}</p>
      </div>
    </main>
  </div>
</template>

<script>
import UploadFile from './components/Upload.vue';

export default {
  name: 'App',
  components: {
    UploadFile,
  },
  data() {
    return {
      selectedHeader: null,
      rSquaredScore: null,
    };
  },
  methods: {
    handleFileUploaded({ selectedHeader, rSquaredScore }) {
      this.selectedHeader = selectedHeader;
      this.rSquaredScore = rSquaredScore;
    },
  },
};
</script>

<style>
/* Your styles here */
</style>