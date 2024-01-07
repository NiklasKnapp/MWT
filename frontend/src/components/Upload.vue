<template>
  <div>
    <input type="file" ref="fileInput" @change="onFileChange" />
    <button @click="uploadFile">Upload</button>
    <select v-model="selectedHeader">
      <option v-for="header in headers" :key="header">{{ header }}</option>
    </select>
    <button @click="getHeaders">Get Headers</button>
    <button @click="trainModel">Train Model</button>
    <div v-if="rSquared !== null">
      R-squared Score: {{ rSquared }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      file: null,
      headers: [],
      selectedHeader: null,
      rSquared: null,
    };
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0];
    },
    uploadFile() {
      const formData = new FormData();
      formData.append('file', this.file);

      axios.post('https://mwt_backend_1:5000/upload', formData)
        .then(response => {
          // Handle the response from the server
          console.log(response.data);
        })
        .catch(error => {
          // Handle errors
          console.error('Error uploading file:', error);
        });
    },
    getHeaders() {
      console.log('Headers:');
      axios.get('https://mwt_backend_1:5000/headers')
        .then(response => {
          // Handle the response from the server
          console.log("Response: ");
          console.log(response.data);
        })
        .catch(error => {
          // Handle errors
          console.error('Error retrieving headers:', error);
        });
      },
    trainModel() {
      axios.get('https://mwt_backend_1:5000/headers')
        .then(response => {
          // Handle the response from the server
          console.log("Response: ");
          console.log(response.data);
        })
        .catch(error => {
          // Handle errors
          console.error('Error retrieving headers:', error);
        });
    },
  },
};
</script>