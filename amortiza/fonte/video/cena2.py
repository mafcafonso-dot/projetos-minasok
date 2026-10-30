import sys, subprocess, os, json
from playwright.sync_api import sync_playwright
from tempo import *
i,a,b=int(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])
env=json.load(open('env.json'))
tmp=f'cenas/v{i}.tmp.mp4'; out=f'cenas/v{i}.mp4'
ff=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30',tmp],stdin=subprocess.PIPE)
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file:///home/claude/video/anim.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(500)
    for f in range(round(a*FPS),round(b*FPS)):
        e=env[f] if f<len(env) else 0
        pg.evaluate(f'render({anim(f/FPS):.4f},{e})'); ff.stdin.write(pg.screenshot(type='jpeg',quality=92))
    br.close()
ff.stdin.close()
if ff.wait()==0: os.replace(tmp,out); print('ok',i)
