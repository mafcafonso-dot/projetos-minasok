"""Renderiza o vídeo tutorial quadro a quadro.
uso: python3 render.py tempos.json saida.mp4 [t0 t1]  (ou --frames t1 t2 ... para PNGs de teste)"""
import sys, json, subprocess, os, re
from playwright.sync_api import sync_playwright
FPS = 30
cfg = json.load(open(sys.argv[1]))          # {"seg":[...], "subs":[[a,b,txt],...], "env":[...], "dur":x}
SEG, SUBS, ENV, DUR = cfg['seg'], cfg['subs'], cfg.get('env', []), cfg['dur']
frames_mode = sys.argv[2] == '--frames'
srv = subprocess.Popen(['python3', '-m', 'http.server', '8765', '--bind', '127.0.0.1'], cwd='/home/claude',
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
import time; time.sleep(1)
try:
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={'width': 1080, 'height': 1920})
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.clock.install(time='2026-11-01T10:00:00-03:00')
        pg.add_init_script(f'window.SEG={json.dumps(SEG)};window.SUBS={json.dumps(SUBS)};window.ENDF={cfg.get("endfrac",.44)};')
        pg.goto('http://127.0.0.1:8765/tutorial/comp.html')
        pg.clock.run_for(1500)
        pg.evaluate('window.ready'); pg.evaluate('document.fonts.ready')
        cdp = pg.context.new_cdp_session(pg)
        cdp.send('Animation.enable')
        if frames_mode:
            want = sorted(float(x) for x in sys.argv[3:]); t = 0.0; f = 0
            os.makedirs('quadros', exist_ok=True)
            while want:
                t = f / FPS
                e = ENV[f] if f < len(ENV) else 0
                pg.evaluate(f'frame({t:.4f},{e})')
                pg.clock.run_for(round(1000 / FPS))
                if t >= want[0] - 1e-6:
                    pg.screenshot(path=f'quadros/q{want[0]:06.2f}.png'); want.pop(0)
                f += 1
        else:
            out = sys.argv[2]; a = float(sys.argv[3]) if len(sys.argv) > 3 else 0; b = float(sys.argv[4]) if len(sys.argv) > 4 else DUR
            ff = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                                   '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', str(FPS), out], stdin=subprocess.PIPE)
            last = time.time()
            for f in range(round(b * FPS)):
                t = f / FPS
                e = ENV[f] if f < len(ENV) else 0
                pg.evaluate(f'frame({t:.4f},{e})')
                # animações CSS do app no ritmo do vídeo
                now = time.time(); dt = max(1e-3, now - last); last = now
                cdp.send('Animation.setPlaybackRate', {'playbackRate': min(1.0, (1 / FPS) / dt)})
                pg.clock.run_for(round(1000 / FPS))
                if t >= a:
                    ff.stdin.write(pg.screenshot(type='jpeg', quality=90))
            ff.stdin.close(); ff.wait()
        print('erros:', errs)
        br.close()
finally:
    srv.terminate()
