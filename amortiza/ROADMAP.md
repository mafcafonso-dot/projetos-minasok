# Roadmap — amortiza | Minas Ok

> **Antecipe e conquiste.** Simulador para o cliente da Construtora Minas Ok adiantar as parcelas da entrada
> com desconto de 1% ao mês e terminar de pagar antes. Para a Minas Ok: receber antes e reduzir atrasos.

- App: https://projetos-minasok.vercel.app
- Apresentação: https://projetos-minasok.vercel.app/apresentacao (demonstração: https://projetos-minasok.vercel.app/?demo)
- Regras de cálculo e decisões: [docs/regras.md](docs/regras.md)
- Contratos dos clientes: repositório **privado** `mafcafonso-dot/amortiza-contratos`

Atualizado em 04/11/2026. Para continuar o trabalho em outra sessão, veja **Regras para o Claude** abaixo.

---

## ✅ Feito

### 1. Simulador
- Parcelamento da entrada com a construtora: tabela Price, 1% ao mês, parcelas mensais ou anuais.
- Parcelas com valores diferentes (faixas), com conferência automática contra o valor parcelado.
- Aditivo de suspensão: o cliente informa a 1ª e a última parcela pausada; o app conta e move para o fim.
- Antecipação sempre em parcelas inteiras, do fim para o começo, com valor exato na data do pagamento.
- "Já adiantei parcelas antes" para quem antecipa mais de uma vez.
- Atraso: multa de 2% + juros de mora, aviso de vencimento antecipado (3 parcelas) e pedido para regularizar.
- Parcela única (balão): tem juros embutidos como as demais; paga, vencida ou a vencer conforme a data do
  último pagamento; pode ser adiantada com 1% a.m. (conferido num contrato real: total confessado = parcelas + balão a valor presente).
- Botão "QUERO AMORTIZAR!" manda a simulação pronta para o WhatsApp da Minas Ok.
- 04/11/2026: redesign com a skill unslop (fundo sem ícones, cores calmas, vermelho só para atraso, amarelo só na casinha) no app e na apresentação.

### 2. Marca e identidade
- Logo, ícone, casa-símbolo que se enche de amarelo conforme o cliente paga.
- Mascote (casinha com perninhas e olhos) animado; conquista ao quitar ("SUA.").
- Textos simples para quem tem pouca leitura ("Você quita o seu imóvel X meses antes").

### 3. Publicação
- Código no GitHub (`projetos-minasok`) com publicação automática no Vercel.
- `.vercelignore`: o site publica só `amortiza/app`, `apresentacao`, `marca` e `divulgacao`; docs, roadmap, scripts e skills ficam fora do ar.
- Cabeçalhos de segurança no `vercel.json` (nosniff, referrer, o app só abre dentro do próprio site).
- Página de apresentação com o app aberto em modo demonstração (contrato fictício).

### 4. Divulgação
- Vídeo de lançamento (26 s, voz Sofia/ElevenLabs, trilha calma) e post.
- Envio individual pelo WhatsApp: 78 clientes "em dia" da lista principal + 8 do Jardim dos Jatobás.
- Vídeo tutorial "como usar" (1min12s) enviado por lista de transmissão.

### 5. Contrato do cliente já carregado (CPF + código)
- Cliente entra com CPF + código de 8 ou 10 caracteres e vê o próprio contrato; preenche só a data do último pagamento.
- Contratos ficam no repositório privado; no app público vai só o pacote **criptografado** (AES-GCM + PBKDF2).
- Quem não tem código continua preenchendo à mão (o app de antes continua igual).
- Lista de acesso (CPF + código por cliente) para a Minas Ok simular pelo cliente.
- Primeiros contratos carregados e códigos enviados em 04/11/2026 (nomes e situação de cada cliente: só no repositório privado).
- Códigos novos com 10 caracteres (os de 8 já enviados continuam valendo).

---

## 🔄 Em andamento

- [ ] Pendências por cliente (envio de código, aditivos a conferir, retorno dos primeiros clientes): ver `ROADMAP.md` no repositório privado `amortiza-contratos`.
- [ ] Reenviar o vídeo tutorial, direto na conversa, para quem ficou com 1 setinha na lista de transmissão.

## ⏭️ Próximos passos

- [ ] **Carregar todos os contratos** (Jardim Amaral e Jardim dos Jatobás): confissão + aditivos de cada cliente.
- [ ] **Enviar o código de cada cliente** pelo WhatsApp, em lotes, com o texto aprovado.
- [ ] Código para o segundo devedor quando houver.
- [ ] Pendências da lista de envio (grupo "Atenção", números a confirmar): ver o repositório privado.
- [ ] Endereço próprio **amortiza.minasok.com.br** (pedir o registro CNAME a quem cuida do domínio).
- [ ] Aviso de privacidade (LGPD) no app e validação com o jurídico da Minas Ok.
- [ ] Avaliar o plano **Vercel Pro** (o plano gratuito é para uso não comercial).
- [ ] Decidir: o "Compartilhar minha casa" mostra a situação de hoje ou a simulada?
- [ ] **Apresentação final do curso Fique Foda em IA** (Felipe — prêmio de R$ 10.000).

## 🤖 Regras para o Claude (executar o roadmap)

**Privacidade:** este repositório e o site são públicos. Nunca escrever aqui nome, CPF, telefone ou valores de
cliente; isso vai só no repositório privado `amortiza-contratos` (inclusive o roadmap com pendências por cliente).

