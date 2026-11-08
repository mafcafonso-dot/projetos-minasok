# Vídeo "Como usar o amortiza" (32 s, versão de 08/11/2026)

A casinha explica os 4 passos em balões de texto (sem narração), com o app de verdade no celular usando o contrato fictício (CPF 111.111.111-11, código DEMO-2026).

Para refazer, numa pasta com `comp.html`, `masc.js`, `render.py`, `som.py`, uma cópia do app como `app.html`, o logo da Minas Ok como `logo.png` e as fontes (`npm i @fontsource/fredoka @fontsource/montserrat`):

    python3 render.py video.mp4      # quadros (grava tempos.json)
    python3 som.py                   # trilha sintetizada + toques -> som.wav
    ffmpeg -i video.mp4 -i som.wav -c:v copy -c:a aac -shortest -movflags +faststart amortiza-como-usar.mp4

Os textos dos balões e os tempos ficam no começo de `comp.html` (FALAS e S).
