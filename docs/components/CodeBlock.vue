<template>
  <div class="`language-${langClass} vp-adaptive-theme line-numbers-mode`">
    <span v-if="link">
      <a v-bind:href="link" target="_blank" style="font-size: 12px;padding:10px;text-decoration:none;" >Full Source </a>
    </span>
    <button title="Copy Code" class="copy"></button>
    <span class="lang">{{ lang.toLowerCase() }}</span>

    <div v-html="htmlFormattedCode"></div>
    <!-- <div class="line-numbers-wrapper" aria-hidden="true"><span class="line-number">1</span><br><span class="line-number">2</span><br><span class="line-number">3</span><br><span class="line-number">4</span><br><span class="line-number">5</span><br><span class="line-number">6</span><br><span class="line-number">7</span><br><span class="line-number">8</span><br><span class="line-number">9</span><br><span class="line-number">10</span><br><span class="line-number">11</span><br><span class="line-number">12</span><br><span class="line-number">13</span><br><span class="line-number">14</span><br><span class="line-number">15</span><br><span class="line-number">16</span><br><span class="line-number">17</span><br><span class="line-number">18</span><br><span class="line-number">19</span><br><span class="line-number">20</span><br><span class="line-number">21</span><br><span class="line-number">22</span><br><span class="line-number">23</span><br></div> -->
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
  highlighColor: {
    type: String,
    default: "green"
  },
  showSkippedLinesHelp: {
    type: Boolean,
    default: true
  }
});

const code = ref("");
//const code = ref("");
const htmlFormattedCode = ref("");

const langClass = computed(() => props.lang.toLowerCase());
const highlighter = ref(null);
const color_maps = [
  {
    "name": "yellow",
    "code":  "rgba(255, 255, 0, 0.3)"
  },
  {
    "name": "blue",
    "code":  "rgba(0, 0, 255, 0.3)"
  },
  {
    "name": "green",
    "code":  "rgba(0, 255, 0, 0.3)"
  },
  {
    "name": "red",
    "code":  "rgba(255, 0, 0, 0.3)"
  },
  {
    "name": "pink",
    "code":  "rgba(255, 192, 203, 0.3)"
  },

]
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
    themes: ["github-dark", "github-light", "slack-dark", "slack-ochin"],
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
    // console.log("validLines")
    // console.log(validLines)
    const lineOptions =validLines.map((line) => ({ line, classes: ["highlighted"] }))
    // console.log(lineOptions)
    const highlightedCode = highlighter.codeToHtml(code.value, {
      lang: props.lang,
      lineOptions: lineOptions,
      themes: {
        dark: "slack-dark", // 'slack-dark',
        light: "slack-ochin", //'slack-ochin',
        //dark: "github-dark", 
        //light: "github-light",
      },
    });
    htmlFormattedCode.value = addHighlightedClassToLines(removeUnwantedStyles(highlightedCode), validLines);
  } catch (e) {
    console.error("Error highlighting code:", e);
  }
}

// hack to add the highlighted class
function addHighlightedClassToLines(htmlCode, lines) {
  const parser = new DOMParser();
  const doc = parser.parseFromString(htmlCode, 'text/html');
  const lineElements = doc.querySelectorAll('code > span');
  const color_code_block = color_maps.find(color => color.name.toLowerCase() === props.highlighColor.toLowerCase()) 
    || { name: "Default", code: "rgba(128, 128, 128, 0.5)" };  // Default to gray if no match
  ;
  const color_code = color_code_block["code"]
  lines.forEach(line => {
    if (lineElements[line - 1]) { // line numbers are 1-based, array is 0-based
      lineElements[line - 1].classList.add('highlighted');
      lineElements[line - 1].style.setProperty('background-color', `${color_code}`, 'important'); // 50% transparent yellow
      lineElements[line - 1].style.setProperty('color', 'black', 'important');
      // lineElements[line - 1].style.setProperty('padding', '0 2px', 'important');
    }
  });

  return doc.body.innerHTML;
}

function wrap_comment_for_lang_text(text) {
  // console.log(props.lang);
  const block = language_comment_blocks.find(comment => comment.lang.toLowerCase() === props.lang.toLowerCase());
  
  if (block) {
    const start = block["start"]
    const end = block["end"]
    text = `${start}${text}${end}`
  }
  // todo make this

  return text;
}

function skipped_lines_text(start, end) {
  //console.log(`props.showSkippedLinesHelp: ${props.showSkippedLinesHelp}`)
  if (props.showSkippedLinesHelp) {
    const text = `... skipped lines [${start}-${end}] for brevity...`;

    return wrap_comment_for_lang_text(text);
  }
  return ""
  
}

function removeUnwantedStyles(formattedCode) {

  
  const unwantedStyles = [
    "background-color:#24292e",
    "color:#e1e4e8",
    "background-color:#222222",
    "color:#E6E6E6",
    "background-color:#fff;--shiki-dark-bg:#24292e;",
    "color:#24292e;--shiki-dark:#e1e4e8",
    // "background-color:#FFF;", 
    "--shiki-dark-bg:#222222;", 
    "color:#002339;",
    "--shiki-dark:#E6E6E6"
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


function expandDisplayLines(inputLines) {
  const result = [];
  inputLines.forEach(item => {
    if (typeof item === "number") {
      result.push(item);
    } else if (item.start && item.end) {
      for (let i = item.start; i <= item.end; i++) {
        result.push(i);
      }
    }
  });
  return result.sort((a, b) => a - b); // Ensure the array is sorted
}

function filterLines(lines, displayLines) {
  let result = [];
  let lastDisplayedIndex = -1; // Initialize to -1 to handle the first line's check correctly
  const linesToDisplay = expandDisplayLines(displayLines);

  // Check for initially skipped lines (before the first displayed line)
  if (linesToDisplay[0] > 1) {
    const text = skipped_lines_text(1, linesToDisplay[0] - 1);
    result.push(text);
  }

  linesToDisplay.forEach((lineNumber) => {
    const currentIndex = lineNumber - 1; // Convert to 0-based index

    // Check for skipped lines before this one
    if (lastDisplayedIndex !== -1 && currentIndex > lastDisplayedIndex + 1) {
      const skippedStart = lastDisplayedIndex + 2; // The next line after the last included line
      const skippedEnd = currentIndex; // One line before the current line
      const text = skipped_lines_text(skippedStart, skippedEnd);
      result.push(text);
    }

    // Add the current line if it exists
    if (lines[currentIndex]) {
      result.push(lines[currentIndex]);
    }

    // Update the last displayed index
    lastDisplayedIndex = currentIndex;
  });

  // Check for any remaining lines after the last displayed line
  if (lastDisplayedIndex < lines.length - 1) {
    const skippedStart = lastDisplayedIndex + 2;
    const skippedEnd = lines.length;
    const text = skipped_lines_text(skippedStart, skippedEnd);
    result.push(text);
  }

  return result.join('\n');
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


