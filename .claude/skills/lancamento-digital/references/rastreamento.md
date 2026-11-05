# Rastreamento e página

Se a compra não chega à plataforma de anúncios, ela não otimiza para venda. Se a venda não guarda
a origem, ninguém sabe qual anúncio vendeu. Foram as duas lacunas mais caras do lançamento de origem.

## Mínimo antes de investir

- Pixel na página, na conta de anúncios certa, com o domínio autorizado.
- **Compra enviada pelo servidor** (Conversions API) a partir do webhook do checkout, com valor e
  ID do evento. Não dependa só da página de obrigado, que pode quebrar.
- UTM salva no navegador e repassada ao checkout, para constar na venda.
- `utm_content` único por anúncio. Duplicar anúncio copia a URL.
- Eventos de página: visita, chegou ao preço, clicou em comprar, compra.
- Uma fonte oficial de vendas, definida antes de começar.
- Captura de contato antes do pagamento, quando o checkout permitir.

## Compra de teste

Faça com a pessoa, com um produto de valor baixo ou cupom, antes de publicar e depois de qualquer
mudança no site ou no checkout. Confira:

- [ ] Pagamento aprovado no checkout.
- [ ] Webhook recebido, sem erro.
- [ ] Compra apareceu nas ferramentas da Meta, com valor.
- [ ] Compra apareceu na análise do site, com a UTM.
- [ ] E-mail de boas-vindas chegou.
- [ ] Página de obrigado abriu e não conta duas vezes ao recarregar.
- [ ] Tudo funcionou no celular, inclusive Pix ou boleto.

## Página

- A maior parte do tráfego de anúncios costuma vir de celular, e quase sempre converte menos.
  Teste o caminho até o pagamento em um celular real.
- Preço, data e botões devem mudar sozinhos na hora marcada. Teste com a data simulada.
- Antes da abertura, os botões levam à inscrição da aula. Depois, ao checkout. Depois do fechamento, à lista de espera.
- Use domínio próprio. Faça as mudanças em branch ou pull request e teste antes de publicar.
- Desative os links antigos do checkout quando o preço mudar. Quem tem o link ainda consegue pagar.

## Leitura dos dados

Anote em cada número sua fonte e seu horário. Lembre que ROAS geral inclui lista e orgânico, não só
anúncios. E-mail de confirmação pode atrasar, então a hora dele não é a hora da venda.
