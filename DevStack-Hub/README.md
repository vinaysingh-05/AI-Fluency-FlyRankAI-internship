# DevStack Hub

DevStack Hub is a modern, local-first developer resource and code snippet manager built to store, organize, and retrieve frequently used code blocks and templates instantly[cite: 1, 5].

## Core Features

* **Offline-First Persistence**: Data is serialized and securely saved directly to your browser's `localStorage`, ensuring your snippets persist across hard page refreshes without cloud dependencies[cite: 5, 6].
* **Responsive Dark-Mode Dashboard**: Features a clean developer-centric UI optimized for mobile, tablet, and widescreen desktop displays[cite: 1, 6].
* **Real-Time Search & Filtering**: Instantly filters snippets by title, category metadata, or raw code content as you type[cite: 1, 6].
* **One-Click Clipboard Copying**: Quickly copy code snippets directly to your clipboard using the native clipboard API, accompanied by visual toast notifications[cite: 1, 6].

## Technical Hardening & Edge Cases

* **Client-Side Form Validation**: Intercepts empty submissions on title or code text areas with inline warning messages[cite: 1, 6].
* **Double-Click Prevention**: Utilizes an execution lock (`isSubmitting`) and disabled button states to prevent rapid double-clicking from creating duplicate entries[cite: 1, 6].
* **XSS Sanitization**: Dynamically sanitizes input strings to safely render raw user code blocks[cite: 6].

## Tech Stack

* **HTML5**
* **Tailwind CSS** (via CDN)[cite: 1, 6]
* **Vanilla JavaScript** (ES6+)[cite: 1, 6]
