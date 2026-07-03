---
name: academic-source-discovery
description: Busca e triagem de fontes academicas para TCCs e artigos. Use para encontrar trabalhos relacionados, fontes recentes, referencias primarias, PDFs, DOI, metadados, lacunas de pesquisa e candidatos a citacao antes da verificacao com bibtex-verified-citations.
---

# Academic Source Discovery

Use esta skill para encontrar fontes. Ela nao autoriza citacao automaticamente; toda citacao nova deve passar por `bibtex-verified-citations`. Em modo avaliador, descoberta de fontes produz apenas candidatas e nao conserta citacoes existentes sem autorizacao explicita.

## Workflow

1. Extrair palavras-chave do tema, problema, metodo, tecnologia e dominio.
2. Buscar em fontes academicas e tecnicas confiaveis: bases cientificas, DOI, arXiv, Semantic Scholar, paginas de eventos, periodicos e documentacao oficial quando for fonte tecnica.
3. Priorizar fontes primarias sobre blogs, slides ou resumos de terceiros.
4. Registrar candidatos com titulo, autores, ano, URL/DOI, motivo de relevancia e afirmacao que poderiam sustentar.
5. Separar fonte candidata de fonte verificada.

## Ranking pratico

Classificar relevancia considerando:

- aderencia ao problema do trabalho;
- correspondencia de metodo ou tecnologia;
- qualidade e tipo da fonte;
- atualidade, quando o tema for tecnologico;
- acesso ao texto suficiente para verificacao posterior;
- utilidade para fundamentacao, metodologia ou trabalhos relacionados.

## Saida recomendada

```markdown
## Fontes candidatas

| Prioridade | Fonte | Ano | URL | Uso possivel | Observacao |
|---|---|---:|---|---|---|
| Alta | ... | 2024 | https://... | Fundamentar conceito X | Candidata; requer verificacao claim-source |
```

Quando separar status, use:

- `Candidata`: pode ser util, mas ainda nao foi verificada contra uma afirmacao especifica.
- `Verificada: Supported`: passou por `bibtex-verified-citations` e pode ser usada.
- `Rejeitada` ou `Uncertain`: nao deve entrar em `references.bib` nem no texto.

## Cuidados

- Nao apresentar contagem de citacoes como prova de qualidade sem verificar a origem.
- Nao baixar ou anexar PDF paywalled sem autorizacao.
- Nao inferir resultado a partir apenas do titulo.
- Nao inserir fonte candidata em `project/references.bib`.
- Quando o usuario pedir insercao no texto, passar para `bibtex-verified-citations`.
