import numpy as np, wave, json, re
OFF=.3;SR=44100
w=wave.open('voz.wav');x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768
h=int(.02*SR);r=np.sqrt(np.convolve(x**2,np.ones(h)/h,'same'))[::h];db=20*np.log10(r+1e-6);low=db<db.max()-30
gaps=[];i=0
while i<len(low):
    if low[i]:
        j=i
        while j<len(low) and low[j]: j+=1
        if (j-i)*.02>=.2 and i>0: gaps.append((i*.02,j*.02))
        i=j
    else: i+=1
voiced=np.where(~low)[0];t0=voiced[0]*.02;t1=voiced[-1]*.02
pars=[p.strip() for p in open('roteiro.txt').read().split('\n\n') if p.strip()]
L=[len(p) for p in pars];T=sum(L)
starts=[t0];ends=[];c=L[0]
for k in range(1,len(pars)):
    est=t0+(t1-t0)*c/T
    cand=[g for g in gaps if abs(g[1]-est)<2.5 and g[1]>starts[-1]+1]
    g=max(cand,key=lambda g:(g[1]-g[0])-abs(g[1]-est)*.12)
    ends.append(g[0]);starts.append(g[1]);c+=L[k]
ends.append(t1)
dur=t1+OFF+2.6
subs=[]
for p,a,b in zip(pars,starts,ends):
    parts=re.split(r'(?<=[.!?])\s+',p);chunks=[]
    for s in parts:
        if len(s)>60:
            bits=re.split(r'(?<=,)\s+',s);cur=''
            for q in bits:
                if len(cur)+len(q)>60 and cur: chunks.append(cur.strip());cur=q
                else: cur+=' '+q
            if cur.strip(): chunks.append(cur.strip())
        else: chunks.append(s)
    m=[];i=0
    while i<len(chunks):
        if len(chunks[i])<10 and chunks[i].endswith(',') and i+1<len(chunks): m.append(chunks[i]+' '+chunks[i+1]);i+=2
        else: m.append(chunks[i]);i+=1
    chunks=m;tot=sum(len(c) for c in chunks);bounds=[a];acc=0
    inner=[g for g in gaps if a<g[0] and g[1]<b]
    for cc in chunks[:-1]:
        acc+=len(cc);est=a+(b-a)*acc/tot
        cand=[g for g in inner if abs(g[1]-est)<1.0 and g[1]>bounds[-1]+.4]
        bounds.append(min(cand,key=lambda g:abs(g[1]-est))[1] if cand else est)
    bounds.append(b)
    for cc,s0,s1 in zip(chunks,bounds,bounds[1:]):
        subs.append([round(s0-.05+OFF,3),round(s1+.25+OFF,3),cc.replace('"','“',1).replace('"','”',1)])
for a_,b_ in zip(subs,subs[1:]): a_[1]=b_[0]
FPS=30;N=int(dur*FPS);env=[]
for f in range(N):
    t=f/FPS-OFF;i0=int(t*SR);sg=x[i0:i0+SR//FPS] if t>=0 else np.zeros(1)
    env.append(float(np.sqrt(np.mean(sg**2))) if len(sg) else 0.0)
e=np.array(env);e=np.clip(e/np.percentile(e[e>0.01],90),0,1)
seg=[0.0]+[round(s+OFF,3) for s in starts[1:]]+[round(dur,3)]
# início do cartão final = pausa antes de "Antecipe e conquiste"
last_gap=[g for g in gaps if g[1]<t1 and g[1]>starts[-1]][-1]
endfrac=(last_gap[1]+OFF-seg[9])/(seg[10]-seg[9])
json.dump({'seg':seg,'subs':subs,'env':[round(float(v),3) for v in e],'dur':round(dur,3),'off':OFF,'endfrac':round(endfrac,3)},open('tempos.json','w'),ensure_ascii=False)
print('dur',round(dur,2),'seg',seg,'endfrac',round(endfrac,3))
for s in subs: print(s)
