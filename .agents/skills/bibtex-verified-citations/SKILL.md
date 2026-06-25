---
name: bibtex-verified-citations
description: Gerenciamento de BibTeX com verificacao obrigatoria de citacoes na internet. Use para inserir, auditar ou corrigir referencias em .bib e no texto, garantindo que a fonte consultada sustente a afirmacao citada e registrando URL/evidencia em project/citation-cheatsheet.md.
---

# BibTeX Verified Citations

Use esta skill sempre que uma nova referencia ou citacao for inserida, removida, auditada ou corrigida.

## Regra de ouro

So inserir uma citacao no `.bib` e no corpo do texto quando a fonte estiver verificada como `Supported` para a afirmacao especifica que ela sustenta.

Se nao houver internet, acesso ao texto, metadados confiaveis ou correspondencia clara entre fonte e afirmacao, bloquear a insercao e informar o motivo.

## Protocolo de verificacao

1. Isolar a afirmacao exata que recebera a citacao.
2. Pesquisar na internet por fontes primarias ou confiaveis: DOI, pagina do periodico/conferencia, arXiv, repositório institucional, Semantic Scholar, Crossref, site oficial ou PDF do autor.
3. Confirmar metadados: titulo, autores, ano, venue, DOI/URL.
4. Ler resumo, introducao, conclusao e, quando necessario, a secao relevante.
5. Comparar a fonte com a afirmacao, sem inferencias amplas.
6. Classificar o suporte.
7. Inserir no `.bib` e no texto apenas se o status for `Supported`.
8. Atualizar `project/citation-cheatsheet.md` na mesma mudanca.
9. Rodar `python tools/check_cites.py`.

## Classificacao de suporte

- `Supported`: a fonte afirma, demonstra ou mede exatamente o ponto usado no texto, com contexto compativel.
- `Partially supported`: a fonte apoia parte da afirmacao, mas o texto esta amplo, impreciso ou extrapolado.
- `Unsupported`: a fonte nao sustenta a afirmacao, contradiz o texto ou trata de outro contexto.
- `Uncertain`: metadados ou texto completo nao foram acessiveis o bastante para verificar.

Somente `Supported` pode virar citacao no texto. Para `Partially supported`, reformular a afirmacao e verificar novamente ou registrar como fonte candidata sem inserir.

## Cheatsheet obrigatorio

Criar ou atualizar `project/citation-cheatsheet.md` com uma tabela por referencia inserida:

```markdown
| BibTeX key | Status | Claim supported | Evidence summary | Source URL | Accessed at | Used in |
|---|---|---|---|---|---|---|
| silva2024dados | Supported | ... | ... | https://... | 2026-06-25 | project/capitulo2/capitulo2.tex |
```

Regras:

- Incluir URL consultavel pelo leitor.
- Resumir a evidencia em uma frase, sem longas citacoes literais.
- Registrar a data local da verificacao.
- Atualizar a linha existente se a mesma chave ja estiver no cheatsheet.
- Nao registrar fonte `Unsupported` como referencia usada; se necessario, criar uma secao `Fontes candidatas rejeitadas`.

## BibTeX

- Nao inventar DOI, paginas, editora, venue ou autores.
- Proteger siglas e nomes proprios no titulo com chaves: `{ALCOA++}`, `{Node.js}`.
- Preferir DOI e URL estavel quando disponiveis.
- Manter convencao de chave `sobrenomeANOtermo`, salvo padrao diferente no projeto.
- Nao remover entradas antigas sem conferir se ainda sao citadas.

## Insercao no texto

- Posicionar a citacao junto da afirmacao que ela sustenta.
- Nao usar uma fonte como decoracao de paragrafo.
- Se a fonte sustenta apenas uma definicao, nao usa-la para justificar resultado empirico.
- Se o texto exagera a fonte, corrigir o texto antes de citar.

## Know-how incorporado

Este protocolo se inspira em abordagens de verificacao de suporte entre afirmacao e citacao, como SemanticCite, CheckIfExist, ScholarCopilot e auditorias academicas de citacoes com postura zero-assumption: primeiro verificar a relacao claim-source, depois editar.
