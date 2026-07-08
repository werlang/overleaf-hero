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

O parecer de avaliação deve ser salvo no arquivo `project/parecer_avaliador.md`. O parecer deve ser altamente detalhado e estruturado da seguinte forma:

```markdown
# Parecer do Avaliador (Detalhamento Completo)

## Sintese
[Uma sintese robusta sobre o trabalho, destacando o tema, solucao proposta, pontos fortes e pontos fracos gerais.]

## Escopo Avaliado e Nivel Assumido
- **Manuscrito:** [Nome do arquivo PDF ou do arquivo principal LaTeX]
- **Texto Extraido:** [Caminho do arquivo txt, se aplicavel]
- **Nivel Assumido:** [TCC1, TCC2, Dissertacao, etc.]

## Decisao / Classificacao
[Decisao recomendada: Aprovado, Aprovado com correcoes obrigatorias, Nao Aprovado, etc., acompanhada de justificativa academica.]

## Rubrica Qualitativa

| Dimensao | Conceito | Evidencia | Observacoes e Paginas |
|---|---|---|---|
| Problema e objetivos | adequado/parcial/insuficiente/nao avaliavel | ... | ... |
| Fundamentacao | adequado/parcial/insuficiente/nao avaliavel | ... | ... |
| Trabalhos relacionados | adequado/parcial/insuficiente/nao avaliavel | ... | ... |
| Metodo | adequado/parcial/insuficiente/nao avaliavel | ... | ... |
| Resultados e analise | adequado/parcial/insuficiente/nao avaliavel | ... | ... |
| Citacoes e evidencias | adequado/parcial/insuficiente/nao avaliavel | ... | ... |
| Forma e LaTeX | adequado/parcial/insuficiente/nao avaliavel | ... | ... |

## Achados por Severidade e Detalhamento Técnico

Para cada achado registrado, forneça:
1. **Página(s) no PDF:** Local exato onde o problema ocorre.
2. **Descrição do Problema:** Descrição clara e direta do erro/inconsistência.
3. **Discussão Técnica e Acadêmica:** Discussão aprofundada mostrando o impacto teórico/técnico desse problema na qualidade do TCC (ex. impactos em reprodutibilidade, validade estatística, clareza científica).
4. **Sugestão de Adequação / Reescrita:** Sugestão concreta de texto de reescrita, correções de sintaxe LaTeX, modelos de tabelas ou orientações específicas para o autor adotar.

### Achados de Severidade Alta / Crítica
#### [Nome do Achado 1]
- **Página(s) no PDF:** ...
- **Descrição do Problema:** ...
- **Discussão Técnica e Acadêmica:** ...
- **Sugestão de Adequação / Reescrita:** ...

### Achados de Severidade Média
#### [Nome do Achado 1]
...

### Achados de Severidade Baixa (Revisão Textual e Formatação)
#### [Nome do Achado 1]
...

## Recomendacoes Prioritarias
1. [Acao prioritária 1]
2. [Acao prioritária 2]

## Citacoes Auditadas ou Pendentes (se aplicavel)
[Tabela de citacoes com Local, Afirmacao, Chave, Status, Evidencia acessada, Risco de overclaim e Recomendacao]

## Limitacoes da Avaliacao
[Explicitar as limitacoes de acesso do avaliador (ex: sem acesso ao codigo-fonte completo, sem execucao local do modelo, etc.)]
```


## Cuidados

- Nao exigir profundidade alem do nivel do trabalho.
- Nao transformar preferencia pessoal em erro.
- Nao aceitar citacao apenas por estar relacionada ao tema; ela deve sustentar a afirmacao citada.
- Diferenciar `nao consegui verificar` de `a fonte nao sustenta`; falta de acesso vira incerteza, nao acusacao.
- Quando precisar verificar citacao, usar `bibtex-verified-citations`.
