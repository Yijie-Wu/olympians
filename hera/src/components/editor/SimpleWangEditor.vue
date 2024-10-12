<script setup>
import '@wangeditor/editor/dist/css/style.css'
import {onBeforeUnmount, shallowRef, watch, toRef, ref} from 'vue'
import {Editor, Toolbar} from '@wangeditor/editor-for-vue'
import {i18nChangeLanguage} from '@wangeditor/editor'

i18nChangeLanguage('en')

const data = ref('')
const editorRef = shallowRef()
const emits = defineEmits(['input']);
const editor_class = ref('editor-basic')
const editor_toolbar_class = ref('toolbar-basic')

const props = defineProps({
  editorHeight: {
    type: String,
    default: '100%'
  },
  editorWidth: {
    type: String,
    default: '100%'
  },
  hidden: {
    type: String,
    default: 'hidden'
  },
  mode: {
    type: String,
    default: 'default'
  },
  viewMode: {
    type: Boolean,
    default: false
  },
  editorData: {
    type: String,
    default: ''
  }
})

const toolbarConfig = {
  toolbarKeys: [
    'color', 'emotion', 'insertLink', 'todo', 'uploadImage', 'uploadVideo', 'fullScreen',
  ]
}
const editorConfig = {
  placeholder: '',
  MENU_CONF: {
    'uploadImage': {
      server: 'http://127.0.0.1:8000/upload/document/image',
      allowedFileTypes: ['image/*'],
      timeout: 5 * 1000,
      maxFileSize: 50 * 1024 * 1024,
      fieldName: 'file',
      maxNumberOfFiles: 1,
    },
    'uploadVideo': {
      server: 'http://127.0.0.1:8000/upload/document/video',
      fieldName: 'file',
      maxNumberOfFiles: 1,
      allowedFileTypes: ['video/*'],
      timeout: 3600 * 1000,
      maxFileSize: 5000 * 1024 * 1024
    }
  },

}

watch(toRef(props, 'editorData'), (newValue) => {
  data.value = newValue;
  const editor = editorRef.value;
  if (editor) {
    editor.setHtml(newValue);
  }
});

onBeforeUnmount(() => {
  const editor = editorRef.value
  if (editor == null) return
  editor.destroy()
})

const handleCreated = (editor) => {
  editorRef.value = editor
  if (props.viewMode === true) {
    editor.disable()
  } else {
    editor.enable()
  }

  if (props.editorData) {
    editor.setHtml(props.editorData);
  }
}

const handleChange = (editor) => {
  emits('input', editor.getHtml());
}

const handleDestroyed = (editor) => {
  editorRef.value = null
}

const handleFocus = (editor) => {
  editor_class.value = 'editor-basic-focus'
  editor_toolbar_class.value = 'toolbar-basic-focus'
}

const handleBlur = (editor) => {
  editor_class.value = 'editor-basic'
  editor_toolbar_class.value = 'toolbar-basic'
}

const customAlert = (info, type) => {
  alert(`Alert: ${type} - ${info}`)
}

const customPaste = (editor, event, callback) => {
  callback(true)
}

</script>

<template>
  <div :class="editor_class">
    <Toolbar :editor="editorRef" :defaultConfig="toolbarConfig" :mode="props.mode" :class="editor_toolbar_class" v-show="props.viewMode !== true"/>
    <Editor
        :defaultConfig="editorConfig"
        :mode=props.mode
        v-model="data"
        :style="{height: props.editorHeight, overflowY: props.hidden, width: props.editorWidth}"
        @onCreated="handleCreated"
        @onChange="handleChange"
        @onDestroyed="handleDestroyed"
        @onFocus="handleFocus"
        @onBlur="handleBlur"
        @customAlert="customAlert"
        @customPaste="customPaste"
    />
  </div>
</template>

<style scoped>
.editor-basic {
  width: 100%;
  height: 100%;
}

:deep(.w-e-image-container img) {
  max-width: 100%;
  height: auto;
}

:deep(.w-e-textarea-video-container video) {
  max-width: 100%;
  height: auto;
}

.editor-basic-focus {
  border: 1px solid #1ab734;
}

.toolbar-basic {
  border-bottom: 1px solid #ccc;
}

.toolbar-basic-focus {
  border-bottom: 1px solid #1ab734;
}


</style>
