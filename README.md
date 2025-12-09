# Workspace Overleaf Hero - Revisão de TCCs e Artigos Científicos

Este workspace está configurado para facilitar a revisão sistemática de trabalhos acadêmicos em LaTeX.

## 📁 Estrutura do Workspace

```
TEMPLATE_ANTEPROJETO___CRIE_UMA_CÓPIA/
├── template/              # Template base (NUNCA modificar)
├── sample/ (ou sample00/, sample01/, ...) # Projetos de exemplo já revisados (NUNCA modificar). Estes projetos são somente texto (imagens removidas).
├── project/               # Seu projeto atual (TRABALHAR AQUI)
├── prompt.md              # Instruções completas para o agente
├── OVERLEAF_HERO_MODE.md  # Configuração do modo de agente
└── README.md              # Este arquivo
```

## 🚀 Como Usar

### 1. Prepare Seu Projeto

Coloque os arquivos do seu TCC/artigo na pasta `project/`:

```bash
project/
├── tcc.tex                    # Arquivo principal
├── references.bib             # Referências bibliográficas
├── pretextuais/
│   ├── resumo.tex
│   ├── abstract.tex
│   └── ...
├── capitulo1/
│   └── capitulo1.tex
├── capitulo2/
│   └── capitulo2.tex
└── ...
```

### 2. Solicite a Revisão

No VS Code com GitHub Copilot, simplesmente diga:

```
Revise todo o projeto seguindo as melhores práticas acadêmicas
```

Ou seja mais específico:

```
Faça uma revisão completa do projeto em project/, corrigindo gramática,
formatação LaTeX, e garantindo qualidade acadêmica
```

### 3. O Agente Vai:

✅ Mapear todos os arquivos `.tex` em `project/`  
✅ Criar uma todo-list para tracking  
✅ Revisar sistematicamente cada capítulo  
✅ Corrigir erros ortográficos e gramaticais  
✅ Padronizar formatação LaTeX e ABNT  
✅ Verificar consistência terminológica  
✅ Validar referências e citações  
✅ Confirmar conclusão da revisão  

## 📋 O Que o Agente Revisa

### ✍️ Gramática e Ortografia
- Acentuação correta
- Concordância verbal e nominal
- Uso adequado de crases
- Pontuação acadêmica

### 🎨 Formatação LaTeX
- Figuras com caption, label e fonte
- Tabelas formatadas corretamente
- Citações no padrão ABNT
- Termos técnicos em itálico

### 📚 Qualidade Acadêmica
- Impessoalidade do texto
- Clareza e coesão
- Estrutura lógica
- Consistência terminológica

### 📊 Elementos Estruturais
- Resumo e Abstract (máx. 500 palavras)
- Introdução com problema e objetivos
- Fundamentação teórica adequada
- Trabalhos relacionados com tabela comparativa
- Metodologia clara
- Resultados alinhados com objetivos
- Conclusão consistente

## 🔍 Arquivos de Referência

### `prompt.md`
Contém instruções detalhadas sobre:
- Workflow de revisão completo
- Checklist de elementos obrigatórios
- Padrões de formatação LaTeX/ABNT
- Erros comuns e como corrigi-los
- Exemplos de código LaTeX

### `OVERLEAF_HERO_MODE.md`
Configuração do modo de agente para VS Code. Use este arquivo para:
- Configurar o modo "Overleaf Hero"
- Entender a filosofia de revisão
- Ver exemplos de uso

### `sample/` (ou `sample00/`, `sample01/`, ...)
Projetos de exemplo já revisados. Use como referência para:
- Ver formatação correta de tabelas e estrutura LaTeX (note que as imagens foram removidas das amostras)
> Nota: Estes projetos de amostra são apenas texto — as imagens foram removidas intencionalmente para focar a revisão em conteúdo textual. Não utilize imagens dos samples como referência visual.
- Entender estrutura de capítulos
- Verificar padrões de citação
- Comparar qualidade acadêmica

## ⚙️ Configuração do Agente (Opcional)

Se quiser configurar manualmente o modo "Overleaf Hero":

1. Abra configurações do VS Code
2. Procure por "Agent Modes"
3. Crie novo modo chamado "Overleaf Hero"
4. Cole o conteúdo de `OVERLEAF_HERO_MODE.md`
5. Defina padrões de arquivo: `**/*.tex, **/*.bib, **/prompt.md`

## 📖 Tipo de Trabalhos Suportados

- ✅ TCC 1 (Anteprojeto)
- ✅ TCC 2 (Trabalho Final)
- ✅ Artigos Científicos
- ✅ Dissertações
- ✅ Teses

## ⚠️ Importante

-### NUNCA Modificar:
- ❌ Arquivos em `template/`
- ❌ Arquivos em quaisquer diretórios `sample*` (ex.: `sample/`, `sample00/`, `sample01/`)
- ❌ Arquivos de configuração LaTeX (`.cls`, `.sty`, `.def`, `.bst`)

### TRABALHE APENAS em:
- ✅ Arquivos `.tex` em `project/`
- ✅ Seu arquivo `project/references.bib` (se necessário)

## 🎯 Resultados Esperados

Após a revisão, você terá:

- ✅ Texto sem erros gramaticais ou ortográficos
- ✅ Formatação LaTeX padronizada e correta
- ✅ Referências verificadas e consistentes
- ✅ Estrutura acadêmica completa
- ✅ Qualidade apropriada para defesa/publicação

## 📞 Dicas de Uso

### Para Revisão Rápida
```
Revise apenas os pré-textuais (resumo e abstract)
```

### Para Capítulo Específico
```
Revise o Capítulo 3 focando em clareza e coesão
```

### Para Verificação Final
```
Execute verificações finais: erros de compilação, referências órfãs,
e consistência terminológica
```

## 🧠 Filosofia

O agente Overleaf Hero segue estes princípios:

1. **Preservar a Voz do Autor**: Corrige, não reescreve
2. **Mínima Intervenção**: Apenas correções necessárias
3. **Qualidade Acadêmica**: Garante excelência formal
4. **Sistematicidade**: Workflow completo e organizado
5. **Transparência**: Todo o processo é trackeável

---

**Pronto para começar?** Coloque seu projeto em `project/` e solicite a revisão! 🎓✨
