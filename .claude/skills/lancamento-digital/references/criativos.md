# Criativos e ângulos

## Inventário

Faça uma tabela com código, fase, público, formato, ângulo, responsável e status. Marque cada
peça como "Claude faz", "precisa gravar" ou "precisa de material". Assim a pessoa vê de uma vez o que depende dela.

## Ângulos que mais renderam

- **Objeção respondida:** "não entendo de tecnologia", "não tenho tempo", "é caro".
- **Caso concreto com número no gancho:** um resultado específico vence uma promessa geral.
- **Dor de trabalho:** reconhecimento, perda de vaga, chefe, cliente.
- **Conta do preço:** horas ou dinheiro devolvidos, comparados ao valor.
- **Prazo real:** motivo claro para agir agora.

## Ângulos mais fracos

- Anúncio que só anuncia, como "matrículas abertas".
- Nicho genérico sem dor clara.
- Corte de live mostrando processo. Prometer o resultado rendeu mais que mostrar como se faz.
- Criativo novo no último dia: não dá tempo de aprender.

Teste, não copie. Isso vale para o público de origem. Use-o como primeira hipótese.

## Pesquisa de linguagem

Busque como o público fala em comentários, avaliações, perguntas de lives e mensagens recebidas.
Não apresente paráfrase como citação de pessoa real. Use a Biblioteca de Anúncios para ver a concorrência.

## Peças estáticas

Sem gerador de imagem, faça em HTML e SVG e renderize:

```bash
python3 scripts/render_criativo.py peca.html --formatos feed,story --saida campanha/criativos
```

Regras:

- Uma ideia por peça. Título legível no celular.
- Mantenha texto longe das bordas e das áreas cobertas pela interface do story.
- Se houver data ou preço, inclua no nome do arquivo. Isso evita subir peça vencida.
- Gere versões por público trocando só o exemplo concreto.
- Mostre o resultado prometido em print ou mockup.
- Respeite a lista de termos proibidos do briefing, em texto e imagem.
- Use imagem própria, licenciada ou gerada. Peça autorização para usar rosto e depoimento.

## Texto do anúncio

Primeira linha com gancho, depois benefício concreto, prova, prazo e chamada. Evite promessa de
ganho garantido e referência a características pessoais do leitor, que costumam ser reprovadas.
Crie versões por fase e guarde quais textos têm prazo, para trocar na hora certa.
