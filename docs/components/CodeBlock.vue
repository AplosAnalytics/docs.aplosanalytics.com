<template>
  <div class="`language-${langClass} vp-adaptive-theme line-numbers-mode`">
    <span v-if="link">
      <a v-bind:href="link" target="_blank">Full Source</a>
    </span>
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
  highlightLines: {
    type: Array,
    default: () => [],
  },
  showLineNumbers: {
    type: Boolean,
    default: true,
  },
  displayLines: {
    type: Array, // Array of integers or ranges
    default: () => [],
  },
  link: {
    type: String,
    default: "",
  },
});

const code = ref("");
//const code = ref("");
const htmlFormattedCode = ref("");

const langClass = computed(() => props.lang.toLowerCase());
const highlighter = ref(null);
const language_comment_blocks = [
  {
    lang: "python",
    start: "#",
    end: "",
  },
  {
    lang: "html",
    start: "<!-- ",
    end: "-->",
  },
  {
    lang: "c#",
    start: "//",
    end: "",
  },
  {
    lang: "java",
    start: "//",
    end: "",
  },
  {
    lang: "R",
    start: "#",
    end: "",
  },
  {
    lang: "shell",
    start: "#",
    end: "",
  },
  {
    lang: "bash",
    start: "#",
    end: "",
  },

];
// Fetch and highlight code
async function highlightCode() {
  const highlighter = await getHighlighter({
    themes: ["github-dark", "github-light"],
    langs: [props.lang],
    showLineNumbers: props.showLineNumbers,
  });

  if (!highlighter) {
    console.error("Highlighter not initialized.");
    return;
  }
  try {
    const validLines = props.highlightLines.filter(
      (line) => line != null && Number.isInteger(line)
    );

    const highlightedCode = highlighter.codeToHtml(code.value, {
      lang: props.lang,
      lineOptions: validLines.map((line) => ({ line, classes: ["highlighted"] })),
      themes: {
        dark: "github-dark", // 'slack-dark',
        light: "github-light", //'slack-ochin',
      },
    });
    htmlFormattedCode.value = removeUnwantedStyles(highlightedCode);
  } catch (e) {
    console.error("Error highlighting code:", e);
  }
}

function wrap_comment_for_lang_text(text) {
  console.log(props.lang);
  const block = language_comment_blocks.find(comment => comment.lang.toLowerCase() === props.lang.toLowerCase());
  
  if (block) {
    const start = block["start"]
    const end = block["end"]
    text = `${start}${text}${end}`
  }
  // todo make this

  return text;
}

function skiped_lines_text(start, end) {
  const text = `... skipped lines [${start}-${end}] for brevity...`;

  return wrap_comment_for_lang_text(text);
}

function removeUnwantedStyles(formattedCode) {
  const unwantedStyles = [
    "background-color:#24292e",
    "color:#e1e4e8",
    "background-color:#222222",
    "color:#E6E6E6",
    "background-color:#fff;--shiki-dark-bg:#24292e;",
    "color:#24292e;--shiki-dark:#e1e4e8",
  ];
  unwantedStyles.forEach((style) => {
    formattedCode = formattedCode.replace(new RegExp(escapeRegExp(style), "g"), "");
  });
  return formattedCode;
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

function filterLines(lines, displayLines) {
  let result = [];
  let lastLineIndex = -2; // Adjusted to -2 to handle edge case for the first element appropriately

  displayLines.forEach((item) => {
    let currentStart = -1;
    let currentEnd = -1;

    if (typeof item === "number") {
      currentStart = currentEnd = item - 1; // Convert 1-based to 0-based index
    } else if (item.start && item.end) {
      currentStart = item.start - 1;
      currentEnd = item.end - 1;
    }

    // Check if there is a gap and insert a placeholder with skipped lines range
    if (lastLineIndex >= 0 && currentStart > lastLineIndex + 1) {
      const skippedStart = lastLineIndex + 2; // Convert back to 1-based and adjust to next line after last
      const skippedEnd = currentStart; // Already 0-based, adjust to 1-based by not adding 1
      const text = skiped_lines_text(skippedStart, skippedEnd);
      result.push(text);
    }

    // Add lines for current start to end if they exist
    for (let i = currentStart; i <= currentEnd && i < lines.length; i++) {
      if (lines[i]) {
        result.push(lines[i]);
      }
    }

    // Update lastLineIndex to the end of the current range
    lastLineIndex = currentEnd;
  });

  // After processing all items, check if there are any lines left to display
  if (lastLineIndex < lines.length - 1) {
    const skippedStart = lastLineIndex + 2; // The next line after the last included line
    const skippedEnd = lines.length; // The last line of the document
    const text = skiped_lines_text(skippedStart, skippedEnd);
    result.push(text);
  }

  return result.join("\n");
}

async function fetchCode(src) {
  const response = await fetch(src);
  if (!response.ok) {
    throw new Error("Failed to fetch code");
  }
  const text = await response.text();
  if (props.displayLines.length === 0) {
    return text;
  }
  const lines = text.split("\n");
  return filterLines(lines, props.displayLines);
}
</script>

<style scoped>
code {
  counter-reset: step;
  counter-increment: step 0;
}

code .line::before {
  content: counter(step);
  counter-increment: step;
  width: 1rem;
  margin-right: 1.5rem;
  display: inline-block;
  text-align: right;
  color: rgba(115, 138, 148, 0.4);
}
</style>
