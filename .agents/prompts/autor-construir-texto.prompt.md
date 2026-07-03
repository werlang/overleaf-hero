# Construir corpo de texto como autor

Use quando o usuario for o autor e quiser ajuda para escrever ou expandir secoes do trabalho.

## Papel

Ajude a planejar e redigir texto academico em LaTeX. Use `overleaf-tcc-workflow`, `scientific-writing`, `research-mentor`, `academic-latex`, `academic-source-discovery` e `bibtex-verified-citations`.

## Procedimento

1. Aplicar `overleaf-tcc-workflow` antes de qualquer escrita em arquivo.
2. Se `project/tcc.tex` nao existir, nao editar arquivos, nao usar `template/` ou `sample*` como substituto; entregar rascunho em chat ou perguntar pelo arquivo de destino.
3. Identificar arquivo-alvo, secao existente ou nova secao, estagio do trabalho, objetivo da secao, fatos conhecidos, evidencias disponiveis e lacunas.
4. Preferir inserir texto em arquivo ja incluido por `project/tcc.tex`; criar arquivo novo somente quando o usuario pedir novo capitulo, apendice ou pre-textual, atualizando tambem o `\input` correspondente.
5. Escrever em PT-BR academico, formal e impessoal, usando `\chapter`, `\section`, `\subsection`, `\label`, `\ref` e `\cite` conforme o padrao existente.
6. Usar `academic-source-discovery` apenas para fontes candidatas; fonte candidata nao entra em `references.bib` nem vira `\cite`.
7. Para cada citacao nova, usar `bibtex-verified-citations`; inserir BibTeX e `\cite` somente se o suporte for `Supported` e atualizar `project/citation-cheatsheet.md`.
8. Quando faltar evidencia, marcar lacuna explicita como `% PENDENTE: fonte/evidencia para ...`, nunca chave BibTeX falsa.
9. Manter texto compativel com o template LaTeX e nao escrever resultados como realizados quando o autor forneceu apenas plano.

## Saida

Informe arquivo-alvo, se a secao e nova ou existente, texto entregue ou alterado, lacunas de evidencia, citacoes verificadas, fontes apenas candidatas e validacoes executadas ou bloqueadas. Se nao houver base suficiente, entregar esqueleto, perguntas objetivas e lacunas de evidencia.
