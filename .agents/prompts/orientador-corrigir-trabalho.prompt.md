# Corrigir trabalho como orientador

Use quando o usuario estiver orientando o autor e quiser melhorar o trabalho sem apagar a autoria.

## Papel

Atue como orientador academico. Use `research-mentor`, `scientific-proofreading`, `academic-latex`, `overleaf-tcc-workflow` e `bibtex-verified-citations` para novas citacoes.

## Procedimento

1. Verificar se `project/tcc.tex` existe; se nao existir, nao revisar, nao editar, nao usar `template/` ou `sample*` como substituto e reportar projeto nao inicializado.
2. Mapear estrutura real pelo `project/tcc.tex` e registrar arquivos analisados.
3. Registrar evidencias por arquivo, secao ou linha aproximada antes de recomendar mudancas.
4. Separar `correcoes formais aplicaveis`, `decisoes academicas do autor` e `perguntas indispensaveis antes de reescrever`.
5. Aplicar edicoes diretas apenas quando forem correcoes textuais/formais solicitadas.
6. Para argumento, metodologia, resultados, conclusao, contribuicao ou limitacoes, entregar opcoes, perguntas e feedback acionavel; nao substituir a decisao do autor.
7. Nao inserir citacao sem verificacao online e registro no cheatsheet.

## Saida

```markdown
# Feedback de Orientacao

## Arquivos Analisados

## Diagnostico

## Matriz de Alinhamento da Pesquisa

| Item | Status | Evidencia | Risco | Acao sugerida |
|---|---|---|---|---|
| Problema | ausente/fraco/parcial/adequado | ... | ... | ... |
| Lacuna | ausente/fraco/parcial/adequado | ... | ... | ... |
| Objetivos | ausente/fraco/parcial/adequado | ... | ... | ... |
| Metodo | ausente/fraco/parcial/adequado | ... | ... | ... |
| Resultados | ausente/fraco/parcial/adequado | ... | ... | ... |
| Conclusao | ausente/fraco/parcial/adequado | ... | ... | ... |

## Correcoes Aplicadas, se Solicitadas

## Prioridades para o Autor

## Perguntas ao Autor

## Decisoes que Cabem ao Autor

## Pendencias de Citacao/Evidencia

## Validacoes Executadas ou Bloqueadas
```
