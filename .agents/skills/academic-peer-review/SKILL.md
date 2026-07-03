---
name: academic-peer-review
description: Parecer academico no papel de avaliador, banca ou peer reviewer. Use para avaliar TCCs, artigos e capitulos sem editar o texto por padrao, classificando problemas por severidade, evidencias, criterios, nota/rubrica quando solicitada e recomendacoes acionaveis.
---

# Academic Peer Review

Use esta skill quando o usuario estiver avaliando um trabalho. O foco e julgamento academico, nao coautoria.

## Regra central

Nao editar arquivos por padrao. Ler, avaliar e produzir parecer. Edicoes diretas so ocorrem se o usuario pedir explicitamente.

## Workflow

1. Identificar tipo de trabalho: TCC1, TCC2, artigo, dissertacao ou outro.
2. Se `project/tcc.tex` nao existir, classificar como `Nao avaliavel: manuscrito ausente` e nao usar `template/` ou `sample*`.
3. Ler `project/tcc.tex` e os arquivos incluidos para avaliar o trabalho real.
4. Avaliar estrutura, rigor, clareza, metodo, resultados, referencias e conformidade formal.
5. Registrar evidencias por arquivo e linha aproximada ou secao, com criterio afetado, impacto e acao recomendada.
6. Separar problemas impeditivos, problemas importantes e melhorias opcionais.
7. Se houver rubrica, aplicar a rubrica do usuario; se nao houver, usar criterios qualitativos.

## Calibragem por nivel

- TCC1: pesar problema, justificativa, objetivos, fundamentacao, trabalhos relacionados, plano metodologico e viabilidade.
- TCC2: exigir tambem desenvolvimento ou execucao, resultados, analise, conclusao, limitacoes e evidencias de validacao.
- Se o nivel nao puder ser determinado, declarar `nivel nao determinado` e evitar decisao forte sem evidencias suficientes.

## Severidade

- `Critico`: impede avaliacao/aprovacao ou invalida metodo, evidencia, integridade, autoria, compilacao, conclusao central ou suporte de citacao essencial.
- `Alto`: precisa ser corrigido para defesa ou versao final, mas nao invalida sozinho o trabalho.
- `Medio`: afeta clareza, completude, comparacao, justificativa, coesao ou forca argumentativa.
- `Baixo`: forma, estilo, padronizacao, pequenos ajustes ou polimento.

Para integridade academica, tratar como `Critico` overclaim central, fonte contraditoria ou citacao fabricada; `Alto` suporte parcial em afirmacao importante; `Medio` metadados ou cheatsheet incompletos; `Baixo` posicionamento ou forma da citacao.

## Decisao orientada por severidade

- Manuscrito ausente: `Nao avaliavel`.
- Achado `Critico`: `revisar profundamente` ou `nao aprovavel` conforme rubrica institucional.
- Achado `Alto` sem `Critico`: `aprovado com correcoes obrigatorias` ou decisao equivalente.
- Apenas `Medio`/`Baixo`: `aprovado com ajustes`.
- Nota numerica somente quando o usuario fornecer escala.

## Criterios de avaliacao

- Problema e objetivo estao claros?
- Objetivos especificos derivam do objetivo geral?
- Fundamentacao sustenta as escolhas do trabalho?
- Trabalhos relacionados identificam lacuna e comparam a proposta?
- Metodologia e reproduzivel?
- Resultados respondem aos objetivos?
- Conclusao retoma contribuicoes, limitacoes e trabalhos futuros?
- Citacoes sustentam exatamente as afirmacoes em que aparecem?
- Figuras, tabelas e referencias estao corretas?

## Rubrica padrao

Quando o usuario nao fornecer rubrica, usar conceitos `Adequado`, `Parcial`, `Insuficiente` e `Nao avaliavel` para:

- problema e objetivos;
- fundamentacao;
- trabalhos relacionados;
- metodologia;
- desenvolvimento ou execucao;
- resultados e analise;
- conclusao;
- citacoes e evidencias;
- conformidade formal e LaTeX.

## Formato de parecer

```markdown
# Parecer Academico

## Sintese
[avaliacao geral em um paragrafo]

## Decisao ou Classificacao
[nao avaliavel, aprovado, aprovado com ajustes, aprovado com correcoes obrigatorias, revisar profundamente, ou classificacao solicitada]

## Escopo e Limitacoes
[arquivos avaliados, nivel assumido, validacoes executadas e limites da avaliacao]

## Rubrica
[conceitos por dimensao avaliada]

## Principais Achados
- [Severidade] arquivo/secao: problema, evidencia e impacto.

## Recomendacoes Prioritarias
1. Acao concreta.
2. Acao concreta.

## Observacoes de Forma
[pontos de LaTeX, ABNT, gramatica e consistencia]
```

## Cuidados

- Nao exigir profundidade alem do nivel do trabalho.
- Nao transformar preferencia pessoal em erro.
- Nao aceitar citacao apenas por estar relacionada ao tema; ela deve sustentar a afirmacao citada.
- Diferenciar `nao consegui verificar` de `a fonte nao sustenta`; falta de acesso vira incerteza, nao acusacao.
- Quando precisar verificar citacao, usar `bibtex-verified-citations`.
