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
- Situação de cada cliente (contratos carregados, códigos enviados, pendências): `docs/ponto-de-partida.md` e
  `ROADMAP.md` no repositório privado `amortiza-contratos`.

## Próximo passo combinado
O Matheus vai mandar os contratos dos demais clientes (confissão + aditivos). Para cada lote: ler, conferir a matemática,
incluir em `dados/clientes.json`, `python3 gerar.py <app de trabalho>`, testar o login, mostrar ao Matheus, publicar e
enviar os códigos pelo WhatsApp com o modelo aprovado.
