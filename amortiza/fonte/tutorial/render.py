"""uso: python3 render.py --frames t1 t2 ... | python3 render.py saida.mp4"""
import sys, subprocess, os, time, json
from playwright.sync_api import sync_playwright
FPS=30
srv=subprocess.Popen(['python3','-m','http.server','8766','--bind','127.0.0.1'],cwd='/home/claude/tut2',stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
time.sleep(1)
try:
  with sync_playwright() as p:
    br=p.chromium.launch(args=['--lang=pt-BR']); ctx=br.new_context(viewport={'width':1080,'height':1920},locale='pt-BR',timezone_id='America/Sao_Paulo')
    pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.clock.install(time='2026-11-08T10:00:00-03:00')
    pg.goto('http://127.0.0.1:8766/comp.html'); pg.clock.run_for(1500)
    pg.evaluate('window.ready'); pg.evaluate('document.fonts.ready')
    dur=pg.evaluate('DUR'); ENV=json.load(open('env.json')); json.dump({'dur':dur,'seg':pg.evaluate('SEGS'),'taps':pg.evaluate('TAPT()')},open('tempos.json','w'))
    if sys.argv[1]=='--frames':
      want=sorted(float(x) for x in sys.argv[2:]); f=0
      while want:
        t=f/FPS; pg.evaluate(f'frame({t:.4f},{ENV[f] if f<len(ENV) else 0})'); pg.clock.run_for(round(1000/FPS))
        if f==0 or True: pass
        if t>=want[0]-1e-6:
          time.sleep(.05); pg.screenshot(path=f'q{want[0]:05.1f}.png',scale='css'); want.pop(0)
        f+=1
    else:
      ff=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',sys.argv[1]],stdin=subprocess.PIPE)
      for f in range(round(dur*FPS)):
        pg.evaluate(f'frame({f/FPS:.4f},{ENV[f] if f<len(ENV) else 0})'); pg.clock.run_for(round(1000/FPS))
        ff.stdin.write(pg.screenshot(type='jpeg',quality=90))
      ff.stdin.close(); ff.wait()
    print('erros:',errs); br.close()
finally: srv.terminate()
