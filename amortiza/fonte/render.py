import sys, pathlib, subprocess
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent / 'saida'
static = {
    'post.html': ('post-amortiza.png', 1080, 1350),
    'logo-mascote-branco.html': ('logo-amortiza-mascote-fundo-branco.png', 1200, 700),
    'logo-mascote-azul.html': ('logo-amortiza-mascote-fundo-azul.png', 1200, 700),
}
with sync_playwright() as p:
    b = p.chromium.launch()
    for src, (dst, w, h) in static.items():
        pg = b.new_page(viewport={'width': w, 'height': h})
        pg.goto((OUT / src).as_uri()); pg.wait_for_timeout(400)
        pg.screenshot(path=str(OUT / dst))
        pg.close()
    # quadros da animação (1,5 s, 25 fps) para GIF e MP4
    if '--anim' in sys.argv:
        fr = OUT / 'frames'; fr.mkdir(exist_ok=True)
        pg = b.new_page(viewport={'width': 1200, 'height': 700})
        pg.goto((OUT / 'logo-mascote-azul-animado.html').as_uri()); pg.wait_for_timeout(300)
        n = 75  # 3 s = 2 pulos, uma piscada
        for i in range(n):
            t = i * 40
            pg.evaluate(f"document.getAnimations().forEach(a=>{{a.pause();a.currentTime={t}+ (a.animationName&&a.animationName.endsWith('pisca')?1500:0)}})")
            pg.screenshot(path=str(fr / f'f{i:03d}.png'))
        pg.close()
    b.close()
print('ok')
