#!/usr/bin/env python3
"""Confere UTMs dos anuncios antes de publicar.

Entrada: CSV com as colunas anuncio,url. Exemplo:
  python3 conferir_utm.py anuncios.csv
Falha quando falta UTM ou quando dois anuncios usam o mesmo utm_content.
"""
import collections, csv, sys
from urllib.parse import parse_qs, urlparse

OBRIGATORIAS = ("utm_source", "utm_medium", "utm_campaign", "utm_content")

def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    with open(sys.argv[1], newline="", encoding="utf-8-sig") as f:
        linhas = list(csv.DictReader(f))
    if not linhas or not {"anuncio", "url"} <= set(linhas[0]):
        sys.exit("O CSV precisa ter as colunas anuncio,url e ao menos uma linha.")
    erros, conteudos = [], collections.defaultdict(list)
    for l in linhas:
        q = parse_qs(urlparse(l["url"]).query)
        faltam = [k for k in OBRIGATORIAS if not q.get(k, [""])[0]]
        if faltam:
            erros.append(f"{l['anuncio']}: falta {', '.join(faltam)}")
        if q.get("utm_content"):
            conteudos[q["utm_content"][0]].append(l["anuncio"])
    for valor, nomes in conteudos.items():
        if len(nomes) > 1:
            erros.append(f"utm_content '{valor}' repetido em: {', '.join(nomes)}")
    print(f"{len(linhas)} anuncios conferidos, {len(erros)} problemas.")
    for e in erros:
        print(" -", e)
    sys.exit(1 if erros else 0)

if __name__ == "__main__":
    main()
