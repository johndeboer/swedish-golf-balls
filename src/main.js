import './assets/main.css'


import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config'
import Tailwind from 'primevue/passthrough/tailwind'
import { usePassThrough } from 'primevue/passthrough'

const app = createApp(App)

const CustomTailwind = usePassThrough(
    Tailwind,
    {
        accordion: {
            root: 'mb-1',
            accordiontab: {
                root: 'mb-1',
                header: ({ props }) => ({
                    class: [
                        { 'select-none pointer-events-none cursor-default opacity-60': props?.disabled } // Condition
                    ]
                }),
                headerAction: ({ context }) => ({
                    class: [
                        'flex items-center cursor-pointer relative no-underline select-none', // Alignments
                        'p-5 transition duration-200 ease-in-out rounded-t-md font-bold transition-shadow duration-200', // Padding and transition
                        'border border-gray-300 bg-gray-100 text-gray-600', // Borders and colors
                        'dark:bg-gray-900 dark:border-blue-900/40 dark:text-white/80 dark:hover:bg-gray-800/80 dark:focus:shadow-[inset_0_0_0_0.2rem_rgba(147,197,253,0.5)]', // Dark mode
                        'hover:border-gray-300 hover:bg-gray-200 hover:text-gray-200', // Hover
                        'focus:outline-none focus:outline-offset-0 focus:shadow-[inset_0_0_0_0.2rem_rgba(191,219,254,1)]', // Focus
                        { 'rounded-br-md rounded-bl-md': !context.active, 'rounded-br-0 rounded-bl-0 text-gray-800': context.active } // Condition
                    ]
                }),
                headerIcon: 'inline-block mr-2',
                headerTitle: 'leading-none',
                content: {
                    class: [
                        'p-5 border border-gray-300 bg-white text-gray-700 border-t-0 rounded-tl-none rounded-tr-none rounded-br-lg rounded-bl-lg',
                        'dark:bg-gray-900 dark:border-blue-900/40 dark:text-white/80' // Dark mode
                    ]
                },
                
            }
        }
    }
)
app.use(PrimeVue, {unstyled: true, pt: CustomTailwind})
app.mount('#app')