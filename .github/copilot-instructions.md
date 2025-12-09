# Overleaf Hero - AI Agent Instructions

## Project Overview

This workspace is designed for **systematic academic review of Brazilian thesis/dissertation LaTeX projects** (TCCs, dissertations, articles). It provides a structured environment with templates, reference samples, and detailed revision workflows for AI agents to perform comprehensive academic paper reviews.

## Directory Structure & Critical Boundaries

```
overleaf-hero/
├── template/           # Base LaTeX template - NEVER MODIFY
├── sample*/            # Reference projects (sample/, sample00/, sample01/) - NEVER MODIFY
├── project/            # Active work area - WORK ONLY HERE
├── prompt.md           # Complete revision instructions (READ FIRST)
└── README.md           # User-facing documentation
```

**CRITICAL**: Never modify files in `template/` or any `sample*` directories. All edits must be in `project/`.

## Architecture & Workflow Philosophy

### Three-Phase Revision Model

1. **Discovery Phase**: Map all `.tex` files, understand structure, create todo-list with `manage_todo_list`
2. **Systematic Revision**: Process each chapter sequentially (mark in-progress → edit → mark completed)
3. **Validation Phase**: Run `get_errors`, verify consistency, confirm completion

### Key Design Principle: "Preserve the Author's Voice"

- **Minimal intervention**: Correct errors, don't rewrite content
- **Direct application**: Apply fixes immediately using `multi_replace_string_in_file` for efficiency
- **No reports**: Unless explicitly requested, apply corrections silently without generating summary markdown files

## Essential Workflows

### Starting a Revision Request

```
1. Read prompt.md (397 lines of detailed instructions)
2. file_search: "**/*.tex" to map all LaTeX files
3. manage_todo_list: Create ~10 tasks (pretextuais, capitulo1-6, apendices, validation)
4. Execute systematically, marking progress after each step
```

### Applying Corrections

**DO**: Use `multi_replace_string_in_file` for parallel edits across multiple files
**DON'T**: Make sequential `replace_string_in_file` calls when edits are independent
**DON'T**: Stop mid-revision - complete ALL files before finishing

### Common Correction Patterns (from prompt.md)

```latex
# Grammar fixes (Brazilian Portuguese academic style)
"através de" → "por meio de"
"Nós implementamos" → "Foi implementado"
"muito importante" → specific technical term

# LaTeX formatting
back-end → \textit{back-end}  # Italicize foreign terms
"texto" → `texto'              # LaTeX quotes
Add \centerline{{Fonte: ...}} to all figures

# ABNT compliance
All figures need: \caption{}, \label{}, and Fonte
All tables need: \caption{}, \label{}, and footnotesize source
```

## Project-Specific Conventions

### LaTeX Document Class

Uses custom `tcc.cls` based on UFRGS (Federal University of Rio Grande do Sul) standards. Key features:
- Custom citation commands: `\apud{orig}{p1}{cons}{p2}` for indirect citations
- Table checkmarks: `\ticV` (✔) and `\ticX` (✘) for comparison tables
- Minted package for code highlighting: `\jsoncode`, `\jscode`, `\htmlcode`

### Mandatory Structural Elements (Chapter Checklist)

**Chapter 1 (Introdução)**: Must have context, problem statement (often italicized), general + specific objectives, document roadmap

**Chapter 3 (Trabalhos Relacionados)**: **MUST include comparative table** using `\ticV`/`\ticX` to compare related work features vs. proposed solution

**Pretextuais**: Resumo and Abstract must be aligned, max 500 words, same structure, NO citations in resumo

### Terminology Consistency

Track technical terms across ALL `.tex` files and standardize:
- Foreign terms: always `\textit{term}` (e.g., `\textit{backup}`, `\textit{offline}`)
- Acronyms: First use spelled out, subsequent uses just acronym
- Compound terms: Decide singular form and enforce everywhere

## Tool Usage Patterns

### Critical Tools for This Workflow

1. **`file_search`**: Always start with `**/*.tex` to map project structure
2. **`read_file`**: Read large ranges (50-100 lines) to get full context; avoid many small reads
3. **`multi_replace_string_in_file`**: Preferred for applying multiple fixes efficiently
4. **`manage_todo_list`**: REQUIRED for tracking revision progress - update after each chapter
5. **`grep_search`**: Validate consistency (e.g., find all instances of term to check formatting)
6. **`get_errors`**: Final validation step to catch LaTeX compilation issues

### Validation Searches (from prompt.md)

```regex
# Run these grep searches on project/**/*.tex at validation phase:
"através de|atraves"           # Common grammar error
"back-end|front-end|offline"   # Check for missing \textit{}
"  +"                          # Find double spaces
"foi realizados|foram realizado" # Verb agreement errors
```

## Integration Points

### External Dependencies

- LaTeX packages: `minted` (code), `hyperref` (links), `graphicx` (images), `appendix` (appendices)
- Bibliography: BibTeX with `abnt-ufrgs.bst` style for ABNT formatting
- Custom commands defined in `iidefs.sty` and document preamble

### Cross-Component Communication

- Main file (`tcc.tex`) uses `\include{}` to load chapters and sections
- References: `references.bib` shared across all chapters
- Labels/refs: Chapters cross-reference using `\ref{fig:label}`, `\ref{tab:label}`

## Common Pitfalls & Solutions

### Pitfall: Stopping Mid-Revision
**Solution**: Use `manage_todo_list` to track ALL chapters upfront. Never finish until all tasks marked completed.

### Pitfall: Over-Rewriting Author's Content
**Solution**: Only fix objective errors (grammar, formatting, ABNT). Don't change argumentative structure or technical content.

### Pitfall: Sequential Edits When Parallel Is Possible
**Solution**: Batch all independent corrections in one `multi_replace_string_in_file` call.

### Pitfall: Missing Sample Context
**Sample directories are TEXT ONLY** - images were removed. Don't expect visual references from samples.

## Special Scenarios

### TCC 1 vs TCC 2 vs Article

- **TCC 1** (Proposal): Needs chronogram, partial results, future steps
- **TCC 2** (Final): Complete results, full discussion, definitive conclusion
- **Article**: More concise, stronger statistical analysis, comparative discussion

Adjust revision expectations based on document type (check `\documentclass` options in `tcc.tex`).

## Quick Reference Commands

```bash
# Map project structure
file_search: "project/**/*.tex"

# Validate common errors
grep_search: "através de" (isRegexp: false, includePattern: "project/**/*.tex")

# Check LaTeX compilation
get_errors with filePaths: ["project/tcc.tex"]
```

## Success Criteria

Revision is complete when:
- ✅ All `.tex` files in `project/` reviewed
- ✅ Todo-list 100% completed
- ✅ No files in `template/` or `sample*/` modified
- ✅ `get_errors` shows no compilation issues
- ✅ Confirmation message sent: "Revisão completa concluída! ✓"
