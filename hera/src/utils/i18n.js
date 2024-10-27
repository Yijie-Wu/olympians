// i18n.js
import { createI18n } from 'vue-i18n';

// 导入翻译文件
import en from '@/locales/en.json';
import zh from '@/locales/zh.json';

const i18n = createI18n({
  locale: 'zh', // 默认语言
  fallbackLocale: 'en', // 回退语言
  messages: {
    en,
    zh,
  },
});

export default i18n;
