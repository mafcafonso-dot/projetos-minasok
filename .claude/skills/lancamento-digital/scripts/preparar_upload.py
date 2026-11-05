#!/usr/bin/env python3
"""Exporta video 9:16 abaixo de um limite de tamanho, para subir pelo navegador.

Exemplo:
  python3 preparar_upload.py editado.mp4 upload/editado.mp4 --limite-mb 9.5
Reduz o bitrate ate caber e confere se a duracao continua igual a do original.
"""
import argparse, json, os, pathlib, subprocess, sys

def probe(arq):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", arq],
                       capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL)
    return float(json.loads(r.stdout)["format"]["duration"])

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("entrada"); p.add_argument("saida")
    p.add_argument("--limite-mb", type=float, default=9.5)
    p.add_argument("--largura", type=int, default=1080)
    p.add_argument("--altura", type=int, default=1920)
    a = p.parse_args()
    dur = probe(a.entrada)
    pathlib.Path(a.saida).parent.mkdir(parents=True, exist_ok=True)
    audio = 128
    alvo = a.limite_mb * 8192 / dur - audio
    vf = (f"scale={a.largura}:{a.altura}:force_original_aspect_ratio=increase,"
          f"crop={a.largura}:{a.altura},setsar=1")
    for fator in (0.95, 0.85, 0.75, 0.65):
        kbps = int(alvo * fator)
        if kbps < 300:
            sys.exit("Video longo demais para o limite sem perder qualidade. Encurte ou suba o limite.")
        subprocess.run(["ffmpeg", "-nostdin", "-y", "-hide_banner", "-loglevel", "error", "-i", a.entrada,
                        "-vf", vf, "-c:v", "libx264", "-preset", "medium", "-b:v", f"{kbps}k",
                        "-maxrate", f"{int(kbps * 1.3)}k", "-bufsize", f"{kbps * 2}k", "-pix_fmt", "yuv420p",
                        "-c:a", "aac", "-b:a", f"{audio}k", "-movflags", "+faststart", a.saida], check=True)
        mb = os.path.getsize(a.saida) / 1048576
        if mb <= a.limite_mb:
            nova = probe(a.saida)
            if abs(nova - dur) > 0.25:
                sys.exit(f"Duracao mudou: {dur:.2f}s -> {nova:.2f}s. Confira o arquivo.")
            print(f"{a.saida}: {mb:.2f} MB, {nova:.1f}s, {kbps} kbps")
            return
    sys.exit("Nao coube no limite. Encurte o video ou suba o limite.")

if __name__ == "__main__":
    main()
