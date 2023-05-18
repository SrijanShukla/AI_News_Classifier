<template>
  <NavBar />
  <div style="margin-top:10%;">
    <h4>The Classification Categories are:
            1-World, 2-Sports, 3-Business, 4-Sci/Tech
        </h4>
    <h1>Enter URL</h1>
    <div>
      <input type="text" placeholder="Enter URL" v-model="this.p.URL">
      <br>
      <p>Please wait for the model to load after clicking classify. The first run may take long as the transformer is loading.</p>
    </div>
    <button @click.prevent="classify()">Classify</button>

  </div>
  <h5>History</h5>
  <div>

    <table border="3">
      <tr>
        <th style="padding: 5px;">URL</th>
        <th style="padding: 5px;">Label</th>
        <th style="padding: 5px;">Key Words</th>
      </tr>
      <tr v-for="names in this.a" :key="names">
        <td style="padding: 5px;">{{ names['url'] }}</td>
        <td style="padding: 5px;">{{ names['label'] }}</td>
        <td style="padding: 5px;">{{ names['key_words'] }}</td>
        <br>
      </tr>
    </table>
  </div>
</template>
  
<script>
import NavBar from './components/NavBar.vue'




export default {
  name: 'ViewBase',
  data() {
    return {
      p: {'URL': ""},
      a: {},
      b: {}


    }
  },

  components: {
    NavBar
  },
  methods: {
    async classify() {

      await fetch("http://127.0.0.1:5000/dashboard", {
        method: 'PUT',
        credentials: 'include',
        body: JSON.stringify(this.p),
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        }
      }).then((response) => response.json()).then(data => this.b = data).catch((error) => { console.log(error) })

      await fetch("http://127.0.0.1:5000/dashboard", {
        method: 'GET',
        credentials: 'include',
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        }
      }).then((response) => response.json()).then(data => this.a = data).catch((error) => { console.log(error) })


    }},
    async created() {
      await fetch("http://127.0.0.1:5000/dashboard", {
        method: 'GET',
        credentials: 'include',
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        }
      }).then((response) => response.json()).then(data => this.a = data).catch((error) => { console.log(error) })

      console.log(this.a)
    }
  }
</script>
<style></style>
  
  