import DefaultTheme from 'vitepress/theme'
import panZoom from 'vue-panzoom'

import panContainer from './components/pan-container.vue'
import Layout from './layout.vue'

import './style.css'

/** @type {import('vitepress').Theme} */
export default {
    extends: DefaultTheme,
    Layout,

    enhanceApp({ app }) {
        app.use(panZoom)
        app.component('pan-container', panContainer)
    }
}
