#!/usr/bin/env python3
"""Remove pausas e respiracoes de uma gravacao, com ffmpeg.

Exemplo:
  python3 cortar_pausas.py gravacao.mp4 cortado.mp4 --ruido -32 --minimo 0.28 --margem 0.06
Se cortar o fim de palavras, aumente --margem. Se sobrar respiracao, suba --ruido.
Confira ouvindo: silencio nao detecta falso comeco nem frase repetida.
"""
import argparse, json, re, subprocess, sys

def duracao(arq):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", arq],
                       capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL)
    return float(json.loads(r.stdout)["format"]["duration"])

def silencios(arq, ruido, minimo):
    r = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-i", arq, "-af",
                        f"silencedetect=noise={ruido}dB:d={minimo}", "-f", "null", "-"],
                       capture_output=True, text=True)
    ini = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", r.stderr)]
    fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    return list(zip(ini, fim))

def trechos_falados(total, sil, margem):
    trechos, pos = [], 0.0
    for ini, fim in sil:
        a, b = pos, min(ini + margem, total)
        if b - a > 0.08:
            trechos.append((a, b))
        pos = max(fim - margem, 0.0)
    if total - pos > 0.08:
        trechos.append((pos, total))
    return trechos

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("entrada"); p.add_argument("saida")
    p.add_argument("--ruido", type=float, default=-32, help="limite de silencio em dB")
    p.add_argument("--minimo", type=float, default=0.28, help="pausa minima cortada, em segundos")
    p.add_argument("--margem", type=float, default=0.06, help="respiro mantido em cada corte, em segundos")
    a = p.parse_args()
    total = duracao(a.entrada)
    trechos = trechos_falados(total, silencios(a.entrada, a.ruido, a.minimo), a.margem)
    if not trechos:
        sys.exit("Nenhum trecho falado encontrado. Revise --ruido.")
    partes = []
    for i, (ini, fim) in enumerate(trechos):
        partes.append(f"[0:v]trim=start={ini:.3f}:end={fim:.3f},setpts=PTS-STARTPTS[v{i}];"
                      f"[0:a]atrim=start={ini:.3f}:end={fim:.3f},asetpts=PTS-STARTPTS[a{i}];")
    pares = "".join(f"[v{i}][a{i}]" for i in range(len(trechos)))
    filtro = "".join(partes) + f"{pares}concat=n={len(trechos)}:v=1:a=1[v][a]"
    subprocess.run(["ffmpeg", "-nostdin", "-y", "-hide_banner", "-loglevel", "error", "-i", a.entrada,
                    "-filter_complex", filtro, "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "160k",
                    a.saida], check=True)
    novo = duracao(a.saida)
    print(f"{len(trechos)} trechos. {total:.1f}s -> {novo:.1f}s ({total - novo:.1f}s removidos)")

if __name__ == "__main__":
    main()
