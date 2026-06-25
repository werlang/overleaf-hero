---
name: overleaf-tcc-workflow
description: Workflow especifico do workspace Overleaf Hero para revisar, orientar ou avaliar TCCs em LaTeX. Use quando trabalhar no diretorio project/, mapear tcc.tex, preservar template/sample*, aplicar prompts de autor/orientador/avaliador e coordenar as skills academicas do projeto.
---

# Overleaf TCC Workflow

Use esta skill para qualquer tarefa neste workspace que envolva `project/`.

## Estrutura canonica

- `template/`: modelo base. Nunca editar.
- `sample*`: exemplos textuais. Nunca editar.
- `project/`: trabalho atual. Editar aqui quando o usuario pedir alteracoes.
- `.agents/skills`: skills canonicas do projeto.
- `.agents/prompts`: prompts por papel do usuario.

## Antes de editar

1. Ler `project/tcc.tex`.
2. Identificar arquivos ativos por `\input` ou `\include`.
3. Mapear pre-textuais, capitulos e apendices.
4. Identificar papel do usuario: autor, orientador ou avaliador.
5. Selecionar skills complementares:
   - autor escrevendo: `scientific-writing`, `research-mentor`, `bibtex-verified-citations`.
   - autor revisando: `scientific-proofreading`, `academic-latex`, `bibtex-verified-citations`.
   - orientador: `research-mentor`, `scientific-proofreading`, `academic-latex`.
   - avaliador: `academic-peer-review`, `academic-latex`, `bibtex-verified-citations` quando houver auditoria de citacoes.

## Regras de edicao

- Nao alterar `template/` nem `sample*`.
- Nao alterar arquivos de configuracao LaTeX salvo pedido explicito.
- Nao editar argumentacao de fundo sem consentimento quando estiver no papel de orientador ou avaliador.
- Para o autor, aplicar correcoes diretas quando a solicitacao for de revisao.
- Para avaliador, gerar parecer por padrao e nao editar arquivos.

## Checklist estrutural

- Resumo sem citacoes e com ate 500 palavras.
- Abstract alinhado ao resumo.
- Introducao com contexto, problema, objetivo geral, objetivos especificos e organizacao.
- Fundamentacao com conceitos usados depois no trabalho.
- Trabalhos relacionados com analise critica e comparacao.
- Metodologia/desenvolvimento reproduzivel.
- Resultados alinhados aos objetivos.
- Conclusao com contribuicoes, limitacoes e trabalhos futuros.
- Figuras e tabelas com caption, label e fonte.
- Citacoes verificadas quando forem novas ou auditadas.

## Validacao final

- Rodar buscas textuais de `academic-latex` e `scientific-proofreading`.
- Rodar `python tools/check_cites.py`.
- Se houver ambiente TeX, compilar o projeto; se nao houver, declarar essa limitacao.
- Confirmar que `template/` e `sample*` nao foram modificados.
