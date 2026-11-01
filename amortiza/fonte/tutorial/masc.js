const W=1080,H=1920,GY=1330;
const AZ='#06449D',AM='#F7BC0A',NV='#0B2547',VD='#1B7F45',VM='#C0392B',CL='#DCEBFB';
const F='font-family:Fredoka;font-weight:600', FB='font-family:Fredoka;font-weight:700';
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const seg=(t,a,b)=>clamp((t-a)/(b-a));
const lerp=(a,b,k)=>a+(b-a)*k;
const eo=x=>1-Math.pow(1-x,3);
const eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const back=x=>{const c1=1.9,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const rnd=i=>{const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);};
const HOUSE='M17 150 L150 27 L283 150 L283 283 L17 283 Z';
let UID=0, AMP=0;

/* ---------------- personagem ---------------- */
function armGeo(side,a){ // a: graus a partir de "para baixo", para fora
  const r=a*Math.PI/180, sx=side<0?-4:304, sy=215, L=82;
  const hx=sx+side*Math.sin(r)*L, hy=sy+Math.cos(r)*L;
  const mx=(sx+hx)/2, my=(sy+hy)/2, nx=-(hy-sy)/L, ny=(hx-sx)/L;
  const b=16*side; return {sx,sy,hx,hy,cx:mx+nx*b,cy:my+ny*b};
}
function handPos(o,side){const s=o.s||1,g=armGeo(side,side<0?(o.armL??15):(o.armR??15));return [o.x+(g.hx-150)*s,o.y+(g.hy-365)*s];}
function masc(o){
  const id='c'+(UID++), s=o.s||1, sx=o.sx||1, sy=o.sy||1, fill=o.fill??.35, lvl=263-209*fill, lx=(o.look||0)*6;
  const eyes=o.eyes||'normal', blink=o.blink&&eyes!=='happy';
  let mouth=o.mouth||'smile'; if(o.lip!==false){if(AMP>.42)mouth='open';else if(AMP>.16)mouth='openS';}
  const leg=(x,dx,rot)=>`<g transform="rotate(${rot} ${x} 296)"><rect x="${x-12}" y="288" width="24" height="60" rx="12" fill="${AZ}" stroke="${NV}" stroke-width="7"/><ellipse cx="${x+dx}" cy="352" rx="29" ry="14" fill="${AZ}" stroke="${NV}" stroke-width="7"/></g>`;
  const arm=(side,a)=>{const g=armGeo(side,a),d=`M${g.sx} ${g.sy} Q${g.cx} ${g.cy} ${g.hx} ${g.hy}`;
    return `<path d="${d}" fill="none" stroke="${NV}" stroke-width="26" stroke-linecap="round"/><path d="${d}" fill="none" stroke="${AZ}" stroke-width="13" stroke-linecap="round"/><circle cx="${g.hx}" cy="${g.hy}" r="18" fill="${AZ}" stroke="${NV}" stroke-width="6"/>`;};
  const eye=(cx,side)=>{
    if(eyes==='happy') return `<path d="M${cx-21} 140 Q${cx} 102 ${cx+21} 140" fill="none" stroke="${NV}" stroke-width="10" stroke-linecap="round"/>`;
    if(blink) return `<path d="M${cx-21} 130 Q${cx} 142 ${cx+21} 130" fill="none" stroke="${NV}" stroke-width="9" stroke-linecap="round"/>`;
    let e=`<ellipse cx="${cx}" cy="128" rx="22" ry="27" fill="#fff" stroke="${NV}" stroke-width="7"/><circle cx="${cx+4+lx}" cy="134" r="12" fill="${NV}"/><circle cx="${cx+8+lx}" cy="129" r="4" fill="#fff"/>`;
    if(eyes==='tired') e+=`<rect x="${cx-26}" y="96" width="52" height="32" fill="#AFC4E3" clip-path="url(#${id}${side})"/><line x1="${cx-22}" y1="128" x2="${cx+22}" y2="128" stroke="${NV}" stroke-width="6" stroke-linecap="round"/>`;
    return e;};
  const brows={determined:`<path d="M88 90 L138 106 M212 90 L162 106"/>`,tired:`<path d="M90 102 L136 88 M210 102 L164 88"/>`}[eyes]||'';
  const M={smile:`<path d="M128 184 Q150 206 172 184" fill="none" stroke="${NV}" stroke-width="7" stroke-linecap="round"/>`,
    open:`<path d="M126 180 Q150 224 174 180 Z" fill="${NV}" stroke="${NV}" stroke-width="5" stroke-linejoin="round"/><path d="M137 201 Q150 214 163 201 Q150 196 137 201Z" fill="#E8697B"/>`,
    frown:`<path d="M130 200 Q150 182 170 200" fill="none" stroke="${NV}" stroke-width="7" stroke-linecap="round"/>`,
    wavy:`<path d="M124 194 q7 -7 13 0 t13 0 t13 0 t13 0" fill="none" stroke="${NV}" stroke-width="6" stroke-linecap="round"/>`,
    openS:`<ellipse cx="150" cy="192" rx="15" ry="10" fill="${NV}"/>`,
    grin:`<path d="M118 178 Q150 228 182 178 Z" fill="${NV}" stroke="${NV}" stroke-width="5" stroke-linejoin="round"/><path d="M124 181 L176 181 L171 191 L129 191Z" fill="#fff"/>`}[mouth];
  let g=`<defs><clipPath id="${id}"><path d="${HOUSE}"/></clipPath><clipPath id="${id}L"><ellipse cx="116" cy="128" rx="22" ry="27"/></clipPath><clipPath id="${id}R"><ellipse cx="184" cy="128" rx="22" ry="27"/></clipPath></defs>`;
  g+=leg(108,-10,o.legL||0)+leg(192,10,o.legR||0);
  g+=`<path d="${HOUSE}" fill="#fff"/><rect x="-10" y="${lvl}" width="320" height="330" fill="${AM}" clip-path="url(#${id})"/>`;
  if(o.win){g+=`<g opacity="${o.win}"><circle cx="71" cy="231" r="40" fill="#fff" opacity=".55"/><circle cx="229" cy="231" r="40" fill="#fff" opacity=".55"/><rect x="54" y="214" width="34" height="34" rx="5" fill="#fff" stroke="${NV}" stroke-width="5"/><rect x="212" y="214" width="34" height="34" rx="5" fill="#fff" stroke="${NV}" stroke-width="5"/></g>`;}
  g+=`<path d="${HOUSE}" fill="none" stroke="${NV}" stroke-width="56" stroke-linejoin="round"/><path d="${HOUSE}" fill="none" stroke="${AZ}" stroke-width="40" stroke-linejoin="round"/>`;
  g+=arm(-1,o.armL??15)+arm(1,o.armR??15);
  g+=eye(116,'L')+eye(184,'R')+`<g fill="none" stroke="${NV}" stroke-width="9" stroke-linecap="round">${brows}</g>`+M;
  if(o.sweat) g+=`<path d="M262 64 q16 24 0 34 q-16 -10 0 -34z" fill="#8FD0FA" stroke="${NV}" stroke-width="5" opacity="${o.sweat}"/>`;
  return `<g transform="translate(${o.x-150*s} ${o.y-365*s}) scale(${s}) rotate(${o.rot||0} 150 365) translate(150 365) scale(${sx} ${sy}) translate(-150 -365)">${g}</g>`;
}
