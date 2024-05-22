import DefaultTheme from 'vitepress/theme'

import panContainer from './components/pan-container.vue'
import Layout from './layout.vue'

import './style.css'
import './printing-doc.css'

/** @type {import('vitepress').Theme} */
export default {
    extends: DefaultTheme,
    Layout,

    enhanceApp({ app }) {
        app.component('pan-container', panContainer)
    }
}
