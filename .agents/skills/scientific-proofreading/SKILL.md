---
name: scientific-proofreading
description: Proofreading cientifico em PT-BR para TCCs, artigos e dissertacoes. Use para corrigir ortografia, gramatica, pontuacao, clareza, coesao, impessoalidade, terminologia e fluidez preservando a voz do autor e sem alterar conteudo tecnico.
---

# Scientific Proofreading

Use esta skill para revisar texto academico existente. Ela corrige, mas nao substitui a autoria do texto.

## Modos de intervencao

- `minima`: corrigir erros objetivos de ortografia, gramatica, pontuacao e LaTeX.
- `moderada`: modo padrao para autor; permite reescrita local de frase ou paragrafo curto para melhorar fluidez, conectivos e clareza sem mudar argumento, resultado ou voz autoral.
- `critica`: modo padrao para orientador/avaliador; comentarios primeiro, com correcoes formais locais apenas quando solicitadas.

Se o usuario nao escolher modo, usar `moderada` para autor e `critica` para orientador/avaliador.

## Workflow

1. Ler o arquivo inteiro antes de editar para entender voz, termos e contexto.
2. Mapear termos tecnicos e manter uma forma padrao.
3. Aplicar correcoes locais e incrementais.
4. Nao remover citacoes, dados, limitacoes ou escolhas metodologicas.
5. Quando o sentido tecnico ou academico estiver ambiguo, nao reescrever; registrar pergunta ou pendencia.
6. Ao final, validar buscas comuns e resumir os tipos de ajuste feitos.

## Fronteira de autoria

Pode corrigir diretamente: ortografia, gramatica, pontuacao, conectivos, coesao local, padronizacao terminologica e problemas LaTeX locais.

Nao corrigir sem decisao do autor: tese, objetivos, metodo, resultados, interpretacao, contribuicao, limitacoes, afirmacoes fortes e novas evidencias.

## O que corrigir

- Acentuacao e grafia: manter `especifica` quando for verbo; usar `específica` quando for adjetivo; `atraves` -> `através` quando mantido, preferindo `por meio de` para meio.
- Concordancia verbal e nominal.
- Pontuacao em frases com citacao: `Segundo \cite{autor}, ...`.
- Crase indevida: `orientada à objetos` -> `orientada a objetos`.
- Gerundismo e coloquialismo.
- Repeticao excessiva e referencias vagas como `isso` sem antecedente claro.

## Estilo academico

Preferir:

- `O presente trabalho propoe...`
- `Foi implementado...`
- `Os resultados indicam...`
- `Em relacao a...`
- `Por meio de...`

Evitar:

- primeira pessoa sem justificativa;
- `muito importante` sem criterio;
- promessas como `garante` quando o estudo apenas indica ou sugere;
- reescrita extensa que apague o estilo do autor.

## LaTeX durante proofreading

- Preservar comandos LaTeX e argumentos.
- Nao quebrar labels, refs, cites, captions ou ambientes.
- Ao editar texto dentro de comando, conferir chaves e caracteres especiais.
- Usar `academic-latex` quando a correcao envolver estrutura, figura, tabela ou compilacao.

## Saida

Quando editar arquivos, informar categorias de mudanca e validacoes. Quando revisar sem editar, usar comentarios objetivos com localizacao aproximada, severidade, motivo pedagogico e sugestao acionavel.
