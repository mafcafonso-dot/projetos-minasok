AZUL = '#06449D'
AMARELO = '#F7BC0A'
BRANCO = '#FFFFFF'
CASA = 'M17 150 L150 27 L283 150 L283 283 L17 283 Z'


def mascote(contorno=AZUL, vazio=None, olho_fundo=BRANCO, pupila=AZUL, animado=False, uid='m', nivel=178):
    """Casa com perninhas e olhos. viewBox: 0 -100 300 480 (espaço para o pulo)."""
    css = ''
    if animado:
        css = f"""<style>
  #{uid}-corpo{{transform-box:view-box;transform-origin:150px 362px;animation:{uid}-pulo 1.5s infinite}}
  #{uid}-sombra{{transform-box:view-box;transform-origin:150px 366px;animation:{uid}-sombra 1.5s infinite}}
  #{uid}-olhos{{transform-box:view-box;transform-origin:150px 128px;animation:{uid}-pisca 4.5s infinite}}
  #{uid}-pe-e{{transform-box:view-box;transform-origin:108px 300px;animation:{uid}-pe-e 1.5s infinite}}
  #{uid}-pe-d{{transform-box:view-box;transform-origin:192px 300px;animation:{uid}-pe-d 1.5s infinite}}
  @keyframes {uid}-pulo{{
    0%{{transform:translateY(0) scale(1.07,.9);animation-timing-function:ease-out}}
    14%{{transform:translateY(-8px) scale(.95,1.07);animation-timing-function:ease-out}}
    45%{{transform:translateY(-82px) scale(1,1);animation-timing-function:ease-in}}
    80%{{transform:translateY(0) scale(.97,1.04);animation-timing-function:ease-out}}
    88%{{transform:translateY(0) scale(1.09,.88);animation-timing-function:ease-in-out}}
    100%{{transform:translateY(0) scale(1.07,.9)}}}}
  @keyframes {uid}-sombra{{
    0%,88%,100%{{transform:scale(1.1,1);opacity:.25}}
    45%{{transform:scale(.6,.7);opacity:.1}}}}
  @keyframes {uid}-pe-e{{0%,14%,80%,100%{{transform:rotate(0)}} 45%{{transform:rotate(14deg)}}}}
  @keyframes {uid}-pe-d{{0%,14%,80%,100%{{transform:rotate(0)}} 45%{{transform:rotate(-14deg)}}}}
  @keyframes {uid}-pisca{{0%,92%,100%{{transform:scaleY(1)}} 95%{{transform:scaleY(.08)}}}}
  @media (prefers-reduced-motion:reduce){{#{uid}-corpo,#{uid}-sombra,#{uid}-olhos,#{uid}-pe-e,#{uid}-pe-d{{animation:none}}}}
</style>"""
    olho = lambda cx: (f'<ellipse cx="{cx}" cy="128" rx="22" ry="27" fill="{olho_fundo}" stroke="{contorno}" stroke-width="7"/>'
                       f'<circle cx="{cx + 4}" cy="134" r="12" fill="{pupila}"/>'
                       f'<circle cx="{cx + 8}" cy="129" r="4" fill="{BRANCO}"/>')
    perna = lambda x, pid, dx: (f'<g id="{pid}"><rect x="{x - 12}" y="296" width="24" height="52" rx="12" fill="{contorno}"/>'
                                f'<ellipse cx="{x + dx}" cy="352" rx="27" ry="13" fill="{contorno}"/></g>')
    return f"""{css}
  <ellipse id="{uid}-sombra" cx="150" cy="368" rx="95" ry="11" fill="#0B1F45" opacity=".22"/>
  <g id="{uid}-corpo">
    {perna(108, uid + '-pe-e', -10)}
    {perna(192, uid + '-pe-d', 10)}
    <defs><clipPath id="{uid}-clip"><path d="{CASA}"/></clipPath></defs>
    {f'<path d="{CASA}" fill="{vazio}"/>' if vazio else ''}
    <rect x="0" y="{nivel}" width="300" height="300" fill="{AMARELO}" clip-path="url(#{uid}-clip)"/>
    <path d="{CASA}" fill="none" stroke="{contorno}" stroke-width="40" stroke-linejoin="round"/>
    <g id="{uid}-olhos">{olho(116)}{olho(184)}</g>
  </g>"""


def svg_mascote(**kw):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 -100 320 490" width="320" height="490">{mascote(**kw)}\n</svg>'
