<template>
  <div class="`language-${langClass} vp-adaptive-theme line-numbers-mode`">
    <button title="Copy Code" class="copy"></button>
    <span class="lang">{{ lang.toLowerCase() }}</span>

    <div v-html="htmlFormattedCode"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, watchEffect, computed } from "vue";
import { getHighlighter, codeToHtml } from "shiki";

const props = defineProps({
  src: {
    type: String,
    required: true,
  },
  lang: {
    type: String,
    default: "plaintext", // Default to plaintext if no language is provided
  },
});

const code = ref("");
const htmlFormattedCode = ref("");

const langClass = computed(() => props.lang.toLowerCase());

// Fetch and highlight code
async function highlightCode() {
  try {
    htmlFormattedCode.value = await codeToHtml(code.value, {
      lang: props.lang,

      themes: {
        dark: "github-dark", // 'slack-dark',
        light: "github-light", //'slack-ochin',
      
      },
      
      // testing line highlight, it's not working yet... i think it's a different pattern
      // this is based on some docs but based on parameters, i don't think is correct anymore
      // lineOptions: [
      //     { line: 10, classes: ['highlighted']}
      // ]
    });
    // it's doing some light grey formatting,
    // so i'm removing it until i can figure out where it's coming from
    const find = [
      "background-color:#24292e",
      "color:#e1e4e8",
      "background-color:#222222",
      "color:#E6E6E6",
    ];
    htmlFormattedCode.value = findAndReplace(htmlFormattedCode.value, find, "", false);
  } catch (e) {
    console.error(e);
  }
}

function findAndReplace(str, find, replace, caseSensitive = true) {
  // If case sensitivity is not required, transform both the string and the find pattern to lowercase

  for (let f in find) {
    // console.log(f)
    const find_str = find[f];
    if (!caseSensitive) {
      str = str.replace(new RegExp(escapeRegExp(find_str), "gi"), replace);
    } else {
      str = str.replace(new RegExp(escapeRegExp(find_str), "g"), replace);
    }
  }

  return str;
}

/**
 * Escapes special characters in a string for use in a regular expression.
 *
 * @param {string} str - The string to escape.
 * @returns {string} The escaped string.
 */
function escapeRegExp(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); // $& means the whole matched string
}

// Initialize Shiki with an initial theme and preload additional theme

onMounted(async () => {
  code.value = await fetchCode(props.src);
  highlightCode(); // Highlight the initial code
});

// React to system theme changes
watchEffect(() => {
  highlightCode(); // Re-highlight the code
});

async function fetchCode(src) {
  const response = await fetch(src);
  if (!response.ok) {
    throw new Error("Failed to fetch code");
  }
  return await response.text();
}
</script>
