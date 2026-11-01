import numpy as np, wave, json
SR=44100; d=json.load(open('tempos.json')); DUR=d['dur']; OFF=d['off']; N=int(DUR*SR)
rd=lambda f:np.frombuffer(wave.open(f).readframes(10**9),np.int16).astype(float)/32768
voz=rd('voz.wav'); m=rd('/home/claude/video/musica.wav')
# música em loop: começo original + trechos 4s..27s com cruzamento de 2s
xf=int(2*SR); loop=m[int(4*SR):int(27*SR)]; bg=m[:int(27*SR)].copy()
while len(bg)<N+SR:
    r=np.linspace(0,1,xf); tail=bg[-xf:]*(1-r)+loop[:xf]*r; bg=np.concatenate([bg[:-xf],tail,loop[xf:]])
bg=bg[:N]
v=np.zeros(N); a=int(OFF*SR); v[a:a+len(voz)]=voz[:N-a]
# toques (pop suave) nos cliques
def pop(vol=.35):
    n=int(.12*SR);t=np.arange(n)/SR;f=500+1300*t/.12;return vol*np.sin(2*np.pi*np.cumsum(f)/SR)*np.minimum(1,t/.002)*np.exp(-t/.04)
fx=np.zeros(N)
S=d['seg'];T=lambda k,f:S[k]+(S[k+1]-S[k])*f
for t in [T(4,.38),T(5,.2),T(5,.74),T(9,.25)]:
    i=int(t*SR);p=pop();fx[i:i+len(p)]+=p[:N-i]
end=T(9,d.get('endfrac',.44))
def plin(vol=.4):
    n=int(.8*SR);t=np.arange(n)/SR;return vol*(np.sin(2*np.pi*1568*t)+.6*np.sin(2*np.pi*2093*t))*np.minimum(1,t/.003)*np.exp(-t/.25)
i=int(end*SR);p=plin();fx[i:i+len(p)]+=p[:N-i]
# ducking da música sob a voz
k=int(.15*SR);sm=np.convolve(np.abs(v),np.ones(k)/k,'same');duck=np.where(sm>.015,.38,1.0);duck=np.convolve(duck,np.ones(int(.25*SR))/int(.25*SR),'same')
fade=np.minimum(1,np.arange(N)/(SR*.5))*np.minimum(1,(N-np.arange(N))/(SR*1.8))
out=v*1.0+fx*.5+bg*.26*duck*fade
out=out/max(1,np.abs(out).max()/.95)
w=wave.open('trilha.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes());w.close();print('ok',DUR)
