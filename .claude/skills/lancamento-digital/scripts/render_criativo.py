#!/usr/bin/env python3
"""Renderiza um HTML em PNG nos formatos de anuncio, com Chrome headless.

Exemplo:
  python3 render_criativo.py peca.html --formatos feed,story --saida criativos/
Formatos: feed (1080x1350), story (1080x1920), quadrado (1080x1080).
Tambem aceita LARGURAxALTURA, como 1200x628.
"""
import argparse, os, pathlib, platform, shutil, subprocess, sys, tempfile

FORMATOS = {"feed": (1080, 1350), "story": (1080, 1920), "quadrado": (1080, 1080)}

def achar_chrome():
    env = os.environ.get("CHROME_BIN")
    if env:
        return env
    if platform.system() == "Darwin":
        mac = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        if os.path.exists(mac):
            return mac
    if platform.system() == "Windows":
        for base in (os.environ.get("ProgramFiles", ""), os.environ.get("ProgramFiles(x86)", "")):
            win = os.path.join(base, "Google", "Chrome", "Application", "chrome.exe")
            if os.path.exists(win):
                return win
    for nome in ("google-chrome", "chromium", "chromium-browser", "chrome"):
        achado = shutil.which(nome)
        if achado:
            return achado
    sys.exit("Chrome nao encontrado. Defina CHROME_BIN com o caminho do executavel.")

def tamanho(nome):
    if nome in FORMATOS:
        return FORMATOS[nome]
    try:
        w, h = nome.lower().split("x")
        return int(w), int(h)
    except ValueError:
        sys.exit(f"Formato invalido: {nome}")

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("html")
    p.add_argument("--formatos", default="feed,story")
    p.add_argument("--saida", default=".")
    a = p.parse_args()
    fonte = pathlib.Path(a.html).resolve()
    if not fonte.exists():
        sys.exit(f"Arquivo nao encontrado: {fonte}")
    destino = pathlib.Path(a.saida)
    destino.mkdir(parents=True, exist_ok=True)
    chrome = achar_chrome()
    for nome in a.formatos.split(","):
        w, h = tamanho(nome.strip())
        png = (destino / f"{fonte.stem}_{nome.strip()}.png").resolve()
        # Perfil proprio: evita conflito com o Chrome em uso e com outros renders.
        with tempfile.TemporaryDirectory() as perfil:
            for tentativa in range(3):
                r = subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                                    "--force-device-scale-factor=1", f"--user-data-dir={perfil}",
                                    f"--window-size={w},{h}", "--virtual-time-budget=4000",
                                    f"--screenshot={png}", fonte.as_uri()],
                                   capture_output=True, text=True, timeout=120, stdin=subprocess.DEVNULL)
                if png.exists() and png.stat().st_size > 0:
                    break
            else:
                sys.exit(f"Falha ao renderizar {png.name}: {r.stderr[-400:]}")
        print(f"{png} ({w}x{h})")

if __name__ == "__main__":
    main()
