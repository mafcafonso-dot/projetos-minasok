# Amortiza Minas Ok – regras e decisões

Simulador público (link único enviado a cada cliente) só para o parcelamento da entrada com a Minas Ok. O cliente preenche os próprios dados; nada é salvo e não há base de clientes. Objetivo: a Minas Ok receber antes e reduzir atrasos e calotes.

- Site publicado (para os clientes): https://amortiza-minasok.lovable.app (projeto "Amortiza Minasok" no Lovable)
- Versão nova (Vercel, publicada a partir deste repositório): https://projetos-minasok.vercel.app — cada push na `main` publica de novo
- Versão de trabalho: `app/index.html` nesta pasta (mesma versão do artefato no Claude: https://claude.ai/artifact/WvT4HYVfGXoyhsYrhuo5te)
- Botão "QUERO AMORTIZAR!": abre o WhatsApp da Minas Ok (34) 3831-3999 com a simulação já escrita; se houver atraso, a mensagem pede regularização.

## Dados que o cliente preenche
- Valor parcelado, quantidade de parcelas, mensais ou anuais, data da 1ª parcela, data da última parcela paga, juros ao mês (padrão 1%).
- "Como são as suas parcelas?": todas com o mesmo valor (calculado pela Price) ou faixas de valor (quantas faixas forem precisas, cada uma com quantidade e valor, na ordem do contrato). O app confere se as faixas somam a quantidade de parcelas e se batem com o valor parcelado a 1% ao mês.
- Aditivo de suspensão: vencimento da 1ª parcela pausada e quantas foram pausadas.
- Para adiantar: quanto tem disponível e a data em que vai pagar.

## Regras (conforme as confissões de dívida do Jardim Amaral)
- Juros de 1% ao mês, tabela Price. Nos 22 contratos o valor parcelado bate com o valor presente das parcelas.
- Antecipação: sempre em parcelas inteiras, das últimas para as primeiras, só para quem está em dia. O cliente paga um valor exato (valor presente com desconto de 1% ao mês, contado por dia até cada vencimento, na data de pagamento escolhida). A Minas Ok emite um boleto com esse valor e cancela no banco os boletos das parcelas adiantadas. A parcela do mês não muda e o contrato termina antes. O desconto é política da Minas Ok (as confissões não têm cláusula de antecipação).
- Não existe plano de "valor por mês": ele gerava pagamentos que não fecham parcelas inteiras e impedia cancelar boletos já emitidos.
- Atraso: multa de 2% + juros de mora de 1% ao mês pro rata die por parcela vencida. Com 3 parcelas seguidas em atraso, o contrato prevê vencimento antecipado (multa de 10% e honorários de 20%).
- Aditivo de suspensão: as parcelas do período ficam pausadas sem juros nem multa e passam para o fim do contrato, pelo mesmo valor nominal, vencendo mensalmente após a última parcela original.
- Parcelas anuais (ex.: 5 parcelas anuais): mesma regra de 1% ao mês; a 1ª parcela vence na data-base.

## Decisões tomadas
- Base de dados individual por cliente descartada; o cliente preenche os próprios dados.
- Diferenças de 1 centavo entre aditivo e contrato: ignoradas.
- Parcelas suspensas por aditivo: valor nominal, sem correção.
- Plano de adiantamento mensal removido; antecipação só em parcelas inteiras com valor exato.
- Aba "Financiamento da Caixa" removida: o app trata só do parcelamento com a Minas Ok.
- Título do topo: "Amortize suas parcelas, economize seu dinheiro!"

## Identidade visual
- Conceito: a marca é uma casa que se completa conforme o cliente paga — "barra de progresso emocional".
- Nome em minúsculas "amortiza", slogan "ANTECIPE E CONQUISTE".
- Cores: azul #06449D e amarelo #F7BC0A (conferir com as oficiais da Minas Ok).
- Fontes: Fredoka (nome e títulos) e Montserrat (slogan e textos).
- Casa em traço grosso, topo do amarelo reto e horizontal. Na marca oficial o amarelo fica parado em 2/3 da parede.
- Mascote: a mesma casa com perninhas e olhos, dando saltinhos e piscando (`marca/mascote-*.svg`, GIF e MP4).
- No app: número grande no centro = parcelas que FALTAM ("parcelas para ser sua"); preenchimento proporcional a parcelas quitadas ÷ total (incluindo as pausadas por aditivo). Ao simular antecipação, o amarelo sobe e o número desce contando. Nível do amarelo: y = 263 − 209 × progresso.
- Conquista (faltam 0): casa toda amarela, aparece "SUA." e as janelas acendem.
- Cliente em atraso: a casa não esvazia; só aparece um selo âmbar para regularizar.
- Botão "Compartilhar minha casa": imagem 1080×1080 sem valores nem dados pessoais.
- Logo da Construtora Minas Ok pequeno no canto superior direito.

## Situação em 29/10/2026
- `app/index.html` já tem a identidade, o mascote, a casa de progresso, a conquista, o aviso de atraso e o compartilhar.
- No Lovable as mudanças foram aplicadas na prévia, mas ainda não publicadas. Falta levar o mascote animado, o logo da Minas Ok à direita, o parágrafo do topo e o tamanho da casa.
- Em aberto: o compartilhar mostra o número depois da antecipação simulada; a sugestão é mostrar a situação de hoje.

## Referência (fora do app): contratos da Caixa
- MCMV: saldo B.5.1, juros B.8 (efetiva a.m.), prazo B.7.3, sistema B.3, índice TR (cláusula 9), desconto FGTS/União B.4.5 (se > 0, devolução proporcional ao amortizar até o 5º ano, cláusula 1.4).
- SBPE: saldo C3.1, juros C7.1 (a.m.), prazo C6.2, sistema C5, índice C5.1 (TR); sem desconto do FGTS.
