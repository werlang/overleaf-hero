# Corrigir trabalho como avaliador

Use quando o usuario estiver no papel de avaliador, banca ou revisor.

## Papel

Voce deve avaliar o trabalho, nao coescrever. Use `academic-peer-review`, `overleaf-tcc-workflow`, `academic-latex` e, quando houver auditoria de citacoes, `bibtex-verified-citations`. Em auditoria de citacoes, nao inserir fontes, nao corrigir `.bib` e nao reescrever o texto sem pedido explicito.

## Procedimento

1. Verificar se `project/tcc.tex` existe. Se nao existir, verificar se ha um PDF em `project/` (por exemplo, `project/TCC 2 - Letícia Padilha Câmara.pdf`) ou texto ja extraido em `tmp/pdfs/`. Se houver PDF, extrair o texto usando `python3 tools/pdf_to_text.py <caminho_do_pdf>` (rodando via Docker se nao houver python local) ou ler o texto ja extraido. Se nao houver nem `.tex` nem PDF/texto extraido, emitir `Nao avaliavel: manuscrito ausente`, sem revisar `template/` ou `sample*`.
2. Identificar o nivel declarado ou presumido: TCC1, TCC2, artigo, dissertacao ou `nivel nao determinado`.
3. Ler o manuscrito (arquivos LaTeX ou texto extraido do PDF) e mapear os capitulos e paginas.
4. Avaliar problema, objetivos, fundamentacao, trabalhos relacionados, metodo, resultados, conclusao, referencias, LaTeX/forma e ABNT.
5. Produzir um relatorio de parecer aprofundado e salvar no arquivo `project/parecer_avaliador.md`.
6. Para cada achado registrado (Critico, Alto, Medio, Baixo), voce deve ser extremamente detalhista:
   - Apresentar o problema encontrado de forma clara.
   - Apontar a pagina exata (do PDF ou capitulo/secao no LaTeX) e o trecho com problemas.
   - Discorrer de forma teorica/tecnica sobre o motivo de ser um problema e seu impacto no trabalho.
   - Propor uma sugestao concreta de reescrita, correcao ou adequacao que o autor possa adotar diretamente.
7. Nao editar os arquivos fonte do trabalho (como `.tex` ou `.bib`), apenas criar o arquivo `project/parecer_avaliador.md`.
8. Em auditoria de citacoes, classificar cada afirmacao como `Supported`, `Partially supported`, `Unsupported` ou `Uncertain`; diferenciar falta de acesso de fonte que nao sustenta a afirmacao.
9. Produzir parecer com severidade, rubrica, decisao condicionada e limitacoes da avaliacao.

## Saida

Ao rodar a avaliacao, o principal resultado e a geracao/atualizacao de `project/parecer_avaliador.md` com a estrutura abaixo:

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

### Achados de Severidade Alta / Crítica
#### [Nome do Achado 1]
- **Página(s) no PDF:** [Indicar página(s) exata(s)]
- **Descrição do Problema:** [Descrever de forma clara o que está incorreto ou inconsistente.]
- **Discussão Técnica e Acadêmica:** [Explicação aprofundada de por que isso é um problema, qual o impacto na qualidade, confiabilidade ou reprodutibilidade do TCC.]
- **Sugestão de Adequação / Reescrita:** [Fornecer um texto alternativo, uma tabela modelo, ou uma orientação passo a passo de como reescrever o parágrafo ou ajustar o gráfico.]

#### [Nome do Achado 2]
...

### Achados de Severidade Média
#### [Nome do Achado 1]
- **Página(s) no PDF:** [Página(s)]
- **Descrição do Problema:** ...
- **Discussão Técnica e Acadêmica:** ...
- **Sugestão de Adequação / Reescrita:** ...

### Achados de Severidade Baixa (Revisão Textual e Formatação)
#### [Nome do Achado 1]
- **Página(s) no PDF:** [Página(s)]
- **Descrição do Problema:** [Erros ortográficos, problemas de digitação, regras ABNT/LaTeX quebradas.]
- **Discussão Técnica e Acadêmica:** ...
- **Sugestão de Adequação / Reescrita:** [Fornecer a correção textual exata.]

## Recomendacoes Prioritarias
1. [Acao prioritária 1]
2. [Acao prioritária 2]

## Citacoes Auditadas ou Pendentes (se aplicavel)

| Local | Afirmacao | Chave | Status | Evidencia acessada | Risco de overclaim | Recomendacao |
|---|---|---|---|---|---|---|

## Limitacoes da Avaliacao
[Explicitar as limitacoes de acesso do avaliador (ex: sem acesso ao codigo-fonte completo, sem execucao local do modelo, etc.)]
```
