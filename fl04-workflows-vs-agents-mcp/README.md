# FL-04 // Flyrank Build — Workflows vs. Agents & MCP Integration

Submission for the **Flyrank AI Internship — Build (core) Phase**.

A single-page dashboard (`index.html`) and companion report (`FL-04_Workflows_vs_Agents_MCP.pdf`) covering workflow vs. agent architecture, the FL-04 classification, MCP's core primitives, an evaluator-optimizer agent upgrade, and 3 live MCP tool-use evidence outputs.

**Status:** Complete &nbsp;|&nbsp; **Estimated Hours:** 5

---

## Contents

| File | Description |
|---|---|
| `index.html` | Interactive, self-contained submission dashboard (inline CSS/JS, no build step) |
| `FL-04_Workflows_vs_Agents_MCP.pdf` | Printable PDF version of the same content |

## What's Inside

### 1. Workflow vs. Agent Explainer
- Defines what an agent is: a system where the model itself controls the loop — deciding which tools to call, in what order, and when to stop.
- Contrasts **fixed DAGs** (developer-orchestrated, single deterministic path) against **dynamic reasoning loops** (model-orchestrated, branching, self-correcting).
- Side-by-side comparison of control flow, tool execution, pathing, and feedback loops.

### 2. FL-04 Classification
FL-04 is classified as a **Workflow** — a fixed 3-step handoff:

```
Draft → Critique → Revise
```

Each stage runs exactly once, in a predetermined order, with no autonomous back-tracking or evaluation gate — the defining trait that separates it from an agent.

### 3. MCP Primitives
Breakdown of the three core Model Context Protocol primitives:

| Primitive | Controlled by | Purpose |
|---|---|---|
| **Tools** | Model | Executable functions for actions/mutations (API calls, DB writes) |
| **Resources** | Application | Read-only contextual data (configs, local files) |
| **Prompts** | User | Standardized slash-commands and interaction templates |

### 4. Evaluator-Optimizer Agent Upgrade
A concrete upgrade path that turns FL-04 from a one-way assembly line into a looping agent:

```
Draft → Critique → Evaluator (score) → Score > 9/10 ? Terminate
                        ↺ (if score ≤ 9)
        re-query MCP tools → Optimizer revises → back to Evaluator
```

Covers dynamic re-querying, the feedback loop, and the auto-termination threshold (score > 9/10).

### 5. Live MCP Execution & Evidence
Three tool-use tasks that a plain LLM chat cannot perform without MCP, each with invocation payload and executed output:

1. `read_file` — direct local filesystem read of `package.json`
2. `git_status` — live git repository status & commit log query
3. `write_file` — real-time local disk mutation of `README.md`

## Usage

Open `index.html` directly in any modern browser — no dependencies, no build step required.

```bash
open index.html   # macOS
# or just double-click the file
```

## Tech Stack

- Vanilla HTML / CSS / JavaScript (single file, no frameworks)
- Dark developer theme: `#090d16` canvas, `#131c2e` surfaces, `#38bdf8` cyan & `#818cf8` indigo accents
- Inter (prose) + JetBrains Mono (code/terminal)
