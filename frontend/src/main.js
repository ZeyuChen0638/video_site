import { createApp } from 'vue';
import { 
    Button,
    ConfigProvider,
    Card,
    Layout,
    Menu,
    Breadcrumb,
    Row,
    Col,
    Form,
    Divider,
    Empty,
    Tabs,
    Carousel,
    Image,
    Modal,
    Input,
    Avatar,
    Tag,
    Space
} from 'ant-design-vue';
import router from './router'
import store from './store/'
import App from './App';
import 'ant-design-vue/dist/reset.css'

import '@/assets/iconfont/iconfont.js'
// import '@/assets/iconfont/iconfont.css'
import SvgIcon from '@/assets/iconfont/IconSvg.vue'

const app = createApp(App);

app.use(router)
app.use(store)

// antd-vue
app.use(Button)
app.use(ConfigProvider)
app.use(Card)
app.use(Layout)
app.use(Menu)
app.use(Breadcrumb)
app.use(Row)
app.use(Col)
app.use(Form)
app.use(Divider)
app.use(Empty)
app.use(Tabs)
app.use(Carousel)
app.use(Image)
app.use(Modal)
app.use(Input)
app.use(Avatar)
app.use(Tag)
app.use(Space)

app.component('svg-icon', SvgIcon)
app.mount('#app');