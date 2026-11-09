# -*- coding: utf-8 -*-
"""Gera site/index.html (versão publicável): só texto próprio + dados factuais.
Nada do livro (imagens, OCR, páginas). Uso: python src/assemble_public.py"""
import json, re, os, sys
SP = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SP)
sys.path.insert(0, SP)
from pt_titles import PT
from fichas import F

lista = json.load(open(os.path.join(ROOT, "data", "lista_nyt.json"), encoding="utf-8"))

def alt_limpo(s):
    ok = []
    for p in (s or "").split(";"):
        p = p.strip()
        if not p or re.search(r"confirmar|subtítulo|The Office U|Rockfeller", p):
            continue
        ok.append(p)
    return " · ".join(ok)

items = []
for r in lista:
    k = r["rank"]
    pt = PT[k]
    anos = (r["anos_nyt"] or "").replace("-present", "–hoje").replace("-", "–")
    it = {"rank": k, "nyt": r["titulo_nyt"], "anos": anos, "pt": pt[0], "alt": alt_limpo(pt[4]), "ficha": None}
    if k in F:
        d = dict(F[k])
        it["ficha"] = {x: (d.get(x) or "") for x in ("tagline", "genero", "pais", "anos", "elenco", "emissora", "premios", "parecido", "episodio")}
        it["ficha"]["texto"] = d["texto"]
    items.append(it)

rodape = [
 "A lista e a ordem são as do jornal The New York Times (“The 100 Best TV Shows of the 21st Century”). Esta página não é afiliada ao jornal.",
 "As fichas e resenhas dos 25 primeiros foram escritas para esta página, em texto próprio, a partir de pesquisa em fontes públicas; o livro “1001 TV Shows You Must Watch Before You Die” foi uma das referências de consulta. Elenco, emissora, anos e prêmios são informações factuais e podem ter pequenas imprecisões; em caso de dúvida, confira numa fonte oficial.",
 "Títulos em português: usamos o título da exibição no Brasil quando há um conhecido; quando não há, mantemos o original. As marcações de “já vi” e “quero ver” e suas anotações ficam apenas neste navegador, não são enviadas a ninguém.",
]
data = {"items": items, "rodape": rodape}
dj = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = open(os.path.join(SP, "template_publico.html"), encoding="utf-8").read().replace("__DATA__", dj)
out = os.path.join(ROOT, "site")
os.makedirs(out, exist_ok=True)
dest = os.path.join(out, "index.html")
open(dest, "w", encoding="utf-8").write(html)
print("ok", len(items), "itens;", sum(1 for i in items if i["ficha"]), "com ficha;", os.path.getsize(dest) // 1024, "KB")
