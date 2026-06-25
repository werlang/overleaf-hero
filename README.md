# Overleaf Hero

Workspace para revisar, orientar e avaliar TCCs em LaTeX.

## Estrutura

```text
overleaf-hero/
├── template/   # modelo base; nao edite
├── sample*/    # exemplos de referencia; nao edite
├── project/    # trabalho atual; trabalhe aqui
├── .agents/    # skills e prompts para agentes
└── tools/      # scripts auxiliares
```

Use `project/` para colocar o trabalho que sera revisado. O arquivo principal esperado e `project/tcc.tex`, que aponta para pre-textuais, capitulos e apendices.

Os diretorios `sample*` servem apenas como referencia textual. As imagens podem estar ausentes e nao devem ser usadas como base visual.

## Como Usar

Abra o projeto no agente e escolha o tipo de ajuda que voce precisa:

- **Sou autor e quero revisar meu texto**: use `.agents/prompts/autor-revisar-trabalho.prompt.md`.
- **Sou autor e quero escrever uma secao**: use `.agents/prompts/autor-construir-texto.prompt.md`.
- **Sou orientador e quero comentar o trabalho**: use `.agents/prompts/orientador-corrigir-trabalho.prompt.md`.
- **Sou avaliador/banca e quero um parecer**: use `.agents/prompts/avaliador-corrigir-trabalho.prompt.md`.

Voce tambem pode pedir em linguagem natural:

```text
Revise o trabalho em project/ como autor, corrigindo gramatica, LaTeX e coesao.
```

```text
Avalie o trabalho como banca e aponte os problemas mais importantes.
```

```text
Ajude a escrever a metodologia em LaTeX, mas nao invente citacoes.
```

## O Que Pode Ser Editado

Normalmente o agente pode editar:

- `project/**/*.tex`
- `project/references.bib`, somente com verificacao de fonte
- `project/citation-cheatsheet.md`, quando novas citacoes forem adicionadas

O agente nao deve editar:

- `template/`
- `sample*`
- arquivos LaTeX de configuracao, como `.cls`, `.sty`, `.def` e `.bst`, salvo pedido explicito

## Citacoes e BibTeX

Novas referencias precisam ser verificadas antes de entrar no texto.

O agente deve:

1. pesquisar a fonte na internet;
2. confirmar que a fonte sustenta a afirmacao citada;
3. inserir a entrada no `.bib` apenas se o suporte for claro;
4. registrar a fonte em `project/citation-cheatsheet.md`.

Se a fonte nao comprovar a afirmacao, ela nao deve ser usada como citacao.

## Scripts Uteis

Verificar citacoes do projeto:

```bash
python tools/check_cites.py
```

Extrair informacoes de PDFs, quando houver uma pasta de PDFs configurada:

```bash
python tools/extract_papers.py
python tools/review_papers.py
```

## Para Agentes

As instrucoes canonicas ficam em:

- `.agents/skills/`
- `.agents/prompts/`
- `AGENTS.md`

Comece por `AGENTS.md` e escolha o prompt adequado ao papel do usuario.
