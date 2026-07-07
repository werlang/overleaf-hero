# Overleaf Hero - Agent Guide

Este workspace apoia revisao, orientacao, avaliacao e escrita de TCCs em LaTeX. A fonte canonica de comportamento dos agentes fica em `.agents/`.

## Limites Obrigatorios

- Nunca editar `template/`.
- Nunca editar `sample*`.
- Nao editar `.cls`, `.sty`, `.def` ou `.bst` salvo pedido explicito.
- Trabalhar em `project/` quando o usuario pedir mudancas no TCC atual.
- Nao inserir citacoes novas sem verificacao online e registro em `project/citation-cheatsheet.md`.

## Estrutura Esperada

- `project/tcc.tex`: arquivo principal quando o TCC estiver carregado.
- `project/pretextuais/`: resumo, abstract e listas.
- `project/capitulo*/`: capitulos do trabalho.
- `project/apendices/`: apendices.
- `project/references.bib`: bibliografia do projeto.
- `.agents/skills/`: skills canonicas.
- `.agents/prompts/`: prompts por papel do usuario.
- `tools/`: scripts auxiliares.

## Skills Canonicas

- `overleaf-tcc-workflow`: fluxo do workspace e limites de edicao.
- `scientific-writing`: escrita de texto cientifico.
- `academic-latex`: sintaxe LaTeX, ABNT, figuras, tabelas e refs.
- `scientific-proofreading`: revisao textual preservando voz do autor.
- `academic-peer-review`: parecer de avaliador/banca.
- `research-mentor`: feedback de orientador.
- `bibtex-verified-citations`: BibTeX e citacoes com verificacao obrigatoria.
- `academic-source-discovery`: busca e triagem de fontes candidatas.

## Prompts por Papel

- Autor revisando: `.agents/prompts/autor-revisar-trabalho.prompt.md`.
- Autor escrevendo: `.agents/prompts/autor-construir-texto.prompt.md`.
- Orientador: `.agents/prompts/orientador-corrigir-trabalho.prompt.md`.
- Avaliador: `.agents/prompts/avaliador-corrigir-trabalho.prompt.md`.

## Fluxo Padrao

1. Identificar o papel do usuario.
2. Verificar se `project/tcc.tex` existe.
3. Se `project/tcc.tex` nao existir, parar, reportar projeto nao inicializado e nao usar `template/` ou `sample*` como substituto.
4. Ler `project/tcc.tex` e mapear os arquivos realmente incluidos.
5. Selecionar as skills adequadas.
6. Para autor, aplicar correcoes diretas objetivas quando solicitado e separar decisoes academicas como pendencias.
7. Para orientador, entregar diagnostico com evidencias, perguntas ao autor e decisoes que o agente nao deve tomar.
8. Para avaliador, produzir parecer por padrao, declarar nivel TCC1/TCC2 ou `nivel nao determinado`, e nao editar arquivos.
9. Rodar validacoes aplicaveis antes de finalizar.

## Politica de Citacoes

Toda citacao nova deve passar por `bibtex-verified-citations`:

- pesquisar fonte na internet;
- confirmar metadados;
- comparar a fonte com a afirmacao especifica;
- inserir somente se o suporte for `Supported`;
- atualizar `project/citation-cheatsheet.md`;
- rodar `python3 -B tools/check_cites.py`.

Se nao houver internet ou acesso suficiente, bloqueie a insercao e diga por que.

## Validacao

Antes de finalizar mudancas em docs, skills ou scripts:

```bash
python3 -B -m py_compile tools/check_cites.py tools/extract_papers.py tools/review_papers.py tools/pdf_to_text.py tools/render_pdf_pages.py
python3 -B tools/check_cites.py
git diff --check
```

`python3 -B tools/check_cites.py` deve sair sem erro em projeto vazio e falhar quando houver citacao sem BibTeX, sem cheatsheet valido ou sem `Status == Supported`. Quando revisar texto LaTeX, tambem confira se `template/` e `sample*` permanecem intocados. Compilacao TeX e opcional: se `latexmk`, `pdflatex`, `xelatex` ou `tectonic` nao estiverem disponiveis, declare essa limitacao.
