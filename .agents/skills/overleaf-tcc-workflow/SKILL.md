---
name: overleaf-tcc-workflow
description: Workflow especifico do workspace Overleaf Hero para revisar, orientar ou avaliar TCCs em LaTeX. Use quando trabalhar no diretorio project/, mapear tcc.tex, preservar template/sample*, aplicar prompts de autor/orientador/avaliador e coordenar as skills academicas do projeto.
---

# Overleaf TCC Workflow

Use esta skill para qualquer tarefa neste workspace que envolva `project/`.

## Estrutura canonica

- `template/`: modelo base. Nunca editar.
- `sample*`: exemplos textuais. Nunca editar.
- `project/`: trabalho atual quando estiver inicializado. Editar aqui quando o usuario pedir alteracoes.
- `.agents/skills`: skills canonicas do projeto.
- `.agents/prompts`: prompts por papel do usuario.

## Projeto vazio ou nao inicializado

Antes de revisar, orientar, avaliar ou editar, verificar se `project/tcc.tex` existe.

Se `project/tcc.tex` nao existir:

- nao revisar nem editar arquivos;
- nao copiar, revisar ou inferir conteudo a partir de `template/` ou `sample*`;
- reportar que o projeto nao contem TCC ativo carregado;
- pedir ao usuario para inserir o trabalho em `project/` ou informar explicitamente outro arquivo de destino;
- marcar `check_cites`, buscas em `project/**/*.tex` e compilacao LaTeX como nao aplicaveis.

## Antes de revisar ou editar

1. Confirmar que `project/tcc.tex` existe.
2. Ler `project/tcc.tex`.
3. Identificar arquivos ativos por `\input` ou `\include`.
4. Mapear pre-textuais, capitulos e apendices.
5. Identificar papel do usuario: autor, orientador ou avaliador.
6. Selecionar skills complementares:
   - autor escrevendo: `scientific-writing`, `research-mentor`, `academic-latex`, `academic-source-discovery`, `bibtex-verified-citations`.
   - autor revisando: `scientific-proofreading`, `academic-latex`, `bibtex-verified-citations`.
   - orientador: `research-mentor`, `scientific-proofreading`, `academic-latex`, `bibtex-verified-citations` quando houver nova citacao, auditoria de citacao ou recomendacao que dependa de fonte.
   - avaliador: `academic-peer-review`, `academic-latex`, `bibtex-verified-citations` quando houver auditoria de citacoes.

## Regras de edicao

- Nao alterar `template/` nem `sample*`.
- Nao alterar arquivos de configuracao LaTeX salvo pedido explicito.
- Nao editar argumentacao, metodo, resultados, contribuicao ou citacoes sem consentimento explicito quando estiver no papel de orientador ou avaliador.
- Para o autor, aplicar correcoes textuais/formais diretas quando solicitado; mudancas de argumento, metodo, escopo, resultados ou contribuicao ficam como pendencia do autor.
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

## Calibragem TCC1/TCC2

- TCC1: pesar mais problema, justificativa, objetivos, fundamentacao, trabalhos relacionados e plano metodologico.
- TCC2: exigir tambem desenvolvimento, resultados, analise, conclusao, limitacoes e evidencias de validacao.
- Quando o nivel nao estiver claro, declarar `nivel nao determinado` em pareceres e orientar o usuario a informar o contexto.

## Validacao final

- Rodar buscas textuais de `academic-latex` e `scientific-proofreading` somente quando houver arquivos ativos em `project/`.
- Rodar `python3 -B tools/check_cites.py`.
- Se houver ambiente TeX, compilar o projeto; se nao houver, declarar essa limitacao.
- Confirmar que `template/` e `sample*` nao foram modificados, por exemplo com `git diff --name-only -- template sample00 sample01`.