Quando o Matheus disser **"segue o roadmap"**, executar os itens que não dependem dele, marcar ✅ aqui e publicar.
Sempre responder **somente em português**.

### Onde está cada coisa
| O quê | Onde |
|---|---|
| App de trabalho (versão para aprovar) | Artefato no Claude: https://claude.ai/artifact/WvT4HYVfGXoyhsYrhuo5te — ler com a ferramenta Artifact (`read`), editar e publicar no mesmo link |
| App publicado | `amortiza/app/index.html` neste repositório (Vercel publica a cada push na `main`) |
| Copiar o app de trabalho para cá | `python3 amortiza/fonte/sincronizar-app.py` (ajustar os caminhos de origem e destino no topo do script) |
| Contratos, códigos e lista de acesso | Repositório **privado** `mafcafonso-dot/amortiza-contratos` (`dados/clientes.json`, `acesso-clientes.md`) |
| Incluir/alterar contrato | Editar `dados/clientes.json` → `python3 gerar.py <app de trabalho .html>` → publicar o artefato → sincronizar → push |
| Controle dos envios de WhatsApp | `amortiza-contratos/envio/` (`progresso.json`, planilhas com "Enviado?") |
| Regras de cálculo | `amortiza/docs/regras.md` |

### Fluxo de mudança no app
1. Editar o app de trabalho (artefato) e testar (Playwright: entrar com CPF + código, conferir conferência, atraso e simulação).
2. Mostrar ao Matheus. **Só publicar no Vercel depois da aprovação** (ou quando ele pedir a mudança explicitamente).
3. Sincronizar, `git fetch` + `rebase` (outras sessões também publicam aqui) e push.

### Envio de mensagens pelo WhatsApp Web (Chrome do Matheus, extensão Claude)
- Precisa do computador ligado com o Chrome e a extensão conectados; se não estiver, avisar e parar.
- Abrir uma aba própria: `https://web.whatsapp.com/send?phone=55DDDNUMERO`; esperar a conversa carregar.
- **Conferir o cabeçalho** (nome ou final do número) antes de enviar; se o número estiver salvo com outro nome, parar e perguntar.
- Colar o texto (evento de colar no campo da mensagem) e clicar em Enviar. Vídeo: colar o arquivo, enviar e esperar aparecer "0:26"/"1:12" antes do texto.
- Ritmo: ~1 mensagem por minuto, lotes de até 25. Fechar a aba no fim.
- Registrar o envio (`codigo_enviado` em `clientes.json` ou `envio/progresso.json` + planilha).
- O Matheus não deve usar o WhatsApp Web enquanto o envio estiver rodando.

**Pode enviar sem perguntar de novo:** os modelos abaixo, sem mudar o texto, para clientes cujo contrato já está carregado e
cujo número está confirmado. **Sempre perguntar antes:** texto novo ou alterado, número com 9 acrescentado sem confirmação,
número salvo com outro nome, cliente do grupo "Atenção", qualquer pedido de pagamento ou cobrança.

**Modelo aprovado — código de acesso** (trocar {nome} e {código}):
```
Oi, {nome}! Tudo bem? Aqui é o Matheus, da Construtora Minas Ok.

Agora o amortiza já mostra o seu contrato prontinho, sem precisar procurar nada no papel. É só abrir o link e entrar com o seu CPF e este código:

Seu código: {código}

https://projetos-minasok.vercel.app

Lá você confere as suas parcelas, coloca a data do último pagamento e vê quanto economiza adiantando.

Esse código é só seu, não passe para ninguém. Qualquer dúvida, me chama aqui!
```

**Modelo aprovado — vídeo tutorial** (enviar o vídeo `amortiza/divulgacao/amortiza-como-usar.mp4` antes; pode trocar "Oi!" por "Oi, {nome}!"):
```
Oi! Tudo bem? Aqui é o Matheus, da Construtora Minas Ok.

Esses dias te mandei o link do amortiza, o app pra você simular quanto economiza adiantando as parcelas da entrada. Conseguiu dar uma olhada?

Gravei esse vídeo rapidinho mostrando como preencher, passo a passo. É só assistir e depois abrir o app:
https://projetos-minasok.vercel.app

Qualquer dúvida, me chama aqui que eu te ajudo!
```

### Ao ler um contrato novo
- Extrair: CPF, nome, empreendimento, lote/quadra, total confessado, parcela única (valor e vencimento), nº de parcelas,
  1ª parcela, faixas de valor, aditivo (1ª e última pausada), devedores e telefone.
- Conferir a matemática (valor presente a 1% a.m. das parcelas + balão = total confessado) e avisar diferenças.
- A situação do balão **não** vem do Matheus: o app decide pela data do último pagamento informada pelo cliente.

## 💡 Futuro

- Ligar ao **Neofin** (API) para trazer a data do último pagamento sozinha, sem o cliente digitar.
- Envio automático do código por e-mail ou WhatsApp (API oficial da Meta) quando o cliente digitar o CPF.
- Painel da Minas Ok: clientes, códigos, antecipações confirmadas e atualização de contratos.
- Métricas: quantos clientes simularam, quantos pediram antecipação, valor antecipado e atrasos evitados.
- Migrar os contratos para um banco de dados (ex.: Supabase) se a base crescer ou precisar de edição pela tela.

## 📏 Como medir o sucesso

- Clientes que entraram com CPF + código.
- Pedidos de antecipação recebidos pelo botão "QUERO AMORTIZAR!".
- Valor antecipado por mês e parcelas canceladas no banco.
- Queda no número de clientes em atraso.
