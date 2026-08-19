<p align="center">
  <a href="README.md">简体中文</a> · <b>English</b>
</p>

# 🚀 Peekdown

A lightweight native Windows markdown viewer and editor. Notepad-fast startup, Obsidian-pretty rendering — in a single ~800 KB executable.

Built with Rust + WebView2. No installer, no runtime dependencies, no Electron.

![Preview mode](screenshot%201.jpg)
![Split view](screenshot%202.jpg)

## ✅ Features

- **Instant startup** ⚡ — native window, no framework overhead
- **Live preview** 👀 — rendered markdown with full GFM support (tables, task lists, footnotes)
- **Marco rendering** 🎨 — signature Astro/Space preview style: left-aligned gradient headings, full-width content and tables
- **Split view** ↔️ — side-by-side editor and preview with live sync (Ctrl+\\)
- **Syntax highlighting** 🌈 — 30+ languages via highlight.js
- **Multi-tab** 📑 — open multiple files, auto-hides tab bar for single files
- **Dark/Light themes** 🌙/☀️ — toggle with one click
- **Find in document** 🔍 — Ctrl+F with match highlighting and navigation
- **Table of Contents** 🧭 — auto-generated outline sidebar (Ctrl+Shift+O)
- **Zoom** 🔎 — Ctrl+/- or Ctrl+scroll, with level indicator
- **Drag & drop** 📥 — drop `.md` files to open, drop multiple to open tabs
- **Adjustable preview width** 📐 — drag the edge to resize
- **Recent files** 🕘 — quick-open panel on empty tabs
- **Cross-mode selection** 🔄 — selected text stays selected when toggling edit/preview
- **File associations** 📄 — use as default `.md` viewer via "Open With"
- **Single executable** 💾 — everything embedded, nothing to install

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| Ctrl+O | Open file |
| Ctrl+S | Save |
| Ctrl+Shift+S | Save As |
| Ctrl+N | New tab |
| Ctrl+W | Close tab |
| Ctrl+Tab | Next tab |
| Ctrl+Shift+Tab | Previous tab |
| Ctrl+E | Toggle edit/preview |
| Ctrl+\\ | Toggle split view |
| Ctrl+F | Find in document |
| Ctrl+Shift+O | Toggle outline |
| Ctrl+= / Ctrl+- | Zoom in/out |
| Ctrl+0 | Reset zoom |

## 🛠️ Build

Requires Rust and the WebView2 runtime (pre-installed on Windows 10/11).

```bash
cargo build --release
```

Output: `target/release/peekdown.exe`

### 🚦 Release via GitHub Actions

Push a `v*` tag to automatically build and publish a release:

```bash
git tag v1.2.3 && git push origin v1.2.3
```

```bash
target/x86_64-pc-windows-msvc/release/peekdown.exe
```

## ⚙️ Tech Stack

- **Rust** — window management, file I/O, IPC ([tao](https://github.com/niceshell/niceshell) + [wry](https://github.com/niceshell/niceshell))
- **WebView2** — rendering engine (Edge, pre-installed on Win10/11)
- **marked.js** — markdown to HTML
- **highlight.js** — code syntax highlighting
- **No Electron, no Node, no bundler** — all frontend assets are embedded at compile time via `include_str!`

## 📄 License

MIT