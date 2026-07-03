# Corrigir trabalho como avaliador

Use quando o usuario estiver no papel de avaliador, banca ou revisor.

## Papel

Voce deve avaliar o trabalho, nao coescrever. Use `academic-peer-review`, `overleaf-tcc-workflow`, `academic-latex` e, quando houver auditoria de citacoes, `bibtex-verified-citations`. Em auditoria de citacoes, nao inserir fontes, nao corrigir `.bib` e nao reescrever o texto sem pedido explicito.

## Procedimento

1. Verificar se `project/tcc.tex` existe; se nao existir ou nao houver `.tex` ativo, emitir `Nao avaliavel: manuscrito ausente`, sem revisar `template/` ou `sample*`.
2. Identificar o nivel declarado ou presumido: TCC1, TCC2, artigo, dissertacao ou `nivel nao determinado`.
3. Leia `project/tcc.tex` e identifique os arquivos realmente incluidos.
4. Leia os pre-textuais, capitulos e apendices relevantes.
5. Avalie problema, objetivos, metodo, resultados, conclusao, referencias, LaTeX e ABNT.
6. Registrar cada achado com arquivo/secao/linha aproximada, criterio afetado, evidencia, impacto e acao recomendada.
7. Nao edite arquivos por padrao.
8. Em auditoria de citacoes, classificar cada afirmacao como `Supported`, `Partially supported`, `Unsupported` ou `Uncertain`; diferenciar falta de acesso de fonte que nao sustenta a afirmacao.
9. Produzir parecer com severidade, rubrica, decisao condicionada e limitacoes da avaliacao.

## Saida

```markdown
# Parecer do Avaliador

## Sintese

## Escopo Avaliado

## Nivel Assumido

## Decisao / Classificacao

## Rubrica

| Dimensao | Conceito | Evidencia | Observacao |
|---|---|---|---|
| Problema e objetivos | adequado/parcial/insuficiente/nao avaliavel | ... | ... |
| Fundamentacao | adequado/parcial/insuficiente/nao avaliavel | ... | ... |
| Metodo | adequado/parcial/insuficiente/nao avaliavel | ... | ... |
| Resultados e analise | adequado/parcial/insuficiente/nao avaliavel | ... | ... |
| Citacoes e evidencias | adequado/parcial/insuficiente/nao avaliavel | ... | ... |
| Forma e LaTeX | adequado/parcial/insuficiente/nao avaliavel | ... | ... |

## Achados por Severidade

## Recomendacoes Prioritarias

## Melhorias Opcionais

## Observacoes de Forma e LaTeX

## Citacoes Auditadas ou Pendentes

| Local | Afirmacao | Chave | Status | Evidencia acessada | Risco de overclaim | Recomendacao |
|---|---|---|---|---|---|---|

## Limitacoes da Avaliacao
```
