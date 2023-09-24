import { createApp } from 'vue';
import { 
    Button,
    ConfigProvider,
    Card,
    Layout,
    Menu,
    Breadcrumb
} from 'ant-design-vue';
import router from './router'
import App from './App';
import 'ant-design-vue/dist/reset.css'

const app = createApp(App);

app.use(router)

// antd-vue
app.use(Button)
app.use(ConfigProvider)
app.use(Card)
app.use(Layout)
app.use(Menu)
app.use(Breadcrumb)

app.mount('#app');