import numpy as np, wave
from tempo import *
SR=44100; N=int(DUR*SR); rng=np.random.default_rng(7)
def env(n,a=.004,d=.2):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t/d)
def plin(v=.5):
    n=int(.7*SR);t=np.arange(n)/SR
    return v*(np.sin(2*np.pi*1568*t)*env(n,.002,.18)+.6*np.sin(2*np.pi*2093*t)*np.r_[np.zeros(int(.07*SR)),env(n-int(.07*SR),.002,.22)])
def papel(v=.35):
    n=int(.18*SR);x=rng.standard_normal(n);x=np.convolve(x,np.ones(6)/6,'same')-np.convolve(x,np.ones(40)/40,'same');return v*x*env(n,.003,.05)
def baque(v=.8):
    n=int(.45*SR);t=np.arange(n)/SR;f=110*np.exp(-t*7)+45
    return v*(np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.002,.16)+.25*rng.standard_normal(n)*env(n,.001,.03))
def pop(v=.45):
    n=int(.16*SR);t=np.arange(n)/SR;f=380+1500*t/.16
    return v*np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.002,.05)
def whoosh(v=.35,d=.45):
    n=int(d*SR);x=rng.standard_normal(n);k=np.linspace(0,1,n);x=np.convolve(x,np.ones(12)/12,'same')
    return v*x*np.sin(np.pi*k)**2
def fanfarra(v=.32):
    out=np.zeros(int(1.1*SR))
    for j,f in enumerate([523,659,784,1047]):
        n=int(.7*SR);t=np.arange(n)/SR;s=(np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*2*f*t))*env(n,.005,.25);a=int(j*.09*SR);out[a:a+n]+=s[:len(out)-a]
    return v*out
mix=np.zeros(N)
def at(t_anim,s):
    a=int(video(t_anim)*SR);b=min(N,a+len(s));mix[a:b]+=s[:b-a]
at(.7,baque(.6)); at(1.6,pop()); at(2.2,pop())
for i in range(9): at(4.3+i*.33+.35,papel(.4))
at(7.0,baque(.75)); at(9.0,whoosh(.4))
for i in range(9): at(9.05+i*.03,papel(.18))
at(11.3,plin(.55)); at(12.2,pop(.5)); at(15.6,baque(.85))
for k in range(6): at(16.6+k*.42,papel(.25))
at(18.3,baque(.6)); at(21.6,pop(.3)); at(22.6,pop(.3)); at(23.8,pop(.3))
for c in (21.9,23.1,24.3): at(c+.45,plin(.5))
at(25.0,pop(.45))
for i in range(3): at(25.55+i*.12,plin(.3))
at(26.0,whoosh(.45)); at(26.6,fanfarra()); at(27.8,pop(.4))
# voz
w=wave.open('voz.wav');x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768
a=int(OFF*SR);voz=np.zeros(N);voz[a:a+len(x)]=x[:N-a]
# trilha: Warm Welcome (ElevenLabs Music)
wm=wave.open('musica.wav');m=np.frombuffer(wm.readframes(wm.getnframes()),np.int16).astype(float)/32768
bg=np.zeros(N);bg[:min(N,len(m))]=m[:N]
from numpy.lib.stride_tricks import sliding_window_view
lvl=np.abs(voz);k=int(.15*SR);sm=np.convolve(lvl,np.ones(k)/k,'same');duck=np.where(sm>.02,.45,1.0);duck=np.convolve(duck,np.ones(int(.1*SR))/int(.1*SR),'same')
fade=np.minimum(1,np.arange(N)/(SR*.4))*np.minimum(1,(N-np.arange(N))/(SR*1.2))
out=voz*1.0+mix*.45+bg*.30*duck*fade
out=out/max(1,np.abs(out).max()/.95)
wv=wave.open('trilha.wav','wb');wv.setnchannels(1);wv.setsampwidth(2);wv.setframerate(SR);wv.writeframes((out*32767).astype(np.int16).tobytes());wv.close();print('ok')
