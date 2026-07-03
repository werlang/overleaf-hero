# Revisar trabalho como autor

Use quando o usuario for o autor e pedir revisao, correcao, polimento ou verificacao final do texto.

## Papel

Aplique diretamente apenas correcoes objetivas, locais e formais em `project/`, preservando a voz do autor. Use `overleaf-tcc-workflow`, `scientific-proofreading`, `academic-latex` e `bibtex-verified-citations`. O modo padrao e `moderada`, salvo pedido por revisao `minima` ou `critica`.

## Fronteira de intervencao

- Pode aplicar: ortografia, gramatica, pontuacao, coesao local, terminologia, LaTeX, labels, refs e formatacao formal.
- Deve devolver ao autor: argumento, metodo, escopo, resultados, interpretacao, contribuicao, limitacoes e novas evidencias.
- Em modo somente leitura ou quando o usuario pedir apenas parecer, nao editar arquivos.

## Procedimento

1. Verificar se `project/tcc.tex` existe; se nao existir, parar, informar projeto nao inicializado e nao usar `template/` ou `sample*` como conteudo revisavel.
2. Ler `project/tcc.tex` e mapear apenas arquivos incluidos.
3. Classificar cada achado como `correcao aplicada`, `pendencia do autor` ou `decisao academica`.
4. Revisar pre-textuais, capitulos e apendices ativos de forma incremental.
5. Corrigir ortografia, gramatica, coesao local, terminologia e LaTeX sem mudar sentido tecnico.
6. Nao alterar `template/`, `sample*` ou configuracoes LaTeX.
7. Nao adicionar citacoes sem verificacao online e cheatsheet.
8. Rodar validacoes disponiveis ao final e listar validacoes puladas com motivo.

## Saida

```markdown
## Revisao do Autor

## Modo e Escopo

## Arquivos Revisados ou Alterados

## Correcoes Aplicadas

## Pendencias do Autor

## Decisoes Academicas Nao Tomadas

## Validacoes Executadas ou Bloqueadas
```
