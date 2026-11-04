# Roadmap — amortiza | Minas Ok

> **Antecipe e conquiste.** Simulador para o cliente da Construtora Minas Ok adiantar as parcelas da entrada
> com desconto de 1% ao mês e terminar de pagar antes. Para a Minas Ok: receber antes e reduzir atrasos.

- App: https://projetos-minasok.vercel.app
- Apresentação: https://projetos-minasok.vercel.app/apresentacao (demonstração: https://projetos-minasok.vercel.app/?demo)
- Regras de cálculo e decisões: [docs/regras.md](docs/regras.md)
- Contratos dos clientes: repositório **privado** `mafcafonso-dot/amortiza-contratos`

Atualizado em 04/11/2026.

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
  último pagamento; pode ser adiantada com 1% a.m. (conferido no contrato do Thiago: R$ 81.933 = parcelas + balão a valor presente).
- Botão "QUERO AMORTIZAR!" manda a simulação pronta para o WhatsApp da Minas Ok.

### 2. Marca e identidade
- Logo, ícone, casa-símbolo que se enche de amarelo conforme o cliente paga.
- Mascote (casinha com perninhas e olhos) animado; conquista ao quitar ("SUA.").
- Textos simples para quem tem pouca leitura ("Você quita o seu imóvel X meses antes").

### 3. Publicação
- Código no GitHub (`projetos-minasok`) com publicação automática no Vercel.
- Página de apresentação com o app aberto em modo demonstração (contrato fictício).

### 4. Divulgação
- Vídeo de lançamento (26 s, voz Sofia/ElevenLabs, trilha calma) e post.
- Envio individual pelo WhatsApp: 78 clientes "em dia" da lista principal + 8 do Jardim dos Jatobás.
- Vídeo tutorial "como usar" (1min12s) enviado por lista de transmissão.

### 5. Contrato do cliente já carregado (CPF + código)
- Cliente entra com CPF + código de 8 caracteres e vê o próprio contrato; preenche só a data do último pagamento.
- Contratos ficam no repositório privado; no app público vai só o pacote **criptografado** (AES-GCM + PBKDF2).
- Quem não tem código continua preenchendo à mão (o app de antes continua igual).
- Lista de acesso (CPF + código por cliente) para a Minas Ok simular pelo cliente.
- Contratos carregados: Thiago Nathan Martins, Murilo Magalhães, Keveny Resende Fiuza (+ contrato de demonstração).
- Códigos enviados: Murilo e Thiago (04/11/2026).

---

## 🔄 Em andamento

- [ ] Enviar o código do Keveny (WhatsApp 38 99855-3958).
- [ ] Conferir o PDF do aditivo do Keveny (datas informadas: 20/02/2026 a 20/06/2026).
- [ ] Acompanhar o retorno do Murilo e do Thiago (conseguiram entrar? dúvidas?) e ajustar o app.
- [ ] Reenviar o vídeo tutorial, direto na conversa, para quem ficou com 1 setinha na lista de transmissão.

## ⏭️ Próximos passos

- [ ] **Carregar todos os contratos** (Jardim Amaral e Jardim dos Jatobás): confissão + aditivos de cada cliente.
- [ ] **Enviar o código de cada cliente** pelo WhatsApp, em lotes, com o texto aprovado.
- [ ] Código para o segundo devedor quando houver (ex.: Maria Liliane, contrato do Murilo).
- [ ] Decidir sobre os clientes do grupo **"Atenção"** (8 na lista principal e Francielle no Jatobás).
- [ ] Confirmar os números em que foi incluído o 9: Dalila, Josiele, Denner, Gustavo, Marianne e Thiago (Jatobás).
- [ ] Conferir Osmar (número salvo como "Carlos Jatobas") e Lais (número digitado errado).
- [ ] Endereço próprio **amortiza.minasok.com.br** (pedir o registro CNAME a quem cuida do domínio).
- [ ] Aviso de privacidade (LGPD) no app e validação com o jurídico da Minas Ok.
- [ ] Avaliar o plano **Vercel Pro** (o plano gratuito é para uso não comercial).
- [ ] Decidir: o "Compartilhar minha casa" mostra a situação de hoje ou a simulada?
- [ ] **Apresentação final do curso Fique Foda em IA** (Felipe — prêmio de R$ 10.000).

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
