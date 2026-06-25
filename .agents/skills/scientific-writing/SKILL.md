---
name: scientific-writing
description: Escrita e reescrita de texto cientifico em LaTeX. Use para construir secoes academicas, transformar notas em parágrafos, melhorar argumentacao, estruturar introducao/fundamentacao/metodologia/resultados/conclusao, ou escrever corpo de texto preservando evidencias e voz do autor.
---

# Scientific Writing

Use esta skill para escrever texto academico em PT-BR por padrao. Use ingles somente quando o usuario pedir.

## Principios

- Escrever em LaTeX nativo, usando `\section`, `\subsection`, `\label`, `\ref` e `\cite` quando apropriado.
- Escrever com voz formal, objetiva e impessoal.
- Sustentar afirmacoes tecnicas, historicas, empiricas ou normativas com fonte verificavel.
- Nao inventar resultado, dado, citacao, autor, DOI ou ano.
- Preservar o escopo do trabalho: nao ampliar a promessa do autor para alem do que o metodo e os resultados permitem.
- Quando uma afirmacao nova exigir citacao, acionar `bibtex-verified-citations` antes de inserir a referencia no texto.

## Workflow

1. Identificar papel do usuario: autor, orientador ou avaliador.
2. Mapear objetivo da secao, leitor esperado e ponto que a secao deve provar.
3. Se a estrutura estiver fraca, propor primeiro um esqueleto em topicos.
4. Converter topicos em parágrafos curtos e coesos.
5. Marcar lacunas de evidencia em vez de preencher com citacoes nao verificadas.
6. Revisar transicoes, consistencia terminologica e aderencia ao objetivo da secao.

## Padroes por secao

### Introducao

Organizar como contexto, problema, lacuna, objetivo, contribuicoes e organizacao do trabalho. A questao de pesquisa deve ser explicita quando o texto estiver vago.

### Fundamentacao teorica

Definir conceitos centrais antes de usa-los. Evitar historico longo que nao volte ao problema de pesquisa. Cada conceito deve preparar uma decisao metodologica, uma comparacao ou uma interpretacao de resultados.

### Trabalhos relacionados

Agrupar por abordagem ou problema, nao apenas por autor. Encerrar com uma sintese que mostre a lacuna que justifica a proposta.

### Metodologia ou desenvolvimento

Escrever para reprodutibilidade: ferramentas, ambiente, dados, fluxo, criterio de escolha e limitacoes. Separar descricao do sistema de justificativa tecnica.

### Resultados

Apresentar evidencias, depois interpreta-las. Evitar resultado puramente narrativo quando uma tabela, quadro ou criterio de avaliacao for necessario.

### Conclusao

Retomar objetivos, sintetizar contribuicoes, reconhecer limitacoes e propor trabalhos futuros especificos.

## Qualidade textual

- Preferir `por meio de` a `atraves de` quando indicar meio.
- Evitar intensificadores vagos como `muito` e `bastante` sem medida.
- Evitar frases longas com muitas oracoes encadeadas.
- Manter o mesmo termo para o mesmo conceito ao longo do documento.
- Definir siglas no primeiro uso e depois usar a forma curta.

## Saida

Quando escrever diretamente em arquivo, alterar apenas arquivos permitidos pelo projeto. Quando o usuario pedir planejamento ou orientacao, entregar topicos acionaveis antes de redigir texto completo.
