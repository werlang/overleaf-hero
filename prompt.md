# Overleaf Hero - Prompt para Revisão de TCCs em LaTeX

## Contexto do Projeto

Este workspace contém três (ou mais) diretórios principais:
- **`template/`**: Template base de TCC (LaTeX) - NUNCA MODIFICAR
 **`sample/` (ou `sample00/`, `sample01/`, ...)**: Projetos de exemplo já revisados (referência) - NÃO MODIFICAR. Estes projetos são somente texto (imagens removidas no repositório de amostra).
- **`project/`**: Projeto atual a ser revisado - TRABALHAR AQUI

> Nota: Os diretórios `sample*` (ex.: `sample/`, `sample00/`...) são exemplos de referência em texto apenas — todas as imagens foram removidas do repositório de amostra. Não conte com figuras presentes nos samples durante a revisão.

 ❌ Qualquer arquivo em qualquer diretório de amostra (ex.: `sample/`, `sample00/`, `sample01/`, etc.)

 - [ ] Nenhum arquivo em `template/` ou em quaisquer `sample*` (ex.: `sample/`, `sample00/`, `sample01/`) foi modificado

1. **Correção ortográfica e gramatical** (português brasileiro acadêmico)
2. **Melhoria de clareza e coesão textual**
3. **Padronização de formatação LaTeX**
4. **Conformidade com normas ABNT**
5. **Qualidade acadêmica** (estilo formal, objetivo, impessoal)
6. **Consistência terminológica** (termos técnicos padronizados)

## Instruções de Execução

### Fase 1: Mapeamento e Análise (OBRIGATÓRIA)

```markdown
1. Listar todos os arquivos .tex no diretório project/
2. Ler arquivo principal (project/tcc.tex) para entender estrutura
3. Identificar capítulos incluídos e ordem de compilação
4. Ler pré-textuais (resumo, abstract, etc.)
5. Criar checklist estrutural baseado no tipo de trabalho (TCC1, TCC2, Artigo)
```

### Fase 2: Revisão Sistemática por Capítulo

Para cada arquivo `.tex` no `project/`, executar:

#### A. Leitura Completa
- Ler arquivo inteiro para compreender contexto e fluxo argumentativo
- Identificar termos-chave e conceitos centrais do trabalho
- Mapear referências cruzadas (labels, refs, cites)

#### B. Identificação de Problemas

**Erros Ortográficos Comuns:**
- Acentuação: especifica/específica, atraves/através, tambem/também
- Crase: "orientada à objetos" → "orientada a objetos"
- Compostos: "off-line" vs "offline" (padronizar com itálico: `\textit{offline}`)

**Erros Gramaticais:**
- Concordância verbal/nominal: "a ausência... podem" → "pode"
- Uso inadequado de vírgulas: "Segundo \cite{autor} o texto..." → "Segundo \cite{autor}, o texto..."
- Gerundismo: "vai estar fazendo" → "fará"

**Problemas de Estilo Acadêmico:**
- Impessoalidade: "Nós implementamos" → "Foi implementado"
- Linguagem coloquial: evitar "muito", "bastante" sem contexto técnico
- Conectivos inadequados: "através de" → "por meio de", "Aonde" → "Onde"
- Estrutura truncada: evitar frases incompletas ou ambíguas

