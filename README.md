# OpenDoc

A static site generator with an integrated workbench, AI chat, and interactive terminal — all in a single Go binary.

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│                   Single Go Binary                       │
│                     (opendoc)                            │
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐ │
│  │   CLI    │  │   Core   │  │  Server  │  │  Chat   │ │
│  │ (cobra)  │  │  SSG     │  │  (chi)   │  │  LLM    │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬────┘ │
│       │              │              │              │      │
│  ┌────┴──────────────┴──────────────┴──────────────┴────┐│
│  │              Embedded Assets (go:embed)               ││
│  │         themes/ · public/ · templates                 ││
│  └──────────────────────────────────────────────────────┘│
└──────────────────────────────────────────────────────────┘
```

**Key features:**
- Zero runtime dependencies (no Node.js, no Python, no nginx)
- 20MB single binary with all assets embedded
- Markdown → HTML with math (KaTeX), tabbed code blocks, margin notes
- Full workbench UI with file editor, live preview, and AI chat
- Anthropic (Claude) and OpenAI (GPT) integration with tool calling
- Interactive terminal (Bubble Tea TUI) via WebSocket
- Private pages with publish mode for public-only builds
- Docker support with simplified single-binary image

## Quick Start

### Build from source

```bash
# Build
go build -o opendoc ./cmd/opendoc

# Create a new project
./opendoc new my-site

# Build the static site
./opendoc build my-site

# Serve with live reload
./opendoc serve my-site

# Start the full workbench (IDE + chat + preview)
./opendoc workbench my-site
```

### Using Make

```bash
make build          # Build the binary
make docs           # Build the documentation site
make serve          # Serve docs with live reload
make workbench      # Start the workbench
```

### Docker

```bash
# Create a workspace directory
mkdir workspace

# Start with Docker Compose
docker compose up -d

# Open http://localhost:3000
```

Set `ANTHROPIC_API_KEY` in your `.env` for AI chat features.

## CLI Reference

```
opendoc build [project-dir]              Build the static site
opendoc serve [project-dir] [-p port]    Serve with live reload
opendoc new <name>                       Scaffold a new project
opendoc workbench [dir] [-p port]        Start the workbench
opendoc publish [dir] [--repo o/r]       Deploy to GitHub Pages
opendoc status [project-dir]             Show project health/info
opendoc config show                      Display global config
opendoc config set <key> <value>         Set a config value
opendoc config path                      Print config file location
opendoc tui                              Run interactive terminal UI
```

### App Configuration

OpenDoc stores global settings in `~/.config/opendoc/config.yml`:

```yaml
github:
  default_account: "your-username"
defaults:
  author: "Your Name"
  theme: "default"
  port: 3000
```

Configure via `opendoc config set`:

```bash
opendoc config set github.default_account cottrellashley
opendoc config set defaults.author "Ashley Cottrell"
```

### Publishing to GitHub Pages

```bash
# Uses settings.json github_repo, app config, or git remote
opendoc publish

# Explicit repo
opendoc publish --repo cottrellashley/my-site
```

Requires the [GitHub CLI](https://cli.github.com/) (`gh`) to be installed and authenticated.

## Project Structure

```
opendoc.go                  # go:embed declarations
cmd/opendoc/                # CLI entry point (cobra)
internal/
  core/
    config.go               # YAML config loading + validation
    content.go              # Frontmatter parsing, page/entry discovery
    renderer.go             # goldmark + pongo2 rendering, TOC
    builder.go              # Full build pipeline
    scaffold.go             # Project scaffolding
    appconfig.go            # Global app config (~/.config/opendoc/)
    publish.go              # GitHub Pages deployment
    cliutil.go              # CLI output helpers (colours, formatting)
    extensions/
      math.go               # LaTeX preprocessor
      tabs.go               # Tabbed code blocks
      sidenotes.go          # Tufte-style margin notes
  server/
    server.go               # HTTP server setup (chi)
    files.go                # File CRUD API
    build.go                # Build/publish API + preview serving
    settings.go             # Settings management
    sse.go                  # Server-Sent Events
    watcher.go              # File watcher with debounce
  chat/
    adapter.go              # LLM adapter interface
    anthropic.go            # Claude adapter (streaming + tools)
    openai.go               # GPT adapter (streaming + tools)
    tools.go                # Tool definitions + executor
    session.go              # Session management + API routes
  tui/                      # Bubble Tea interactive TUI
  web/                      # Console WebSocket server
  pty/                      # PTY management
themes/                     # Built-in themes (embedded)
public/                     # Workbench UI (embedded)
docs/                       # Documentation site
```

## Markdown Extensions

### Math (KaTeX)

Inline: `$E = mc^2$`

Display:
```
$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}
$$
```

Theorem blocks:
```
:::theorem Pythagorean Theorem
For a right triangle: $a^2 + b^2 = c^2$
:::
```

### Tabbed Code Blocks

```
:::tabs
=== Python
\`\`\`python
print("hello")
\`\`\`
=== JavaScript
\`\`\`javascript
console.log("hello")
\`\`\`
:::
```

### Margin Notes

```
:::sidenote Important Note
This appears in the margin on wide screens.
:::
```

## Configuration (opendoc.yml)

```yaml
site:
  name: "My Site"
  url: "https://example.com"
  author: "Your Name"

content:
  dir: "content"

build:
  output_dir: "dist"

collections:
  blog:
    sort: "newest_first"
    date_format: "%B %d, %Y"
    items_per_page: 10
    tags: true
    archive: true
    layout: "timeline"

nav:
  - Home: index.md
  - Blog: blog/
  - About: about.md
  - Private: secret.md?    # ? suffix = private page

theme:
  name: "default"
```

## Go Dependencies

| Purpose | Library |
|---|---|
| Markdown | `github.com/yuin/goldmark` |
| Syntax highlighting | `github.com/yuin/goldmark-highlighting/v2` (chroma) |
| Templates | `github.com/flosch/pongo2/v6` |
| YAML | `gopkg.in/yaml.v3` |
| HTTP router | `github.com/go-chi/chi/v5` |
| File watching | `github.com/fsnotify/fsnotify` |
| CLI | `github.com/spf13/cobra` |
| WebSocket | `github.com/gorilla/websocket` |
| PTY | `github.com/creack/pty` |
| TUI | `github.com/charmbracelet/bubbletea` |

## License

MIT
