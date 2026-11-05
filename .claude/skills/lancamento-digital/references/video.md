# Roteiros e edição de vídeo

## Roteiros

Entregue no dia anterior à gravação, em um arquivo pronto para ler no celular:

- Ordem de gravação, agrupando por roupa e lugar.
- Para cada vídeo: objetivo, público, duração, gancho, corpo, chamada.
- Dois ou três ganchos alternativos, gravados no mesmo take.
- Linguagem falada, escrita como a pessoa fala.
- Sem data no vídeo, quando possível. Prazo em cartão fácil de trocar dura mais.

Estrutura de 20 a 45 segundos:

1. **Gancho em até 3 segundos.** Dor, número ou caso concreto.
2. **Prova ou exemplo.**
3. **O que a pessoa recebe.**
4. **Quebra da objeção principal.**
5. **Chamada e prazo.**

Diga que pode adaptar o texto. A versão natural costuma ficar melhor que o roteiro.

Dicas de gravação: celular em pé, boa luz de frente, olhar na lente, áudio perto da boca.
Se errar, pause e repita a frase inteira.

## Edição

Pergunte antes de baixar modelos ou programas. Dependências: `ffmpeg`, `whisper.cpp` e Python.

1. Corrija a rotação com `ffprobe`.
2. Transcreva:
   ```bash
   ffmpeg -nostdin -i bruto.mov -ar 16000 -ac 1 audio.wav
   whisper-cli -m modelo.bin -l pt -f audio.wav -ojf -osrt
   ```
   Use modelo grande para português e corrija nomes e termos com uma lista de troca.
3. Escolha os melhores takes pela transcrição e corte falsos começos.
4. Na gravação bruta, ache olhares para fora. No macOS:
   ```bash
   swift scripts/olhar_camera.swift bruto.mov
   ```
   Confira os trechos em quadros, porque a detecção é aproximada.
5. Corte pausas:
   ```bash
   python3 scripts/cortar_pausas.py take.mp4 cortado.mp4
   ```
6. Alterne zoom a cada corte, para esconder emendas e dar ritmo.
7. Adicione legenda, título e cartões. Renderize como PNG transparente e aplique com `overlay`.
   Isso funciona mesmo se o `ffmpeg` não tiver os filtros `subtitles` ou `ass`.
8. Normalize o áudio.
9. Exporte a cópia de upload:
   ```bash
   python3 scripts/preparar_upload.py final.mp4 upload/final.mp4
   ```

## Padrão de qualidade

- Sem pausa, suspiro ou respiração.
- Legenda no peito e cartões no terço superior. Nada sobre a boca.
- Olhar na câmera. Se o rosto virar, corte ou congele poucos quadros.
- Prints e mockups mostram o resultado prometido.
- Sem falso começo nem frase repetida.

## Conferência

- Ouça o vídeo. Whisper pode juntar um falso começo com a retomada, e a transcrição parece normal.
- Veja quadros do começo, de cada corte e do fim.
- Compare a duração da cópia com a do final.
- Em lote, use `-nostdin` no `ffmpeg`. Dentro de `while read`, ele consome a lista e gera arquivos
  truncados com nome errado.
- Rode um render pesado de cada vez se estiver operando o navegador.
