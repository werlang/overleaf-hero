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
2. Ler `project/tcc.tex` e os arquivos incluidos para avaliar o trabalho real.
3. Avaliar estrutura, rigor, clareza, metodo, resultados, referencias e conformidade formal.
4. Registrar evidencias por arquivo e linha aproximada ou secao.
5. Separar problemas impeditivos, problemas importantes e melhorias opcionais.
6. Se houver rubrica, aplicar a rubrica do usuario; se nao houver, usar criterios qualitativos.

## Severidade

- `Critico`: compromete aprovacao, sentido, metodo, evidencia, compilacao ou integridade academica.
- `Alto`: erro relevante de estrutura, argumentacao, citacao, resultado ou norma.
- `Medio`: clareza, completude, comparacao, justificativa ou coesao melhoravel.
- `Baixo`: estilo, pequenos ajustes, consistencia fina ou polimento.

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

## Formato de parecer

```markdown
# Parecer Academico

## Sintese
[avaliacao geral em um paragrafo]

## Decisao ou Classificacao
[aprovado, aprovado com ajustes, revisar profundamente, ou classificacao solicitada]

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
- Quando precisar verificar citacao, usar `bibtex-verified-citations`.
