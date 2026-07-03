# Overleaf Hero - Copilot Instructions

This repository uses `.agents` as the canonical location for project agent guidance.

Read these files first:

- `AGENTS.md`
- `.agents/skills/overleaf-tcc-workflow/SKILL.md`

Then choose the prompt that matches the user's role:

- `.agents/prompts/autor-revisar-trabalho.prompt.md`
- `.agents/prompts/autor-construir-texto.prompt.md`
- `.agents/prompts/orientador-corrigir-trabalho.prompt.md`
- `.agents/prompts/avaliador-corrigir-trabalho.prompt.md`

Core rules:

- Work in `project/` for the active TCC.
- Fresh checkouts may have an empty `project/`; if `project/tcc.tex` is missing, stop and report that no active TCC is loaded.
- Do not infer active thesis content from `template/` or `sample*`.
- Never edit `template/` or `sample*`.
- Do not edit LaTeX configuration files unless explicitly requested.
- New citations require online verification through `bibtex-verified-citations` and an entry in `project/citation-cheatsheet.md`.
- Use `python3 -B tools/check_cites.py` for citation validation.
- Advisor mode comments and recommends by default; edit only requested formal corrections.
- Evaluator mode produces a review by default and does not edit files unless requested.
