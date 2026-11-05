#!/usr/bin/env python3
"""Calcula ponto de equilibrio e cenarios de um lancamento.

Exemplo:
  python3 cenarios.py --verba 8000 --preco 1997 --cpl 6 --conv-pior 0.01 --conv-base 0.02 --conv-melhor 0.04
Todas as taxas sao hipoteses ate existirem dados proprios da campanha.
"""
import argparse, math

def brl(v):
    return "R$ " + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--verba", type=float, required=True, help="verba total de anuncios (R$)")
    p.add_argument("--preco", type=float, required=True, help="preco liquido medio por venda (R$)")
    p.add_argument("--cpl", type=float, required=True, help="custo por lead esperado (R$)")
    p.add_argument("--parte-captacao", type=float, default=0.4, help="fracao da verba em captacao (0 a 1)")
    p.add_argument("--lista-atual", type=int, default=0, help="contatos que ja existem")
    p.add_argument("--conv-pior", type=float, default=0.01, help="lead -> venda, cenario ruim")
    p.add_argument("--conv-base", type=float, default=0.02, help="lead -> venda, cenario base")
    p.add_argument("--conv-melhor", type=float, default=0.04, help="lead -> venda, cenario bom")
    p.add_argument("--custo-max-pct", type=float, default=0.30, help="custo maximo por venda, fracao do preco")
    a = p.parse_args()
    if min(a.verba, a.preco, a.cpl) <= 0 or not 0 < a.parte_captacao <= 1:
        p.error("verba, preco e cpl precisam ser positivos; parte-captacao entre 0 e 1")

    leads = a.verba * a.parte_captacao / a.cpl + a.lista_atual
    print(f"Leads esperados: {leads:,.0f} (lista atual incluida: {a.lista_atual:,})".replace(",", "."))
    print(f"Ponto de equilibrio sobre a verba: {math.ceil(a.verba / a.preco)} vendas")
    print(f"Custo maximo por venda: {brl(a.preco * a.custo_max_pct)}")
    print(f"Pausar anuncio sem venda ao gastar: {brl(a.preco * a.custo_max_pct * 2)}")
    print(f"\n{'Cenario':<8} {'Conv.':>6} {'Vendas':>7} {'Receita':>18} {'ROAS':>6} {'Custo/venda':>16}")
    for nome, c in (("Ruim", a.conv_pior), ("Base", a.conv_base), ("Bom", a.conv_melhor)):
        v = leads * c
        cpv = brl(a.verba / v) if v else "-"
        print(f"{nome:<8} {c:>6.1%} {v:>7.0f} {brl(v * a.preco):>18} {v * a.preco / a.verba:>5.1f}x {cpv:>16}")
    print("\nHipoteses. Troque pelos numeros reais depois de 48 horas de campanha.")

if __name__ == "__main__":
    main()
