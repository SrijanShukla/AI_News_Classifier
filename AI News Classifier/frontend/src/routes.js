import {createWebHistory, createRouter} from 'vue-router'
import ViewBase from '/src/ViewBase.vue'
import Home from '/src/components/Home.vue'


const routes = [
    {
        name: 'ViewBase',
        path:'/base',
        component: ViewBase
    },
    {
        name: 'Dashboard',
        path:'/home',
        component: Home

    }
];


const router = createRouter({
    history: createWebHistory(), routes
});

export default router;