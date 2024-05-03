<template>
  <div class="`language-${langClass} vp-adaptive-theme`">
    <button title="Copy Code" class="copy"></button>
    <span class="lang">{{ lang.toLowerCase() }}</span>
    <pre v-html="highlightedCode" class="shiki shiki-themes github-light github-dark vp-code"></pre>
        
  </div>
</template>

<script setup>
import { ref, onMounted, watchEffect, computed } from 'vue';
import { getHighlighter, codeToHtml } from 'shiki';

const props = defineProps({
  src: {
    type: String,
    required: true,
  },
  lang: {
    type: String,
    default: 'plaintext'  // Default to plaintext if no language is provided
  }
});

const code = ref('');
const highlightedCode = ref('');
const isDarkMode = ref(window.matchMedia('(prefers-color-scheme: dark)').matches);
const langClass = computed(() => props.lang.toLowerCase());

// Fetch and highlight code
async function highlightCode() {
  
  try{
    highlightedCode.value = await codeToHtml(code.value, 
      { 
        lang: props.lang, 
        theme: isDarkMode.value ? 'github-dark' : 'github-light'
      }
    
    );
    //background-color:#24292e;color:#e1e4e8
    const find = "background-color:#24292e;color:#e1e4e8"
    highlightedCode.value = findAndReplace(highlightedCode.value, find, "", false);
    //highlightedCode.value = highlighter.codeToHtml(code.value, { lang: props.lang });
  } catch(e){
    console.error(e)
  }
  
}

function findAndReplace(str, find, replace, caseSensitive = true) {
    // If case sensitivity is not required, transform both the string and the find pattern to lowercase
    if (!caseSensitive) {
        return str.replace(new RegExp(escapeRegExp(find), 'gi'), replace);
    } else {
        return str.replace(new RegExp(escapeRegExp(find), 'g'), replace);
    }
}

/**
 * Escapes special characters in a string for use in a regular expression.
 * 
 * @param {string} str - The string to escape.
 * @returns {string} The escaped string.
 */
function escapeRegExp(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');  // $& means the whole matched string
}

// Initialize Shiki with an initial theme and preload additional theme

onMounted(async () => {
  
  code.value = await fetchCode(props.src);
  highlightCode();  // Highlight the initial code
});

// React to system theme changes
watchEffect(() => {
  
  highlightCode();  // Re-highlight the code
});

async function fetchCode(src) {
  const response = await fetch(src);
  if (!response.ok) {
    throw new Error('Failed to fetch code');
  }
  return await response.text();
}
</script>

<style scoped>
pre {
  background-color: var(--shiki-color-background); 
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
}
.copy-button {
  position: absolute;
  right: 5px;
  top: 5px;
}
.language-label {
  display: block;
  text-transform: uppercase;
  color: var(--shiki-color-foreground); 
}
</style>
