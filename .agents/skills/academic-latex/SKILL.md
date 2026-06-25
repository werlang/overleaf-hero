---
name: academic-latex
description: Revisao e escrita de sintaxe LaTeX academica, ABNT e template de TCC. Use para corrigir figuras, tabelas, captions, labels, refs, BibTeX, comandos do template, pre-textuais, apendices, citacoes e problemas de compilacao em projetos LaTeX academicos.
---

# Academic LaTeX

Use esta skill para manter o projeto LaTeX compilavel, padronizado e adequado ao template academico.

## Limites do workspace

- Nunca editar `template/`.
- Nunca editar `sample*`.
- Evitar editar `.cls`, `.sty`, `.def` e `.bst` salvo pedido explicito.
- Trabalhar normalmente em `project/**/*.tex` e, quando necessario, em `project/references.bib` junto com `bibtex-verified-citations`.

## Workflow

1. Ler `project/tcc.tex` para entender a ordem real de `\input` e `\include`.
2. Mapear arquivos `.tex` ativos no `project/`; arquivos existentes mas nao incluidos devem ser tratados como possivel legado.
3. Corrigir sintaxe LaTeX preservando texto e intencao do autor.
4. Validar labels, refs, captions, fontes e citacoes.
5. Rodar verificacoes textuais e, se houver ambiente TeX, compilar ou usar o validador disponivel.

## Figuras

Toda figura deve ter conteudo, legenda, label e fonte:

```latex
\begin{figure}[!h]
    \centerline{\includegraphics[width=15em]{caminho/imagem.png}}
    \caption{Descricao clara da figura}
    \label{fig:nome_figura}
    \centerline{{Fonte: autoria propria}}
\end{figure}
```

- Referenciar no texto com `Figura~\ref{fig:nome_figura}`.
- Nao depender de imagens nos diretorios `sample*`; os samples sao referencia textual.

## Tabelas

Toda tabela deve ter `\caption`, `\label`, corpo consistente e fonte. Para comparativos do template, usar `\ticV` e `\ticX` quando esses comandos estiverem definidos.

```latex
\begin{table}[h]
\centering
\caption{Descricao da tabela}
\label{tab:nome_tabela}
\begin{tabular}{|l|l|l|}
\hline
... conteudo ... \\hline
\end{tabular}
\footnotesize{Fonte: autoria propria}
\end{table}
```

## Citacoes e BibTeX

- Nao inserir nova citacao sem `bibtex-verified-citations`.
- Usar `\cite`, `\citep`, `\citet` ou comandos do template de acordo com o estilo ja presente.
- Nao aninhar comandos de citacao em construcoes frageis sem testar.
- Nao inventar campos BibTeX.

## Padroes comuns

- Termos estrangeiros em PT-BR: `\textit{back-end}`, `\textit{front-end}`, `\textit{offline}`, `\textit{framework}`.
- Aspas LaTeX: ``texto''.
- Referencias cruzadas: nao escrever numeros fixos como `Figura 3`; usar `\ref`.
- Codigo-fonte: usar ambiente existente do template, como `\jsoncode`, `\jscode`, `\htmlcode` ou `minted`, quando disponivel.

## Validacoes textuais

Buscar em `project/**/*.tex`:

- `atraves|através de`
- `  +`
- aspas retas em texto corrido
- `back-end|front-end|offline|framework|middleware` sem `\textit`
- `foi realizados|foram realizado|foi implementados|foram implementado`
