<template>


        <h2>AI News Classifier</h2>
<div><h3>Instructions</h3>
<p>Hi! Go to the dashboard and paste the news url you wish classify and your result will be printed</p></div>
        <br><br><br><br><br><br><br><br><br><br>
        <h3>The Classification Categories are:
            1-World, 2-Sports, 3-Business, 4-Sci/Tech
        </h3><br><br><br><br><br><br><br><br><br><button @click="gotodsh()">GO TO DASHBOARD</button><br><br><br><br>
        <p>note: the first run of the application may take some time as it loads the transformer to the cache memory</p>

</template>

<script>



export default {
    name: 'Home',
    props: {},
    data() {
        return {
            
            a: { "name": '' },


        }
    },
    methods: {
        gotodsh() {
            window.location = ('/base')
        }
        
    }

}

</script>

<style scoped>
.Head {
  
    font-size: 150px;
    color: black;
}
</style>