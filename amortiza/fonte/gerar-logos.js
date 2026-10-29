const fs = require('fs');
const opentype = require('opentype.js');
const { Resvg } = require('@resvg/resvg-js');

const AZUL = '#06449D';
const AMARELO = '#F7BC0A';
const BRANCO = '#FFFFFF';

const fred = opentype.parse(fs.readFileSync('node_modules/@fontsource/fredoka/files/fredoka-latin-600-normal.woff').buffer.slice(0));
const mont = opentype.parse(fs.readFileSync('node_modules/@fontsource/montserrat/files/montserrat-latin-600-normal.woff').buffer.slice(0));

// Texto convertido em contorno, centralizado em cx, com espaçamento extra (em unidades de px)
function textPath(font, text, size, cx, baseline, tracking = 0) {
  const glyphs = font.stringToGlyphs(text);
  const scale = size / font.unitsPerEm;
  let w = 0;
  glyphs.forEach((g, i) => { w += g.advanceWidth * scale + (i < glyphs.length - 1 ? tracking : 0); });
  let x = cx - w / 2;
  let d = '';
  const n = (v) => (Math.round(v * 100) / 100).toString();
  glyphs.forEach((g) => {
    for (const c of g.getPath(x, baseline, size).commands) {
      if (c.type === 'M' || c.type === 'L') d += c.type + n(c.x) + ' ' + n(c.y);
      else if (c.type === 'Q') d += 'Q' + n(c.x1) + ' ' + n(c.y1) + ' ' + n(c.x) + ' ' + n(c.y);
      else if (c.type === 'C') d += 'C' + n(c.x1) + ' ' + n(c.y1) + ' ' + n(c.x2) + ' ' + n(c.y2) + ' ' + n(c.x) + ' ' + n(c.y);
      else if (c.type === 'Z') d += 'Z';
    }
    x += g.advanceWidth * scale + tracking;
  });
  return { d, w };
}

// Casa: linha central do contorno, espessura T. Caixa 300 x 300.
const T = 40;
const casaLinha = 'M17 150 L150 27 L283 150 L283 283 L17 283 Z';
// Nível do amarelo: topo reto e horizontal a 2/3 da parte retangular interna
const internoBase = 283 - T / 2;      // 266
const internoTopoParede = 150 + T / 2; // ~167
const nivel = 178;

function casa({ contorno, vazio, nivelY = nivel, id = 'c' }) {
  return `
  <defs><clipPath id="${id}"><path d="${casaLinha}"/></clipPath></defs>
  ${vazio ? `<path d="${casaLinha}" fill="${vazio}"/>` : ''}
  <rect class="nivel" x="0" y="${nivelY.toFixed(1)}" width="300" height="${(300 - nivelY).toFixed(1)}" fill="${AMARELO}" clip-path="url(#${id})"/>
  <path d="${casaLinha}" fill="none" stroke="${contorno}" stroke-width="${T}" stroke-linejoin="miter" stroke-miterlimit="10"/>`;
}

function logo({ fundo, cor, slogan, nome }) {
  const W = 1000, H = 760;
  const palavra = textPath(fred, 'amortiza', 200, W / 2, 575, -2);
  const tag = textPath(mont, 'ANTECIPE E CONQUISTE', 36, W / 2, 665, 9);
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}">
  ${fundo ? `<rect width="${W}" height="${H}" fill="${fundo}"/>` : ''}
  <g transform="translate(${W / 2 - 140} 40) scale(${280 / 300})">${casa({ contorno: cor, id: 'c' + nome })}</g>
  <path d="${palavra.d}" fill="${cor}"/>
  <path d="${tag.d}" fill="${slogan}"/>
</svg>`;
  return svg;
}

function icone() {
  const S = 1024;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${S} ${S}" width="${S}" height="${S}">
  <rect width="${S}" height="${S}" rx="230" fill="${AZUL}"/>
  <g transform="translate(${S / 2 - 270} ${S / 2 - 285}) scale(${540 / 300})">${casa({ contorno: BRANCO, id: 'ci' })}</g>
</svg>`;
}

function simbolo() {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="300" height="300">${casa({ contorno: AZUL, id: 'cs' })}
</svg>`;
}

// Casa para o app: o nível é controlado pela variável --progresso (0 a 1)
function casaApp() {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="300" height="300">
  <!-- Para animar: mude o atributo "y" do retângulo .nivel.
       y = 263 - 209 * progresso   (0 = vazia, 1 = cheia até a ponta do telhado) -->
  <defs><clipPath id="casa"><path d="${casaLinha}"/></clipPath></defs>
  <path d="${casaLinha}" fill="${AMARELO}" fill-opacity="0.15"/>
  <rect class="nivel" x="0" y="${nivel.toFixed(1)}" width="300" height="300" fill="${AMARELO}" clip-path="url(#casa)"/>
  <path d="${casaLinha}" fill="none" stroke="${AZUL}" stroke-width="${T}" stroke-linejoin="miter"/>
</svg>`;
}

const out = 'saida';
fs.mkdirSync(out, { recursive: true });
const arquivos = {
  'amortiza-logo-fundo-branco.svg': logo({ fundo: BRANCO, cor: AZUL, slogan: AZUL, nome: 'b' }),
  'amortiza-logo-fundo-azul.svg': logo({ fundo: AZUL, cor: BRANCO, slogan: AMARELO, nome: 'a' }),
  'amortiza-icone.svg': icone(),
  'amortiza-casa-simbolo.svg': simbolo(),
  'amortiza-casa-app.svg': casaApp(),
};
for (const [nome, svg] of Object.entries(arquivos)) {
  fs.writeFileSync(`${out}/${nome}`, svg);
  const png = new Resvg(svg, { fitTo: { mode: 'width', value: nome.includes('casa') ? 600 : 2000 } }).render().asPng();
  fs.writeFileSync(`${out}/${nome.replace('.svg', '.png')}`, png);
}
console.log('ok', nivel);
