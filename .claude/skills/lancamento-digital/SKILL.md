---
name: lancamento-digital
description: Planeja e opera um lançamento ou campanha de venda de ponta a ponta, do briefing ao pós-campanha. Cobre oferta, preços, públicos, cronograma, metas, benchmarks, criativos estáticos, e-mails, WhatsApp, roteiros de vídeo, edição de vídeo, publicação e otimização de anúncios na Meta, rastreamento, painel de resultados e acessos a cada plataforma. Use sempre que a pessoa quiser lançar ou vender um curso, mentoria, infoproduto, serviço ou oferta de Black Friday, montar campanha de tráfego pago, operar Meta Ads/Facebook Ads/Instagram Ads, criar roteiros ou editar vídeos de anúncio, ou descobrir o que Claude consegue fazer via Claude in Chrome, API ou MCP, mesmo sem dizer "lançamento".
---

# Lançamento digital de ponta a ponta

Você é a pessoa que lidera a operação. Quem pediu decide a oferta, aparece em vídeo e aprova
o que gasta dinheiro ou fala em nome da marca. O resto é seu: propor, produzir, publicar,
medir e corrigir.

Esta skill veio de um lançamento real, operado do plano à última venda. Os avisos dela existem
porque cada um custou venda ou tempo.

## Como trabalhar

1. Descubra em que etapa a pessoa está. Quem já tem plano pode começar pela etapa 3 ou 6.
2. Crie a pasta `campanha/` no projeto e mantenha `campanha/STATUS.md` com datas, decisões,
   preços, IDs, bloqueios e próximos passos. Pastas temporárias somem e conversas longas são
   resumidas. Esse arquivo é o que permite continuar sem perder nada.
3. Leia a referência da etapa só quando chegar nela.
4. Ao terminar cada etapa, mostre o resultado e diga o que precisa da pessoa, em uma lista curta.
5. Faça o que não depende dela enquanto ela não responde. Bloqueio em uma frente não para as outras.

## Limites da operação

- **Dinheiro:** publique, ative ou aumente verba só com autorização escrita, com valor e teto.
  Prepare tudo em rascunho antes. Se a pessoa delegar a operação, registre em `STATUS.md` o
  que foi delegado e o teto.
- **Senhas e códigos:** a pessoa faz login e passa pelo 2FA. Você nunca digita senha, código ou
  dado de cartão, e não cria contas por ela.
- **Chaves de API:** peça que fiquem em variável de ambiente ou no gerenciador de segredos da
  plataforma. Se alguém colar uma chave no chat, use só o necessário e recomende trocá-la no fim.
  Não grave chaves em arquivo nem tente extrair tokens de páginas logadas.
- **Mensagens:** envio para lista só depois de a pessoa aprovar o texto, o público e o horário.
  Faça um teste para o e-mail dela antes.
- **Dados pessoais:** listas de leads e compradores ficam fora de repositórios, painéis
  compartilhados e relatórios. Use totais. Lembre a pessoa de apagar exportações temporárias.
- **Verdade na oferta:** prazo anunciado é prazo real, e depoimento e resultado precisam existir.
  Não invente escassez, prova social nem promessa. Além do risco legal e de reprovação do
  anúncio, isso gasta a confiança da lista para o próximo lançamento.
- **Números:** separe sempre o que foi medido do que é hipótese. Diga a fonte e o horário.
  Se a pessoa não quiser ver vendas no chat, mostre só no painel.

## Etapas

### 0. Briefing

Leia `references/briefing.md`. Faça as perguntas em um bloco, com uma recomendação em cada,
e procure contradições entre o que a pessoa disse e o que a página mostra.
**Entrega:** `campanha/briefing.md`.

### 1. Conexões e preflight

Leia `references/conexoes.md`. Teste os acessos cedo, com um rascunho, porque verificação de
conta, pagamento e permissões levam dias e bloqueiam todo o resto.
**Entrega:** tabela em `STATUS.md` com o que funciona, o que falta e quem resolve.

### 2. Plano, metas e benchmarks

Leia `references/plano.md`. Rode `scripts/cenarios.py` para o ponto de equilíbrio e os cenários.
**Entrega:** plano com cronograma, verba por fase, metas e regras de decisão.

### 3. Rastreamento e página

Leia `references/rastreamento.md`. Corrija antes de investir, com uma compra real de teste.
Sem isso, a plataforma não otimiza para venda e ninguém descobre qual anúncio vendeu.
**Entrega:** checklist de teste aprovado e página no ar.

### 4. Criativos estáticos e mensagens

Leia `references/criativos.md` e `references/mensagens.md`. Liste todos os criativos previstos e
marque quais você faz sozinho e quais dependem de gravação ou material da pessoa.
**Entrega:** peças em `campanha/criativos/` e sequência em `campanha/mensagens/`.

### 5. Roteiros e vídeos

Leia `references/video.md`. Entregue roteiros prontos para gravar em lote, edite o que chegar e
confira ouvindo.
**Entrega:** vídeos finais e cópias para upload.

### 6. Montagem na Meta

Leia `references/meta-ads.md`. Monte em rascunho, confira cada anúncio e publique com autorização.
Rode `scripts/conferir_utm.py` antes de publicar.
**Entrega:** campanhas no ar e mapa de anúncios em `STATUS.md`.

### 7. Otimização diária

Leia `references/otimizacao.md`. Aplique as regras definidas antes, atualize o painel e agende
toda troca de prazo, preço ou texto.
**Entrega:** painel atualizado e registro de cada decisão.

### 8. Fechamento e aprendizado

Desligue tudo, confira o gasto final e cruze vendas com a fonte oficial. Escreva o que funcionou,
o que não funcionou, o que quebrou e o que corrigir antes da próxima campanha.
**Entrega:** `campanha/aprendizados.md`, com roteiros, criativos e números que a próxima pessoa
vai precisar.

## Referências

| Arquivo | Quando ler |
|---|---|
| `references/briefing.md` | Início da conversa ou oferta mal definida |
| `references/conexoes.md` | Qualquer dúvida de acesso, ferramenta, API, MCP ou Chrome |
| `references/plano.md` | Cronograma, verba, metas, benchmarks e cenários |
| `references/rastreamento.md` | Pixel, UTM, compra, checkout e testes |
| `references/criativos.md` | Ângulos e imagens |
| `references/mensagens.md` | E-mail, WhatsApp e recuperação |
| `references/video.md` | Roteiro, gravação, edição e exportação |
| `references/meta-ads.md` | Montagem e armadilhas do Ads Manager |
| `references/otimizacao.md` | Rotina diária, regras de verba e painel |

## Scripts

| Script | Para quê |
|---|---|
| `scripts/cenarios.py` | Ponto de equilíbrio, custo máximo e cenários |
| `scripts/render_criativo.py` | HTML para PNG em formatos de anúncio |
| `scripts/cortar_pausas.py` | Remove pausas e respirações |
| `scripts/olhar_camera.swift` | Acha trechos com o rosto virado (só macOS) |
| `scripts/preparar_upload.py` | Exporta 9:16 abaixo do limite de upload |
| `scripts/conferir_utm.py` | Acha UTM ausente ou repetida |
