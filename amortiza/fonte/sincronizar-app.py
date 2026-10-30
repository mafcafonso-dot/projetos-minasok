"""Copia a versão de trabalho (artefato) para o repositório, com os ajustes de site:
- fora do Claude, o compartilhar baixa o PNG direto;
- título, ícone e prévia de link (WhatsApp/redes) dentro do <head>."""
import pathlib
SRC = pathlib.Path('/home/claude/artefato/amortiza-minas-ok.html')
DST = pathlib.Path('/home/claude/projetos-minasok/amortiza/app/index.html')
s = SRC.read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)

rep("  const dl=window.claude&&await window.claude.use('downloads');\n  if(!dl){$('casa-share').hidden=true;return;}",
    "  const dl=window.claude&&await window.claude.use('downloads');\n  if(!dl){const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='minha-casa-amortiza.png';document.body.appendChild(a);a.click();a.remove();return;}")

URL = 'https://projetos-minasok.vercel.app'
head = f'''<title>amortiza | Minas Ok</title>
<link rel="icon" type="image/svg+xml" href="/amortiza/marca/amortiza-icone.svg">
<link rel="apple-touch-icon" href="/amortiza/marca/amortiza-icone.png">
<meta name="description" content="Simule quanto você economiza adiantando as parcelas da sua entrada com a Construtora Minas Ok.">
<meta property="og:title" content="amortiza | Minas Ok">
<meta property="og:description" content="Antecipe e conquiste: veja quanto você economiza adiantando suas parcelas.">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}/">
<meta property="og:image" content="{URL}/amortiza/marca/logo-amortiza-mascote-fundo-azul.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="700">
<meta name="twitter:card" content="summary_large_image">'''
rep('<title>Amortiza Minas Ok</title>\n', '')
rep('</style></head><body>', '</style>\n' + head + '\n</head><body>')
DST.write_text(s)
print('ok', DST, len(s))
