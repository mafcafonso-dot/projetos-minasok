# amortiza — ponto de partida para uma nova sessão

Escrito em 04/11/2026, ao encerrar uma sessão longa. **Responder sempre em português.**

## Para começar
1. Ler o roadmap: `claude/amortiza-roadmap.md` (cópia de `amortiza/ROADMAP.md` no GitHub). A seção
   **"Regras para o Claude"** diz onde está cada coisa, os textos de WhatsApp aprovados e o que precisa de aprovação.
2. Conectar os repositórios (ferramenta de adicionar repositório):
   - `mafcafonso-dot/projetos-minasok` (público: app, apresentação, marca, vídeos, docs, roadmap);
   - `mafcafonso-dot/amortiza-contratos` (**privado**: contratos, códigos, lista de acesso, controle dos envios).
3. App de trabalho: artefato https://claude.ai/artifact/WvT4HYVfGXoyhsYrhuo5te — ler com Artifact `read`
   e salvar como `/home/claude/artefato/amortiza-minas-ok.html` (é o caminho que `sincronizar-app.py` e `gerar.py` usam).

## Estado em 04/11/2026
- App no ar com login por CPF + código (contrato criptografado), faixas, aditivo por datas, parcela única (balão),
  "já adiantei", modo demonstração (`?demo`, CPF 111.111.111-11, código DEMO-2026) e página `/apresentacao`.
- Contratos carregados: Thiago Nathan Martins (com aditivo e balão pago), Murilo Magalhães, Keveny Resende Fiuza (aditivo
  20/02–20/06/2026 informado pelo Matheus; PDF do aditivo não recebido).
- Códigos enviados: Murilo e Thiago (04/11). **Pendente: Keveny, WhatsApp 38 99855-3958 (com o 9, confirmado pelo Matheus)** —
  a extensão do Chrome estava desconectada; texto já aprovado (modelo "código de acesso").
- Thiago comentou que poderia adiantar ~R$ 1.000 em 21/12/2026; recebeu simulação: 1 parcela (R$ 529,48, economia R$ 545,46)
  ou 2 parcelas com R$ 1.064,25 (economia R$ 1.085,63).

## Próximo passo combinado
O Matheus vai mandar os contratos dos demais clientes (confissão + aditivos). Para cada lote: ler, conferir a matemática,
incluir em `dados/clientes.json`, `python3 gerar.py <app de trabalho>`, testar o login, mostrar ao Matheus, publicar e
enviar os códigos pelo WhatsApp com o modelo aprovado.
