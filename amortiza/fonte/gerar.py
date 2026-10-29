import base64, pathlib
from mascote import mascote, svg_mascote, AZUL, AMARELO, BRANCO, CASA

D = pathlib.Path(__file__).parent
OUT = D / 'saida'
OUT.mkdir(exist_ok=True)

logo_mok = 'data:image/png;base64,' + base64.b64encode((D / 'logo-minasok-transparente.png').read_bytes()).decode()

FONTES = """
@font-face{font-family:Fredoka;font-weight:600;src:url(fonts/fredoka-latin-600-normal.woff2)}
@font-face{font-family:Fredoka;font-weight:700;src:url(fonts/fredoka-latin-700-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:400;src:url(fonts/montserrat-latin-400-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:500;src:url(fonts/montserrat-latin-500-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:600;src:url(fonts/montserrat-latin-600-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:700;src:url(fonts/montserrat-latin-700-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:800;src:url(fonts/montserrat-latin-800-normal.woff2)}
*{box-sizing:border-box;margin:0;padding:0}
"""

# ---------- mascote solto ----------
(OUT / 'mascote-amortiza.svg').write_text(svg_mascote(uid='a'))
(OUT / 'mascote-amortiza-animado.svg').write_text(svg_mascote(uid='a', animado=True))
(OUT / 'mascote-amortiza-fundo-azul-animado.svg').write_text(
    svg_mascote(uid='b', contorno=BRANCO, animado=True))


def masc_inline(uid, w, **kw):
    return f'<svg viewBox="-10 -100 320 490" width="{w}" height="{w * 490 / 320:.0f}">{mascote(uid=uid, **kw)}</svg>'


# ---------- logomarca com mascote ----------
def logo_html(fundo, cor, slogan, animado):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTES}
body{{background:{fundo};width:1200px;height:700px;display:flex;align-items:center;justify-content:center}}
.l{{display:flex;align-items:center;gap:36px}}
.n{{font-family:Fredoka;font-weight:600;font-size:200px;line-height:.9;color:{cor};letter-spacing:-2px}}
.s{{font-family:Montserrat;font-weight:600;font-size:33px;letter-spacing:10px;color:{slogan};margin-top:18px;padding-left:6px}}
</style></head><body><div class="l">{masc_inline('l', 260, contorno=cor, animado=animado)}
<div><div class="n">amortiza</div><div class="s">ANTECIPE E CONQUISTE</div></div></div></body></html>"""


(OUT / 'logo-mascote-branco.html').write_text(logo_html('#FFFFFF', AZUL, AZUL, False))
(OUT / 'logo-mascote-azul.html').write_text(logo_html(AZUL, BRANCO, AMARELO, False))
(OUT / 'logo-mascote-azul-animado.html').write_text(logo_html(AZUL, BRANCO, AMARELO, True))

# ---------- ícones simples (traço) ----------
ic = lambda body: f'<svg viewBox="0 0 24 24" width="46" height="46" fill="none" stroke="{AMARELO}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
ICONES = {
    'casa': ic('<path d="M3 11 12 3l9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>'),
    'desconto': ic('<path d="M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z"/><circle cx="8" cy="8" r="1.4"/><path d="m10 16 5-5"/>'),
    'calendario': ic('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/><path d="m9 15 2 2 4-4"/>'),
    'conversa': ic('<path d="M21 12a8 8 0 0 1-11.8 7L4 20l1.1-4.6A8 8 0 1 1 21 12z"/><path d="M9 11h6M9 14h4"/>'),
}

# ---------- casa de progresso (tela do celular) ----------
def casa_app(faltam, total, w):
    prog = (total - faltam) / total
    y = 263 - 209 * prog
    return f"""<div style="position:relative;width:{w}px;height:{w}px;margin:0 auto">
