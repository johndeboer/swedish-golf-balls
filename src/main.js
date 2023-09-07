import './assets/main.css'


import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config'
import Tailwind from 'primevue/passthrough/tailwind'

const app = createApp(App)

app.use(PrimeVue, {unstyled: true, pt: Tailwind})
app.mount('#app')