# Guia editorial das fichas

Decisões do projeto para escrever as fichas e resenhas de `src/fichas.py`. O público é o leitor leigo brasileiro; a página é uma **referência**, não um tratado aprofundado.

## Texto próprio

- Tudo é escrito do zero, em português. O livro *1001 TV Shows You Must Watch Before You Die* serve só como referência de tom e de fatos (o que a série é, quem a fez, por que importa).
- Nenhum trecho, imagem, página ou paráfrase próxima do livro entra no repositório público. Material do livro fica em `privado/` (ignorado pelo Git).
- Na dúvida sobre como abordar uma série, consultar o PDF original em `privado/` como inspiração, sem copiar.

## Tamanho por faixa de posição

Faixas sem sobreposição; o tamanho conta só o campo `texto` (caracteres, com espaços).

| Posições | Alvo | Estrutura |
|---|---|---|
| 1–10 | ~2000 caracteres | premissa; o que torna a série especial; contexto e legado; para quem serve e para quem não serve; por onde começar |
| 11–25 | ~1500 caracteres | premissa; o que a destaca; para quem serve |
| 26–100 | ~800 caracteres | premissa + um parágrafo de avaliação |

- Nas faixas maiores, poucos prêmios e números: cada um custa uma conferência em fonte oficial (ver `TODO.md`).
- Opinião e recomendação são opcionais; a inspiração é o tom do livro de referência.
- Equilíbrio no conteúdo extra: é uma referência, não um tratado.

## Spoilers

- Nunca entregar.
- Se uma revelação importante faz parte do atrativo da série, **anunciar que ela existe**, sem detalhes.

## Onde assistir

- Não listamos plataformas (mudam o tempo todo e variam por país).
- Cada ficha tem um link do IMDb. Hoje é uma busca pelo título original; `IMDB_IDS` em `src/assemble_public.py` aceita o link direto (`https://www.imdb.com/title/tt.../`) quando for conferido.

## Exibição

- Resenha com até 2 parágrafos aparece inteira.
- Com mais de 2, só o primeiro aparece; o resto fica atrás do botão "Ler mais" (alterna para "Ler menos").
