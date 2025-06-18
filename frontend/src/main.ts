import { createApp } from 'vue'
import './style.css'


// import App from './App.vue'
// createApp(App).mount('#app')

const app = createApp({});

import { HomeComponent } from "../../apps/dashboard/assets/js/app";
app.component("home-component", HomeComponent);

app.mount("#app");