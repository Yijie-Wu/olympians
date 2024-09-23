import {createApp} from 'vue';
import './style.css';
import App from './App.vue';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import 'element-plus/theme-chalk/display.css';
import 'element-plus/theme-chalk/dark/css-vars.css';
import router from "./router/index.js";
import {createPinia} from 'pinia';
import i18n from "./utils/i18n.js";

const app = createApp(App)
const pinia = createPinia()

app.use(ElementPlus).use(pinia).use(router).use(i18n).mount('#app')
