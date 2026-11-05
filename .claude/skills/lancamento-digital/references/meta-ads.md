# Montagem na Meta

## Estrutura

Separe por objetivo e temperatura, com nomes que digam fase, público e data.

| Campanha | Otimização | Público |
|---|---|---|
| Captação | Lead em formulário ou página | Frio |
| Lembrete | Visita ao grupo ou à página | Leads e lista |
| Venda quente | Compra, quando houver dado. Antes disso, visita à página | Lista, visitantes, engajamento, quem viu vídeo |
| Venda fria | Compra ou início de checkout | Amplo |

Sem compra chegando ao pixel, otimize pelo evento mais próximo com volume. Exclua compradores
e use públicos personalizados no quente. Coloque vários criativos por conjunto e deixe a entrega
concentrar nos melhores. Quente pequeno satura rápido: acompanhe a frequência.

## Fluxo seguro

1. Monte tudo em rascunho.
2. Suba as mídias na biblioteca.
3. Abra cada anúncio e confira a lista abaixo.
4. Rode `scripts/conferir_utm.py` em um CSV de `anuncio,url`.
5. Mostre o resumo com verba, teto, datas e públicos e peça autorização.
6. Publique, acompanhe a revisão e confira a entrega depois de uma hora.

## Conferência de cada anúncio

- [ ] Vídeo ou imagem certos, sem mídia relacionada indevida.
- [ ] Texto, título e prazo certos.
- [ ] URL e `utm_content` únicos.
- [ ] Página e Instagram certos.
- [ ] Melhorias automáticas desligadas, se a pessoa quer controle.
- [ ] Resumo do site, destaques e detalhes de app desligados.
- [ ] Sem peça ou texto vencido.

## Armadilhas do Ads Manager

- **Automação puxa lixo.** Melhorias do Advantage+, resumo do site, destaques e detalhes de app
  podem trazer promoção antiga, app errado e imagem vencida.
- **Upload pode entrar em anúncios ativos.** Desmarque "Publicar este carregamento nos anúncios ativos
  como mídia relacionada".
- **Mídia relacionada persiste.** Trocar o vídeo principal não apaga as extras.
- **Duplicar copia URL, UTM e mídia relacionada.** Ajuste os três.
- **Publicar em massa pode levar rascunhos antigos.** Em "Conferir itens de rascunho", desmarque tudo e
  marque só o que quer.
- **Editar vários anúncios muda o texto de todos.** Útil para troca de prazo, perigoso se forem diferentes.
- **Toda edição volta para revisão.** Conte alguns minutos sem entrega.
- **Hora de término pode voltar a 00:00.** Confira se ficou salva depois de agendar.
- **Teto da campanha é silencioso.** Ao subir verba diária, confira o teto.
- **Limite da conta e pagamento param tudo.** Olhe saldo e limite antes do pico.
- **Público por arquivo pode não ter campo de upload.** Se não tiver, use "colar valores" com a lista limpa.
- **Pixel pode recusar o domínio.** Confira a lista de domínios permitidos quando o script carrega e nada chega.

## Navegação pelo Chrome

- Use a URL para abrir colunas, ordem e seleção de campanhas, em vez de clicar em menus.
- A grade pode mostrar poucas linhas. Mude a ordenação ou filtre para ver as demais.
- Prefira leitura da página a capturas, e confira o nome do arquivo depois de trocar mídia.
- Rascunhos salvam sozinhos. Se a tela travar, recarregue antes de refazer.
- Faça uma alteração por vez e confirme. Lotes de cliques às cegas erram em silêncio.
