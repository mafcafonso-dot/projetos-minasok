# Vídeo "Como usar o amortiza" (44 s, versão de 08/11/2026)

A casinha explica os 4 passos com a voz da Sofia (ElevenLabs, Eleven v4, estabilidade 50%, similaridade 75%), a boca sincronizada com a fala e as frases em balões. Trilha: "Warm Welcome" (ElevenLabs Music), em loop com transição. No celular aparece o app de verdade com o contrato fictício (CPF 111.111.111-11, código DEMO-2026).

Roteiro falado:
Oi! Eu sou a casinha do amortiza. Vou te mostrar como usar o app em quatro passos... Primeiro: a Minas Ok manda o seu código pelo WhatsApp. Ainda não recebeu? É só pedir pra gente... Depois, entre no app com o seu CPF e o código. O seu contrato já aparece prontinho... Agora, coloque a data da última parcela que você pagou. O app confere se você está em dia... Se tiver atraso, ele mostra o valor para regularizar, como está no seu contrato. Se estiver em dia, é só escolher quanto quer adiantar... Gostou? Toque em Quero amortizar. A Minas Ok confere e te manda o boleto. Antecipe e conquiste!

Para refazer, numa pasta com `comp.html`, `masc.js`, `render.py`, `som.py`, uma cópia do app como `app.html`, o logo da Minas Ok como `logo.png`, `voz.wav`, `musica.wav`, `env.json` (envelope da voz por quadro, 30 fps, voz começando em 0,3 s) e as fontes (`npm i @fontsource/fredoka @fontsource/montserrat`):

    python3 render.py video.mp4      # quadros (grava tempos.json)
    python3 som.py                   # voz + trilha + toques -> som.wav
    ffmpeg -i video.mp4 -i som.wav -c:v copy -c:a aac -shortest -movflags +faststart amortiza-como-usar.mp4

Os tempos das frases ficam no começo de `comp.html` (S e FALAS), tirados das pausas da fala.
