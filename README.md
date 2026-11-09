# Os 100 melhores programas de TV do século XXI (NYT), em português

Página única (SPA, um arquivo HTML, sem dependências) com a lista do *The New York Times*, títulos em português quando há,
e fichas/resenhas em texto próprio. Público: leitor leigo brasileiro.

## Estrutura

| Pasta | O que é | Versionada? |
|---|---|---|
| `src/` | `fichas.py` (fichas e resenhas próprias), `pt_titles.py` (títulos em português), `template_publico.html`, `assemble_public.py` | sim |
| `data/` | `lista_nyt.json` (posição, título, anos, se há verbete no livro) e `cruzamento.csv` (só números de página, sem texto do livro) | sim |
| `site/` | `index.html`, gerado por `python src/assemble_public.py` | sim |
| `privado/` | OCR e imagens das páginas do livro, scripts de extração, versão pessoal offline | **não** (`.gitignore`) |

## Regras

- O livro *1001 TV Shows You Must Watch Before You Die* é só **referência**: usamos fatos e escrevemos texto próprio.
  Nenhum texto, imagem ou paráfrase próxima do livro entra em `src/`, `data/` ou `site/`.
- Títulos em português só quando existe título oficial conhecido; senão, mantém-se o original.

## Gerar a página

```bash
python src/assemble_public.py
```

## Estado

- Fichas completas: posições 1–25.
- Posições 26–100: só título e anos ("Ficha em preparação").
