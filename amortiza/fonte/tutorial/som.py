import numpy as np, wave, json
SR=44100; d=json.load(open('tempos.json')); DUR=d['dur']; S=d['seg']; N=int(DUR*SR)
t_all=np.arange(N)/SR; out=np.zeros(N)
def note(f,dur,vol,kind='mar'):
    n=int(dur*SR); t=np.arange(n)/SR
    if kind=='mar': w=np.sin(2*np.pi*f*t)+.35*np.sin(2*np.pi*4*f*t)*np.exp(-t/.05); env=np.minimum(1,t/.004)*np.exp(-t/.28)
    else: w=np.sin(2*np.pi*f*t)+.2*np.sin(2*np.pi*2*f*t); env=np.minimum(1,t/.01)*np.exp(-t/.5)
    return vol*w*env
def put(sig,at):
    i=int(at*SR); j=min(N,i+len(sig)); 
    if i<N: out[i:j]+=sig[:j-i]
bpm=112; beat=60/bpm
hz=lambda m:440*2**((m-69)/12)
chords=[[60,64,67],[55,59,62],[57,60,64],[53,57,60]]  # C G Am F
pat=[0,2,1,2,0,2,1,2]
b=0;t=0.0
while t<DUR:
    c=chords[(b//8)%4]
    i=pat[b%8]; put(note(hz(c[i]+12),.6,.16),t)
    if b%8 in (3,7): put(note(hz(c[(i+1)%3]+24),.4,.06),t+beat/4)
    if b%4==0: put(note(hz(c[0]-24),1.2,.22,'bass'),t)
    # chocalho
    n=int(.05*SR); put(np.random.default_rng(b).normal(0,1,n)*np.exp(-np.arange(n)/SR/.012)*.03,t+beat/2)
    b+=1;t=b*beat/2*2/2 if False else b*beat/2
fx=np.zeros(N)
def pop(vol=.35):
    n=int(.12*SR);t=np.arange(n)/SR;f=500+1300*t/.12;return vol*np.sin(2*np.pi*np.cumsum(f)/SR)*np.minimum(1,t/.002)*np.exp(-t/.04)
def plin(vol=.4):
    n=int(.8*SR);t=np.arange(n)/SR;return vol*(np.sin(2*np.pi*1568*t)+.6*np.sin(2*np.pi*2093*t))*np.minimum(1,t/.003)*np.exp(-t/.25)
music=out.copy(); out[:]=0
for tp in d['taps']: put(pop(),tp)
for s in S[1:5]: put(pop(.18),s+.25)
put(plin(),S[5]); fx=out.copy()
fade=np.minimum(1,t_all/.4)*np.minimum(1,(DUR-t_all)/1.5)
mix=music*fade+fx*.6
mix=mix/np.abs(mix).max()*.85
w=wave.open('som.wav','w');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype(np.int16).tobytes());w.close()