**Problemas de Formatação LaTeX:**
- Termos técnicos estrangeiros SEM itálico: `back-end` → `\textit{back-end}`
- Espaços duplos: remover
- Aspas incorretas: `"texto"` → `` `texto' `` (usar aspas LaTeX)
- Figuras sem fonte: adicionar `\centerline{{Fonte: ...}}`
- Tabelas sem caption ou label
- Código-fonte sem listing environment apropriado

**Problemas de Coesão:**
- Repetição excessiva de termos: variar vocabulário academicamente
- Falta de conectivos: adicionar "Além disso,", "Entretanto,", "Por outro lado,"
- Transições abruptas entre parágrafos
- Referências vagas: "isso", "aquilo" sem antecedente claro

#### C. Aplicação de Correções

**Priorização:**
1. **CRÍTICO**: Erros que impedem compilação ou afetam sentido
2. **ALTO**: Erros gramaticais, typos óbvios, problemas de formatação ABNT
3. **MÉDIO**: Melhorias de clareza, padronização terminológica
4. **BAIXO**: Otimizações de estilo (apenas se não alterar voz do autor)

**Princípios de Edição:**
- ✅ **PRESERVE A VOZ DO AUTOR**: Não reescrever completamente
- ✅ **MÍNIMA INTERVENÇÃO**: Corrigir apenas o necessário
- ✅ **CONSISTÊNCIA**: Padronizar termos técnicos em todo o documento
- ✅ **CLAREZA**: Simplificar frases complexas, mas manter rigor acadêmico
- ❌ **NÃO alterar argumentação ou conteúdo técnico**
- ❌ **NÃO remover citações ou referências**

### Fase 3: Verificações Específicas

#### Pré-textuais

**Resumo (Português):**
- Estrutura: Contexto → Problema → Solução → Resultados → Trabalhos Futuros
- Máximo: 500 palavras
- Conter palavras-chave do trabalho
- Mencionar metodologia e principais resultados
- SEM citações bibliográficas

**Abstract (Inglês):**
- Tradução precisa e idiomática do resumo
- Mesma estrutura do resumo em português
- Termos técnicos em inglês correto

#### Capítulo 1 - Introdução

**Checklist:**
- [ ] Contextualização histórica/teórica do tema
- [ ] Motivação e justificativa claras
- [ ] Problema de pesquisa bem definido (pode estar em itálico como questão)
- [ ] Objetivo geral claro e específico
- [ ] Objetivos específicos mensuráveis e desdobrados do geral
- [ ] Organização do trabalho (roadmap dos capítulos)

**Problemas Comuns:**
- Objetivo muito vago: "estudar, analisar e desenvolver" → focar em RESOLVER
- Falta de questão-problema explícita

#### Capítulo 2 - Fundamentação Teórica

**Checklist:**
- [ ] Conceitos-chave bem definidos
- [ ] Citações corretas e completas
- [ ] Figuras e tabelas com fonte
- [ ] Sequência lógica de apresentação
- [ ] NÃO há plágio (texto copiado sem citação)

#### Capítulo 3 - Trabalhos Relacionados

**OBRIGATÓRIO:**
- [ ] Tabela comparativa entre trabalhos e proposta
- [ ] Análise crítica de cada trabalho
- [ ] Gap claramente identificado

**Formato da Tabela Comparativa:**
```latex
\begin{table}[h]
\centering
\caption{Comparação entre trabalhos relacionados}
\label{tab:comparativo}
\begin{tabular}{|l|c|c|c|c|}
\hline
Critério & Trabalho 1 & Trabalho 2 & Trabalho 3 & Proposta \\
\hline
Característica A & \ticV & \ticX & \ticV & \ticV \\
...
\end{tabular}
\end{table}
```

#### Capítulos 4-5 - Metodologia e Resultados

**Verificar:**
- Metodologia reproduzível e clara
- Ferramentas e tecnologias justificadas
- Resultados alinhados com objetivos
- Discussão crítica (não apenas descritiva)
- Figuras/tabelas com dados reais e fontes

#### Capítulo 6 - Conclusão

**Checklist:**
- [ ] Retoma objetivos propostos
- [ ] Apresenta contribuições do trabalho
- [ ] Menciona limitações
- [ ] Sugere trabalhos futuros específicos

### Fase 4: Verificações Finais

#### Consistência Terminológica

Criar tabela de termos-chave e verificar uso consistente:

| Termo Original | Forma Padronizada | Formatação |
|---------------|-------------------|------------|
| back-end | \textit{back-end} | Itálico |
| front-end | \textit{front-end} | Itálico |
| offline | \textit{offline} | Itálico |
| backup | \textit{backup} | Itálico |
| API RESTful | API RESTful | Normal |

#### Buscas de Validação (grep_search)

Execute estas buscas no `project/**/*.tex`:

```regex
# Erros comuns de português
"através de|atraves|Atraves"
"a nível de|ao nível de"
"onde|aonde" (verificar contexto)
"mesmo que|sendo que|visto que"

# Problemas de formatação
"  +" (espaços duplos)
"[^`]\"[^']" (aspas erradas)

# Inconsistências técnicas
"ALCOA\+[^+]" (ALCOA+ ao invés de ALCOA++)
"back-end|front-end|offline|backup" (sem itálico)

# Concordância
"foi realizados|foram realizado"
"foi implementados|foram implementado"
```

#### Validação de Referências

```bash
# Verificar citações órfãs
grep -r "\\cite{" project/**/*.tex | cut -d'{' -f2 | cut -d'}' -f1 | sort -u
# Comparar com entradas em references.bib
```

### Fase 5: Relatório de Revisão (Relatório Crítico `.md` por padrão)

Por padrão, gere um relatório `.md` com esta estrutura; caso o autor peça para não gerar, não crie o arquivo.

```markdown
# Relatório de Revisão - [Nome do Trabalho]

## Resumo Executivo
- Total de arquivos revisados: X
- Total de correções aplicadas: Y
- Classificação: [Excelente / Bom / Necessita melhorias]

## Correções por Categoria
### Ortografia e Gramática (Z correções)
- arquivo.tex:linha: "erro" → "correção"

### Formatação LaTeX (W correções)
- arquivo.tex:linha: descrição

### Melhorias de Clareza (V correções)
- arquivo.tex:seção: descrição

## Checklist Estrutural
- [x] Elemento presente e correto
- [ ] Elemento ausente ou incompleto

