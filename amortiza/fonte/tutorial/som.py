"""Mistura: voz da Sofia (voz.wav) + trilha Warm Welcome (musica.wav, em loop) + toques. Lê tempos.json."""
import numpy as np, wave, json
SR=44100; d=json.load(open('tempos.json')); DUR=d['dur']; S=d['seg']; N=int(DUR*SR); OFF=0.3
rd=lambda f:np.frombuffer(wave.open(f).readframes(10**9),np.int16).astype(float)/32768
voz=rd('voz.wav'); m=rd('musica.wav')
xf=int(2*SR); bg=m.copy(); loop=m[int(2*SR):]
while len(bg)<N:
    r=np.linspace(0,1,xf); bg=np.concatenate([bg[:-xf],bg[-xf:]*(1-r)+loop[:xf]*r,loop[xf:]])
bg=bg[:N]
v=np.zeros(N); a=int(OFF*SR); v[a:a+len(voz)]=voz[:N-a]
fx=np.zeros(N)
def put(sig,t):
    i=int(t*SR); j=min(N,i+len(sig)); fx[i:j]+=sig[:j-i]
def pop(vol=.35):
    n=int(.12*SR);t=np.arange(n)/SR;f=500+1300*t/.12;return vol*np.sin(2*np.pi*np.cumsum(f)/SR)*np.minimum(1,t/.002)*np.exp(-t/.04)
def plin(vol=.4):
    n=int(.8*SR);t=np.arange(n)/SR;return vol*(np.sin(2*np.pi*1568*t)+.6*np.sin(2*np.pi*2093*t))*np.minimum(1,t/.003)*np.exp(-t/.25)
for t in d['taps']: put(pop(),t)
put(plin(.3),S[5])
k=int(.15*SR);sm=np.convolve(np.abs(v),np.ones(k)/k,'same');duck=np.where(sm>.012,.35,1.0);duck=np.convolve(duck,np.ones(int(.3*SR))/int(.3*SR),'same')
t=np.arange(N)/SR; fade=np.minimum(1,t/.5)*np.minimum(1,(DUR-t)/2)
out=v*1.0+fx*.4+bg*.32*duck*fade
out=out/max(1,np.abs(out).max()/.95)
w=wave.open('som.wav','w');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes());w.close()