<svg viewBox="0 0 300 300" width="{w}" height="{w}"><defs><clipPath id="cp"><path d="{CASA}"/></clipPath></defs>
<path d="{CASA}" fill="{AMARELO}" fill-opacity=".15"/><rect x="0" y="{y:.1f}" width="300" height="300" fill="{AMARELO}" clip-path="url(#cp)"/>
<path d="{CASA}" fill="none" stroke="{AZUL}" stroke-width="40" stroke-linejoin="round"/></svg>
<div style="position:absolute;left:0;right:0;top:{w*0.47:.0f}px;text-align:center;font-family:Fredoka;font-weight:600;color:{AZUL}">
<div style="font-size:{w*0.27:.0f}px;line-height:1">{faltam}</div><div style="font-family:Montserrat;font-weight:600;font-size:{w*0.055:.0f}px">parcelas para ser sua</div></div></div>"""


itens = [
    ('casa', 'Adiante as parcelas<br>do <b>fim do contrato</b>'),
    ('desconto', 'Cada parcela adiantada<br>sai <b>com desconto dos juros</b>'),
    ('calendario', 'Seu contrato<br><b>termina antes</b>'),
    ('conversa', 'Peça o boleto pelo<br><b>WhatsApp da Minas Ok</b>'),
]
linhas = ''.join(f"""<div class="it"><div class="ib">{ICONES[k]}</div><div class="tx">{t}</div></div>""" for k, t in itens)

post = f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTES}
body{{width:1080px;height:1350px;background:{AZUL};position:relative;overflow:hidden;font-family:Montserrat;color:#fff}}
.mok{{position:absolute;top:48px;right:56px;width:230px}}
.h{{position:absolute;left:68px;top:120px;font-family:Fredoka;font-weight:600;line-height:.98}}
.h1{{font-size:70px}} .h2{{font-size:104px;color:{AMARELO};letter-spacing:-1px}} .h3{{font-size:54px;margin-top:6px}}
.h3 span{{color:{AMARELO}}}
.sub{{position:absolute;left:70px;top:470px;width:520px;font-size:29px;line-height:1.38;font-weight:500}}
.sub b{{color:{AMARELO};font-weight:700}}
.rule{{position:absolute;left:70px;top:604px;width:470px;height:3px;background:{AMARELO};opacity:.9}}
.lista{{position:absolute;left:70px;top:640px;display:flex;flex-direction:column;gap:22px}}
.it{{display:flex;align-items:center;gap:24px}}
.ib{{width:86px;height:86px;border:3px solid {AMARELO};border-radius:18px;display:flex;align-items:center;justify-content:center;flex:none}}
.tx{{font-size:25px;line-height:1.3;font-weight:500}} .tx b{{color:{AMARELO};font-weight:700}}
.phone{{position:absolute;left:628px;top:300px;width:380px;height:770px;border-radius:58px;background:#0B0F1A;padding:13px;transform:rotate(5deg);box-shadow:0 30px 60px rgba(0,0,0,.35)}}
.scr{{width:100%;height:100%;border-radius:46px;background:#F6F8FC;overflow:hidden;position:relative;color:{AZUL}}}
.notch{{position:absolute;top:10px;left:50%;transform:translateX(-50%);width:110px;height:30px;border-radius:20px;background:#0B0F1A}}
.sb{{height:52px;padding:16px 28px 0;font-size:15px;font-weight:700;color:#fff;background:{AZUL}}}
.hd{{background:{AZUL};padding:4px 22px 18px;display:flex;align-items:center;gap:10px}}
.hd .n{{font-family:Fredoka;font-weight:600;font-size:36px;color:#fff;line-height:1}}
.hd .s{{font-size:8.5px;letter-spacing:2.6px;color:{AMARELO};font-weight:700;margin-top:3px}}
.bd{{padding:18px 22px}}
.tt{{font-family:Fredoka;font-weight:600;font-size:21px;margin-bottom:10px}}
.cmp{{text-align:center;font-size:13px;font-weight:500;margin:6px 0 14px}} .cmp b{{font-weight:800}}
.card{{background:#FFF6D9;border:1.5px solid {AMARELO};border-radius:16px;padding:14px 16px;font-size:13px;line-height:1.5}}
.card .v{{font-family:Fredoka;font-weight:600;font-size:22px;line-height:1.15}}
.card .g{{color:#1E8A4C}}
.btn{{margin-top:14px;background:{AMARELO};color:{AZUL};font-weight:800;font-size:15px;text-align:center;padding:14px;border-radius:14px;letter-spacing:.5px}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:230px;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center}}
.fl{{display:flex;align-items:center;gap:18px}}
.fl .n{{font-family:Fredoka;font-weight:600;font-size:92px;color:{AZUL};line-height:.9;letter-spacing:-1px}}
.fl .s{{font-size:16px;letter-spacing:6px;color:{AZUL};font-weight:700;margin-top:8px;padding-left:3px}}
.url{{margin-top:12px;font-size:20px;font-weight:600;color:{AZUL};opacity:.8}}
</style></head><body>
<img class="mok" src="{logo_mok}">
<div class="h"><div class="h1">Simule sua</div><div class="h2">amortização</div><div class="h3">no app <span>amortiza</span></div></div>
<div class="sub">Veja quantas parcelas cabem no seu dinheiro e termine de pagar sua casa <b>mais rápido</b>.</div>
<div class="rule"></div>
<div class="lista">{linhas}</div>
<div class="phone"><div class="scr"><div class="notch"></div>
 <div class="sb">9:41</div>
 <div class="hd">{masc_inline('ph', 46, contorno=BRANCO)}<div><div class="n">amortiza</div><div class="s">ANTECIPE E CONQUISTE</div></div></div>
 <div class="bd"><div class="tt">Sua casa está ficando pronta</div>
 {casa_app(47, 60, 230)}
 <div class="cmp">Hoje: <b>53</b> → Depois de adiantar: <b>47</b></div>
 <div class="card">Adiantando 6 parcelas, você paga<div class="v">R$ 4.824,36</div>e economiza<div class="v g">R$ 3.183,66</div></div>
 <div class="btn">QUERO AMORTIZAR!</div></div>
</div></div>
<div class="foot"><div class="fl">{masc_inline('ft', 104, contorno=AZUL)}<div><div class="n">amortiza</div><div class="s">ANTECIPE E CONQUISTE</div></div></div>
<div class="url">amortiza-minasok.lovable.app</div></div>
</body></html>"""
(OUT / 'post.html').write_text(post)

# copia as fontes para a pasta de saída (os HTML apontam para fonts/)
import shutil
shutil.copytree(D / 'fonts', OUT / 'fonts', dirs_exist_ok=True)
print('ok')
