# amortiza — Minas Ok

Simulador para o cliente da Construtora Minas Ok adiantar parcelas da entrada com desconto de juros.
A marca é uma casa que se completa conforme o cliente paga.

- App publicado: https://amortiza-minasok.lovable.app
- Regras de cálculo e decisões: [docs/regras.md](docs/regras.md)

## Pastas

| Pasta | O que tem |
|---|---|
| `app/` | `index.html` — versão de trabalho completa do simulador (abre direto no navegador) |
| `marca/` | Logomarca (fundo branco e azul), ícone do app, casa-símbolo, casa para animação, mascote (parado e animado, SVG, GIF e MP4) e logo da construtora |
| `divulgacao/` | Post para Instagram/Facebook (1080×1350) |
| `docs/` | Regras do parcelamento, identidade visual e situação do projeto |
| `fonte/` | Scripts que geraram as logos, o mascote e o post (Node + Python/Playwright) |

## Cores e fontes

- Azul `#06449D` · Amarelo `#F7BC0A`
- Fredoka (nome e títulos) · Montserrat (textos)

## Observações

- Os scripts de `fonte/` foram escritos para o ambiente onde a marca foi criada: precisam de `opentype.js`, `@fontsource/fredoka`, `@fontsource/montserrat`, `@resvg/resvg-js` e Playwright, e os caminhos de entrada podem precisar de ajuste.
- O logo da construtora em `marca/` foi recortado do app publicado (335 px de largura). Para impressão, use o arquivo original da Minas Ok.
