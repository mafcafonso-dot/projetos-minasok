import numpy as np
# (tempo da animação, tempo do vídeo) — encaixe na voz da Sofia (+0,5 s)
ANC=[(0,0),(4,2.94),(9,6.52),(12,8.54),(15,11.02),(17.8,12.96),(21,15.41),(26,19.66),(27.8,22.55),(30,26.5)]
A=np.array([a for a,_ in ANC]); V=np.array([v for _,v in ANC])
def anim(v): return float(np.interp(v,V,A))
def video(t): return float(np.interp(t,A,V))
DUR=26.5; OFF=0.5; FPS=30