## Recomendações
1. Prioridade ALTA: [item]
2. Prioridade MÉDIA: [item]
```

## Arquivos a NUNCA Modificar

- ❌ Qualquer arquivo em `template/`
- ❌ Qualquer arquivo em quaisquer diretórios `sample*` (ex.: `sample/`, `sample00/`, `sample01/`)
- ❌ `project/references.bib` (apenas revisar, não modificar estrutura)
- ❌ Arquivos de configuração LaTeX (.cls, .sty, .def, .bst)

## Arquivos de Trabalho Principal

- ✅ `project/tcc.tex` (apenas se necessário corrigir includes)
- ✅ `project/pretextuais/*.tex` (resumo, abstract, etc.)
- ✅ `project/capitulo*/*.tex` (todos os capítulos)
- ✅ `project/apendices/*.tex` (apêndices)

## Padrões de Qualidade Acadêmica

### Estilo de Escrita

**BOM:**
- "O presente trabalho propõe..."
- "Foi implementado um sistema..."
- "Os resultados demonstram que..."
- "Por meio de testes, verificou-se..."
- "Em relação ao atributo X, observa-se..."

**EVITAR:**
- "Nós implementamos..." (impessoalidade)
- "Eu desenvolvi..." (impessoalidade)
- "Muito importante..." (vago)
- "Através de..." (use "por meio de")
- "Referente ao..." (use "Em relação ao", "Quanto ao")

### Formatação ABNT em LaTeX

**Figuras:**
```latex
\begin{figure}[!h]
    \centerline{\includegraphics[width=15em]{caminho/imagem.png}}
    \caption{Descrição clara da figura}
    \label{fig:nome_figura}
    \centerline{{Fonte: autoria própria ou \cite{referencia}}}
\end{figure}
```

**Tabelas:**
```latex
\begin{table}[h]
\centering
\caption{Descrição da tabela}
\label{tab:nome_tabela}
\begin{tabular}{|l|l|l|}
\hline
... conteúdo ...
\hline
\end{tabular}
\footnotesize{Fonte: autoria própria}
\end{table}
```

**Citações:**
```latex
\citep{ref}           % (AUTOR, Ano)
\citet{ref}           % Autor (Ano)
\citep[p.~30]{ref}    % (AUTOR, Ano, p. 30)
\apud{orig}{p1}{cons}{p2}  % Citação indireta
```

## Fluxo de Trabalho Recomendado

```
1. Ler prompt.md (este arquivo)
2. Mapear estrutura do projeto (project/)
3. Criar todo-list com 10 tarefas principais
4. Para cada capítulo:
   - Marcar tarefa como "in-progress"
   - Ler arquivo completo
   - Identificar problemas
   - Aplicar correções (multi_replace quando possível)
   - Marcar como "completed"
5. Verificações finais (grep_search)
6. Remover arquivos obsoletos (se houver)
7. Confirmar sucesso: "Revisão completa concluída!"
```

## Princípios Fundamentais

1. **NUNCA pare no meio**: Continue até completar TODOS os capítulos
2. **PRESERVE o autor**: Corrija, não reescreva
3. **SEJA SISTEMÁTICO**: Use todo-list para tracking
4. **PARALELIZAÇÃO**: Use multi_replace_string_in_file quando possível
5. **VALIDAÇÃO**: Execute get_errors ao final
6. **DOCUMENTAÇÃO**: Apenas se solicitado explicitamente

## Casos Especiais

### TCC 1 (Anteprojeto)
Elementos adicionais obrigatórios:
- Cronograma de atividades
- Resultados parciais
- Próximos passos detalhados

### TCC 2 (Trabalho Final)
Deve ter todos elementos completos:
- Resultados finais
- Discussão aprofundada
- Trabalhos futuros
- Conclusão definitiva

### Artigo Científico
Estrutura mais concisa:
- Abstract mais técnico
- Metodologia mais detalhada
- Resultados com análise estatística
- Discussão comparativa forte

## Exemplo de Uso

```bash
# Usuário solicita:
"Revise todo o projeto em project/ seguindo as melhores práticas acadêmicas"

# Você deve:
1. Ler este prompt.md inteiro
2. Mapear project/**/*.tex
3. Criar todo-list (manage_todo_list)
4. Revisar sistematicamente cada arquivo
5. Aplicar todas as correções necessárias
6. Validar (get_errors)
7. Confirmar conclusão
```

## Checklist Final de Entrega

Antes de considerar o trabalho concluído, verificar:

- [ ] Todos os arquivos .tex em project/ foram revisados
- [ ] Resumo e abstract estão alinhados e dentro de 500 palavras
- [ ] Todos os capítulos obrigatórios estão presentes
- [ ] Figuras e tabelas têm caption, label e fonte
- [ ] Referências estão formatadas corretamente
- [ ] Nenhum erro de compilação (get_errors)
- [ ] Termos técnicos padronizados
- [ ] Linguagem acadêmica formal mantida
- [ ] Todo-list 100% completo
 - [ ] Nenhum arquivo em `template/` ou em quaisquer `sample*` (ex.: `sample/`, `sample00/`, `sample01/`) foi modificado

---

**Lembre-se**: Qualidade acadêmica + Preservação da voz do autor + Revisão completa = Sucesso! 🎓
