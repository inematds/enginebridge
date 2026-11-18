# Handoff — 2026-11-18 — Toda a produção de vídeo passa pela fila do x3

## Projeto e escopo
Sessão aberta em ~/projetos/enginebridge; o trabalho foi em ~/projetos/yt-pub-x3 e nos produtores de vídeo: ~/projetos/radar-viral, ~/projetos/imersao2026, ~/projetos/inemaccbot, ~/projetos/eventosextremospub, ~/projetos/gitbombando, ~/projetos/aventurasinemavideo, ~/projetos/wifi (fila-espanhol e vigia-izabela) e ~/projetos/explicavideos. O Nei pediu que qualquer sistema que gera vídeo só salve no x3, e que o x3 duplique cada vídeo nas filas de imports e redes. O vídeo do Zelador no lives7 continua pendente.

## Objetivo atual
Conferir a primeira publicação real de cada fluxo migrado. Pronto = cada fluxo com item real em `~/projetos/yt-pub-x3/data/x3.db`, YouTube `feito` com link, e redes `feito` onde o canal tem redes ligadas.

## Estado aceito
- [confirmed] Todo vídeo novo vira entregas youtube e rs — evidência: arquivo: ~/projetos/yt-pub-x3/lib/entrada.py; teste: `python3 -m pytest -q tests` em yt-pub-x3 → 70 passed
- [confirmed] `enviar-arquivo` ganhou `--quando`, `--esperar`, `--contexto-arquivo`, `--tags`, `--sem-capa`; comando novo `esperar` — evidência: arquivo: ~/projetos/yt-pub-x3/yt-pub-x3
- [confirmed] Radar não agenda mais o Metricool, salvo item antigo só com YouTube — evidência: arquivo: ~/projetos/radar-viral/radar.py
- [confirmed] Imersão entra na fila no dia do vídeo; hora marcada só no lives23 ou depois das 16:00 — evidência: arquivo: ~/projetos/imersao2026/diaria/agendador.py
- [confirmed] Bot 0.28.12 no ar, pede sempre as duas filas — evidência: teste: `npx vitest run` → 1181 passed; log do serviço "no ar v0.28.12"
- [confirmed] Clima, gitbombando, explicavideo/vigias, Aventuras e espanhol alterados; testados em fila temporária, sem publicar — evidência: arquivo: ~/projetos/eventosextremospub/auto/rodar.sh; ~/projetos/gitbombando/gb.py; ~/projetos/explicavideos/bot/entrega.sh; ~/projetos/aventurasinemavideo/publicar_episodio.py; ~/projetos/wifi/fila-espanhol/fila_es.py
- [confirmed] Redes ligadas no lives10 e no lives24; lives25 ativado com idioma es e rótulo de IA; lives26 com clipes às 8, 10, 12, 14, 16 e 18 h — evidência: arquivo: ~/projetos/yt-pub-x3/canais/lives24.yaml, lives10.yaml, lives25.yaml, lives26.yaml
- [confirmed] Episódio real do Aventuras entrou como item 3601, YouTube aguardando; lives26 pausado até 20:30 por limite de envios — evidência: arquivo: ~/projetos/yt-pub-x3/data/x3.db

## Proposto / tentado, não confirmado
- [unverified] Publicação real pelo novo caminho de clima, gitbombando, vigias, espanhol e Aventuras — nenhuma rodada real concluída até o último registro.
- [unverified] Episódio 3601 sair em 19/11 às 08:00 — previsão pelos horários; o processo fica esperando até 6 h e tenta de novo.
- [?] Login do lives25 ter permissão de legenda — o que tem histórico de sucesso é o token `~/.config/yt-pubx/tokens/espanhol.json`.

## Decisões
- Regra única na entrada do x3: vídeo vai a imports e redes; `destinos` e `--so-youtube` são ignorados — pedido do Nei em 18/11, gravado em ~/projetos/yt-pub-x3/docs/PRODUCAO.md.
- Clima, gitbombando e explicavideo usam `--quando agora --esperar`, porque precisam do link logo depois.
- Itens já na fila e migrados não foram duplicados.
- Saúde e futebol passam a ir às redes, substituindo a regra de 12/11.

## Não fazer (restrições e travas)
- Não fazer commit nem push sem pedido — fonte: ~/.claude/CLAUDE.md.
- Não pôr dados sensíveis no git; nenhuma API não autorizada — fonte: ~/.claude/CLAUDE.md e dito pelo usuário, só nesta conversa.
- Não trocar o público do crítico por conta própria; `CRITICO_SEGUE=1` só com ordem do Nei; não registrar nota em nome dele — fonte: ~/.claude/projects/-home-nmaldaner-projetos-enginebridge/memory/zelador-publicacao.md e só nesta conversa.
- Não apagar nada no Telegram sem aprovação individual — fonte: ~/.claude/CLAUDE.md.
- Não editar `.sh` em uso no próprio arquivo: gravar em arquivo novo e renomear — só nesta conversa.

## Arquivos alterados
- Sem commit, junto com trabalho preexistente: `~/projetos/yt-pub-x3` (lib, CLI, canais, testes, docs, READMEs), `~/projetos/radar-viral` (radar.py, radar.json, README.md), `~/projetos/inemaccbot` (destinos.ts, reel.ts, reel.test.ts, package.json, CHANGELOG.md), `~/projetos/imersao2026/diaria/agendador.py`, `~/projetos/eventosextremospub/auto/rodar.sh`, `~/projetos/gitbombando` (gb.py, auto/rodar.sh, CHANGELOG.md), `~/projetos/aventurasinemavideo` (publicar_episodio.py, fila_publicar.sh, cortes.py), `~/projetos/wifi` (fila-espanhol/fila_es.py, vigia-izabela/divulga.sh), `~/projetos/explicavideos` (bot/entrega.sh, VERSION 2.32.12).
- Também sem commit, da etapa anterior: `~/projetos/promoavatar` e `~/projetos/promoavatar3` (mapa e documento de públicos).

## Memória e regras duráveis tocadas
- `~/.claude/projects/-home-nmaldaner-projetos-enginebridge/memory/producao-so-fila-x3.md` — regra de que a produção só entrega no x3.
- `~/.claude/projects/-home-nmaldaner-projetos-enginebridge/memory/MEMORY.md` — ponteiro para essa regra.

## Verificação
- Rodado: `python3 -m pytest -q tests` em yt-pub-x3 → 70 passed.
- Rodado: `npx vitest run` em inemaccbot → 1181 passed; `npm run build` → ok.
- Rodado: teste em fila temporária de clima, Aventuras e espanhol → entregas, espera, repetição e playlist corretas, com publicação simulada.
- Rodado: `bash -n` nos scripts alterados e `py_compile` nos Python → ok.
- Rodado: consulta a `runner.disponivel` do lives24 → (True, '').
- Não rodado: publicação real pelos novos caminhos — depende das próximas rodadas.

## Estado em execução
- Processos em segundo plano: serviços do usuário `yt-pub-x3`, `yt-pub-x3-painel`, `inemaccbot`, `imersao-diaria-agendador`, `aventuras-fila`; parar com `systemctl --user stop <serviço>`. O `aventuras-fila` pode estar esperando o item 3601.
- Servidores / portas: painel do x3 pelo serviço `yt-pub-x3-painel`
- Worktrees / branches abertos: nenhum

## Perguntas abertas e adiados
- Aberta: programar envio de legenda no x3 só para o espanhol? Hoje vídeo com legenda segue pelo yt-pubx.
- Aberta: fazer commit e push dos projetos alterados?
- Adiado: redes do lives11 usam outra conta do Metricool e a fila `metricool-lives11` lê o histórico do yt-pubx, que o x3 não alimenta.
- Adiado: guias públicos do promoavatar ainda citam 12 públicos e 36 alvos.

## Pela metade
- Conferência real dos fluxos migrados — parou em: item 3601 aguardando — falta: acompanhar as próximas rodadas.
- Vídeo do Zelador no lives7 — parou em: crítico já usa o público do canal — falta: rodar o crítico de novo, ficha, avatar, entrega, embed nos guias, READMEs, portal e tópico.

## Próxima ação exata
Consultar em `~/projetos/yt-pub-x3/data/x3.db` os itens novos de clima, gitbombando, explicavideo, aventuras e espanhol e corrigir o que falhar. Isso é só leitura e não precisa de aprovação. Legenda e commit dependem da resposta do Nei.

## Mapa de retomada
- `~/projetos/yt-pub-x3/docs/PRODUCAO.md` — situação e regra de entrada
- `~/projetos/yt-pub-x3/lib/entrada.py` — duplicação nas duas filas
- `~/projetos/yt-pub-x3/yt-pub-x3` — comandos usados pelos produtores
- `~/.claude/projects/-home-nmaldaner-projetos-enginebridge/memory/producao-so-fila-x3.md` — ordem do Nei
- `~/.claude/projects/-home-nmaldaner-projetos-enginebridge/memory/zelador-publicacao.md` — pendência do vídeo

## Perguntas-teste
1. Qual é a tarefa atual e o critério de pronto? → Conferir a primeira publicação real de cada fluxo no x3 — fonte: ~/projetos/yt-pub-x3/docs/PRODUCAO.md — chave: `x3`
2. Qual foi a última decisão e por quê? → Ligar as redes do lives24 para a contabilidade continuar nas redes — fonte: ~/projetos/yt-pub-x3/canais/lives24.yaml — chave: `lives24`
3. O que não pode mudar? → Sem commit ou push sem pedido — fonte: ~/.claude/CLAUDE.md — chave: `commit`
4. O que está pela metade? → Conferência real e vídeo do Zelador — fonte: ~/.claude/projects/-home-nmaldaner-projetos-enginebridge/memory/zelador-publicacao.md — chave: `Zelador`
5. Qual é a próxima ação, por quê, e precisa de aprovação? → Consultar os itens novos no banco para validar a migração; não precisa — fonte: só nesta conversa — chave: `x3.db`

## Checagem de compartilhamento
- Sem segredos, tokens, cookies, dados pessoais ou endpoints privados: sim


<!-- handoff-estado:inicio -->
## Estado gravado pelo script (não editar)

Gravado por handoff-grava.py no momento do handoff. `--conferir` compara com o projeto agora.

- commit: 5244ce10625b8b07290887494816b0cacc35e944 · branch: main
- arquivos sujos fora de handoffs/: 0

### Repo do trabalho: /home/nmaldaner/projetos/yt-pub-x3
- commit: 4a7db14b2e9e52e35dd8ba24fd1c5b2e28177656 · branch: main
- arquivos sujos: 24
- impressão de todos os sujos: c53cf518b595c4bf
- `CLAUDE.md` · sha256:9bc550a3eb20 · sujo
- `FALHAS.md` · sha256:67f2a77b9769 · sujo
- `README.en.md` · sha256:4ce4ab5df80b · sujo
- `README.es.md` · sha256:a0963404c106 · sujo
- `README.md` · sha256:18d419cac019 · sujo
- `dashboard/index.html` · sha256:05b28f460f38 · sujo
- `dashboard/server.py` · sha256:b9a8405c1c8e · sujo
- `docs/ESPECIFICACAO.md` · sha256:d46d25bacc94 · sujo
- `docs/PRODUCAO.md` · sha256:c34755dc7b60 · sujo
- `hub.py` · sha256:537193d1e821 · sujo
- `lib/__init__.py` · sha256:38dd691e2514 · sujo
- `lib/canais.py` · sha256:fadb1c5c4389 · sujo
- `lib/db.py` · sha256:241981dbb0e4 · sujo
- `lib/entrada.py` · sha256:972c3df96037 · sujo
- `lib/importar.py` · sha256:c487006787e1 · sujo
- `lib/metricool.py` · sha256:e2464b5dbb97 · sujo
- `lib/migrar.py` · sha256:6a72eb13eff8 · sujo
- `lib/painel.py` · sha256:4a16b245788a · sujo
- `lib/runner.py` · sha256:2c02b56c9359 · sujo
- `lib/youtube.py` · sha256:8053a3cf330d · sujo
- `scripts/ia_ytpubx.py` · sha256:cf25f6123dbe · sujo
- `systemd/yt-pub-x3-painel-rede.service` · sha256:8201e3aebc41 · sujo
- `tests/test_x3.py` · sha256:a8fd7af918d3 · sujo
- `yt-pub-x3` · sha256:01153cc47647 · sujo

### Repo do trabalho: /home/nmaldaner/projetos/radar-viral
- commit: 0bc3160eb94bcb7c5db36e46013034618b174901 · branch: main
- arquivos sujos: 5
- impressão de todos os sujos: e21ba3a4598125db
- `.gitignore` · sha256:05a798ddf61f · sujo
- `CLAUDE.md` · sha256:5e4d43c6fe61 · sujo
- `README.md` · sha256:a556ee235ca0 · sujo
- `radar.json` · sha256:d83e6efbec1b · sujo
- `radar.py` · sha256:a76a251e2ab0 · sujo

### Repo do trabalho: /home/nmaldaner/projetos/inemaccbot
- commit: 63c773e64c32b711199b03191fcffb7ab1476d93 · branch: master
- arquivos sujos: 9
- impressão de todos os sujos: 6862bcfa03128bfc
- `CHANGELOG.md` · sha256:dd8eda4b8578 · sujo
- `FALHAS.md` · sha256:80b320c7082a · sujo
- `package.json` · sha256:009e88eaf687 · sujo
- `src/dominio/destinos.ts` · sha256:405e81d918a3 · sujo
- `src/fila/tarefas/reel.test.ts` · sha256:d407e322e487 · sujo
- `src/fila/tarefas/reel.ts` · sha256:16287af76732 · sujo
- `src/fluxos/entrada-fase.ts` · sha256:9447d8dbe9ee · sujo
- `src/integracao/promoavatar.test.ts` · sha256:ac1b804f14f2 · sujo
- `src/integracao/promoavatar3.test.ts` · sha256:f2bc5e742881 · sujo

### Repo do trabalho: /home/nmaldaner/projetos/imersao2026
- commit: 0f5228f203e672745f3fd2353ae1f9b35becbcab · branch: main
- arquivos sujos: 174
- impressão de todos os sujos: 68088dd4ddd99235
- `diaria/agendador.log` · sha256:a52262d5d297 · sujo
- `diaria/agendador.py` · sha256:7f955c940205 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives1.txt` · sha256:a04a9cb9744d · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives1.txt.plano` · sha256:5f59e89ab98b · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives10.txt` · sha256:1c124af405dc · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives10.txt.plano` · sha256:99b8947d3ad9 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives11.txt` · sha256:32cc7da59cdf · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives11.txt.plano` · sha256:9b1d87681b61 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives12.txt` · sha256:da339ce63e6f · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives12.txt.plano` · sha256:fb8c7ef203eb · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives2.txt` · sha256:6376814a6275 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives2.txt.plano` · sha256:b07bb778339a · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives22.txt` · sha256:855de7e1d174 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives22.txt.plano` · sha256:87b9268cf6c4 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives23.txt` · sha256:15842af5b11c · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives23.txt.plano` · sha256:17fbd6769955 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives24.txt` · sha256:e4dcbd80bb25 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives24.txt.plano` · sha256:62e3d30d77f4 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives3.txt` · sha256:b776493cfad5 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives3.txt.plano` · sha256:754b9db0a973 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives31.txt` · sha256:b6b370be8cba · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives31.txt.plano` · sha256:a00e03b083a2 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives4.txt` · sha256:fb8bc683b6b4 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives4.txt.plano` · sha256:002e48b7d658 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives6.txt` · sha256:fd1e7502707a · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives6.txt.plano` · sha256:f72ee3352ef4 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives7.txt` · sha256:6fa9d69293f1 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives7.txt.plano` · sha256:e5c8e6ba8875 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives8.txt` · sha256:2b0a665b9a21 · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives8.txt.plano` · sha256:e069685b04fe · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives9.txt` · sha256:0b095ebace0c · sujo
- `diaria/ctx/2026-11-18-imersao-d1118-lives9.txt.plano` · sha256:7300cb2b59ad · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives1.txt` · sha256:aa2f90dd6ce1 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives1.txt.plano` · sha256:d898d1d869ec · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives10.txt` · sha256:582660f47802 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives10.txt.plano` · sha256:7d79ea6ab518 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives10b.txt` · sha256:d4e1db4727e7 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives10b.txt.plano` · sha256:c8e6822de3ab · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives11.txt` · sha256:ce6aa49a8b08 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives11.txt.plano` · sha256:b3965b06d4bc · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives12.txt` · sha256:44f77239b59c · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives12.txt.plano` · sha256:365cb43c7d3b · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives12b.txt` · sha256:2e6bece2004b · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives12b.txt.plano` · sha256:770223b79fd5 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives1b.txt` · sha256:1b66805761fd · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives1b.txt.plano` · sha256:d1dabaf41333 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives2.txt` · sha256:931acd7630a3 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives2.txt.plano` · sha256:8158249ef9d8 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives22.txt` · sha256:97d6c6d7e33a · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives22.txt.plano` · sha256:cd817e754047 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives22b.txt` · sha256:00d178ca8de1 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives22b.txt.plano` · sha256:170663b5de67 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives23.txt` · sha256:e4719111d258 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives23.txt.plano` · sha256:1e24565142e9 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives23b.txt` · sha256:0ac2ae815ca5 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives23b.txt.plano` · sha256:fd244fb032b7 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives24.txt` · sha256:e00d549a0a38 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives24.txt.plano` · sha256:c7af10803586 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives24b.txt` · sha256:8f61471688a8 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives24b.txt.plano` · sha256:be90ba715a98 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives2b.txt` · sha256:2de6f59a53eb · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives2b.txt.plano` · sha256:0ba71b5f87c3 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives3.txt` · sha256:91d198054a92 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives3.txt.plano` · sha256:e9c1cf02f0be · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives31.txt` · sha256:249190caf3eb · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives31.txt.plano` · sha256:dfb5d92e8131 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives31b.txt` · sha256:b0ddee789337 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives31b.txt.plano` · sha256:433083ca796b · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives3b.txt` · sha256:45c94e104f9a · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives3b.txt.plano` · sha256:02559ce548d4 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives4.txt` · sha256:7f9b0f62cadb · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives4.txt.plano` · sha256:7cdf56b7b222 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives4b.txt` · sha256:83629874a945 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives4b.txt.plano` · sha256:2588db44b6fc · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives6.txt` · sha256:3f7e4f51dfb7 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives6.txt.plano` · sha256:82ddc7990dea · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives6b.txt` · sha256:d828deca907d · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives6b.txt.plano` · sha256:2cbfdbacc6b2 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives7.txt` · sha256:6396af78cd32 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives7.txt.plano` · sha256:f63d5a7aa4b3 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives7b.txt` · sha256:10b8a845c6d4 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives7b.txt.plano` · sha256:31d9d49ff751 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives8.txt` · sha256:ad0f006f4609 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives8.txt.plano` · sha256:3424dfda247f · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives8b.txt` · sha256:ac64e7e69885 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives8b.txt.plano` · sha256:4bdc3cdd9d16 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives9.txt` · sha256:ec1476706c78 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives9.txt.plano` · sha256:6bb0926dd9d4 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives9b.txt` · sha256:b9c485b48aa6 · sujo
- `diaria/ctx/2026-11-18-imersao-d1119-lives9b.txt.plano` · sha256:c3c0df96508e · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives10b.txt` · sha256:e2ba507a6811 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives10b.txt.plano` · sha256:6bd0382db193 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives11b.txt` · sha256:63fcf6b4b9da · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives11b.txt.plano` · sha256:1ee2355dbab0 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives12b.txt` · sha256:bcfc75f2fdb5 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives12b.txt.plano` · sha256:2b93ead768fc · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives1b.txt` · sha256:5d6e616eac9d · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives1b.txt.plano` · sha256:dd529849b4a5 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives22b.txt` · sha256:9eafdc8fc1c3 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives22b.txt.plano` · sha256:2d0bd840bcf7 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives24b.txt` · sha256:3cabc2dbb723 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives24b.txt.plano` · sha256:2ec37cd65efc · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives2b.txt` · sha256:0d94b4c59b5a · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives2b.txt.plano` · sha256:6040d0700955 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives31b.txt` · sha256:7a6544eaddee · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives31b.txt.plano` · sha256:d966831d6f0e · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives3b.txt` · sha256:4192bbc68076 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives3b.txt.plano` · sha256:322c8b2e7d0a · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives4b.txt` · sha256:6b1617f2d4c0 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives4b.txt.plano` · sha256:97de80bebf16 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives6b.txt` · sha256:e619c43351cf · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives6b.txt.plano` · sha256:21686310f37d · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives7b.txt` · sha256:0ccfd6d7ef0d · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives7b.txt.plano` · sha256:bff265c162d8 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives8b.txt` · sha256:ad2260c84c5f · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives8b.txt.plano` · sha256:870f8445e895 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives9b.txt` · sha256:3eb445077304 · sujo
- `diaria/ctx/2026-11-18-imersao-d1120-lives9b.txt.plano` · sha256:c48957d670c0 · sujo
- `diaria/jobs.txt` · sha256:ddd17a1c6844 · sujo
- `diaria/montagem.log` · sha256:d047218e7b6b · sujo
- `diaria/pegos.txt` · sha256:55e5f84284ef · sujo
- `diaria/pegos.txt.bak-20261118` · sha256:32f0eaf48e23 · sujo
- `diaria/publicados.tsv` · sha256:7e8af766e10d · sujo
- `diaria/publicar.lock` · sha256:e3b0c44298fc · sujo
- `diaria/saidas/imersao-d1118-lives10.txt` · sha256:0cd60d17b328 · sujo
- `diaria/saidas/imersao-d1118-lives23.txt` · sha256:c047c7cf7e0a · sujo
- `diaria/saidas/imersao-d1118-lives31.txt` · sha256:21e8760f2597 · sujo
- `diaria/saidas/imersao-d1118-lives4.txt` · sha256:d2d51c74866d · sujo
- `diaria/saidas/imersao-d1119-lives1.txt` · sha256:3b8f6ffdacfb · sujo
- `diaria/saidas/imersao-d1119-lives10.txt` · sha256:04dd4f9baad4 · sujo
- `diaria/saidas/imersao-d1119-lives10b.txt` · sha256:e6d7862b738c · sujo
- `diaria/saidas/imersao-d1119-lives11.txt` · sha256:00a328bf7529 · sujo
- `diaria/saidas/imersao-d1119-lives11b.txt` · sha256:8b7b607eb8ed · sujo
- `diaria/saidas/imersao-d1119-lives12.txt` · sha256:590128546b4d · sujo
- `diaria/saidas/imersao-d1119-lives12b.txt` · sha256:1c5c92d0ef3f · sujo
- `diaria/saidas/imersao-d1119-lives1b.txt` · sha256:7f3a6a1a2e26 · sujo
- `diaria/saidas/imersao-d1119-lives2.txt` · sha256:7a8ccce789e5 · sujo
- `diaria/saidas/imersao-d1119-lives22.txt` · sha256:d2632f193a92 · sujo
- `diaria/saidas/imersao-d1119-lives22b.txt` · sha256:a8df1c592ac1 · sujo
- `diaria/saidas/imersao-d1119-lives23.txt` · sha256:2aefcb2f847a · sujo
- `diaria/saidas/imersao-d1119-lives23b.txt` · sha256:5ba85bf8d682 · sujo
- `diaria/saidas/imersao-d1119-lives24.txt` · sha256:d3d4337994c4 · sujo
- `diaria/saidas/imersao-d1119-lives24b.txt` · sha256:65fbca633491 · sujo
- `diaria/saidas/imersao-d1119-lives2b.txt` · sha256:fe396409da40 · sujo
- `diaria/saidas/imersao-d1119-lives3.txt` · sha256:60ccace0d30c · sujo
- `diaria/saidas/imersao-d1119-lives31.txt` · sha256:6bf88caba45d · sujo
- `diaria/saidas/imersao-d1119-lives31b.txt` · sha256:c56fc95d9055 · sujo
- `diaria/saidas/imersao-d1119-lives3b.txt` · sha256:3e4d9112fc0b · sujo
- `diaria/saidas/imersao-d1119-lives4.txt` · sha256:6d09aca38126 · sujo
- `diaria/saidas/imersao-d1119-lives4b.txt` · sha256:dc03cc3286c9 · sujo
- `diaria/saidas/imersao-d1119-lives6.txt` · sha256:9a29d0dc3f80 · sujo
- `diaria/saidas/imersao-d1119-lives6b.txt` · sha256:d20f3395462c · sujo
- `diaria/saidas/imersao-d1119-lives7.txt` · sha256:dfbec6f088d0 · sujo
- `diaria/saidas/imersao-d1119-lives7b.txt` · sha256:e2fab5e80caa · sujo
- `diaria/saidas/imersao-d1119-lives8.txt` · sha256:e894e89d77d9 · sujo
- `diaria/saidas/imersao-d1119-lives8b.txt` · sha256:49f5879df778 · sujo
- `diaria/saidas/imersao-d1119-lives9.txt` · sha256:6bea38d6f5b4 · sujo
- `diaria/saidas/imersao-d1119-lives9b.txt` · sha256:41b752727796 · sujo
- `diaria/saidas/imersao-d1120-lives10b.txt` · sha256:a8c521501344 · sujo
- `diaria/saidas/imersao-d1120-lives11b.txt` · sha256:a161760a61b1 · sujo
- `diaria/saidas/imersao-d1120-lives12b.txt` · sha256:c57f2892185c · sujo
- `diaria/saidas/imersao-d1120-lives1b.txt` · sha256:2472d1e24adc · sujo
- `diaria/saidas/imersao-d1120-lives22b.txt` · sha256:20935de3bba0 · sujo
- `diaria/saidas/imersao-d1120-lives23b.txt` · sha256:bb97c9642f13 · sujo
- `diaria/saidas/imersao-d1120-lives24b.txt` · sha256:5b97254621fe · sujo
- `diaria/saidas/imersao-d1120-lives2b.txt` · sha256:903556d3965e · sujo
- `diaria/saidas/imersao-d1120-lives31b.txt` · sha256:103d9f7974bf · sujo
- `diaria/saidas/imersao-d1120-lives3b.txt` · sha256:ac1e3f9ced50 · sujo
- `diaria/saidas/imersao-d1120-lives4b.txt` · sha256:a2cbf2d4aa2f · sujo
- `diaria/saidas/imersao-d1120-lives6b.txt` · sha256:74a9f8602ac6 · sujo
- `diaria/saidas/imersao-d1120-lives7b.txt` · sha256:afa05c43c9b3 · sujo
- `diaria/saidas/imersao-d1120-lives8b.txt` · sha256:cd3b28487fb8 · sujo
- `diaria/saidas/imersao-d1120-lives9b.txt` · sha256:06a83f1bfc11 · sujo
- `diaria/trabalho.log` · sha256:d98329e83275 · sujo

### Repo do trabalho: /home/nmaldaner/projetos/eventosextremospub
- commit: 7a8b1a4ff1c2c656eafcea4ded75b2ce9be001f1 · branch: main
- arquivos sujos: 23710 (lista cortada)
- impressão de todos os sujos: e6f826514e9c8720
- `"edicoes/2026-10-23-mundo-7d/pesquisa/bruto/gn_DANA_Adam_v\303\255ctimas.xml"` · sha256:apagado · sujo
- `"edicoes/2026-10-23-mundo-7d/pesquisa/bruto/gn_temp\303\252te_Austen.xml"` · sha256:apagado · sujo
- `"edicoes/2026-10-24-mundo-7d/pesquisa/bruto/gn_temp\303\252te_Austen.xml"` · sha256:apagado · sujo
- `"edicoes/2026-10-25-mundo-7d/pesquisa/bruto/gn_temp\303\252te_Austen.xml"` · sha256:apagado · sujo
- `"edicoes/2026-11-06-mundo-7d/pesquisa/bruto/gn_Ecuador_r\303\255os_desbordados.xml"` · sha256:apagado · sujo
- `"edicoes/2026-11-07-mundo-7d/pesquisa/bruto/gn_Ecuador_r\303\255os_desbordados.xml"` · sha256:apagado · sujo
- `"edicoes/2026-11-08-mundo-7d/pesquisa/bruto/gn_Ecuador_r\303\255os_desbordados.xml"` · sha256:apagado · sujo
- `"edicoes/2026-11-15-semana/pesquisa/quadros/legenda-mil\303\255metros.jpg"` · sha256:apagado · sujo
- `"edicoes/2026-11-15-semana/pesquisa/quadros/legenda-quil\303\264metros.jpg"` · sha256:apagado · sujo
- `FALHAS.md` · sha256:f6928fe65583 · sujo
- `auto/previsao-usados.txt` · sha256:6e596e546105 · sujo
- `auto/rodar.sh` · sha256:c45b27ab16c5 · sujo
- `edicoes/2026-10-09-alerta-norte-nordeste/video-avatar.mp4.envio-v3.json` · sha256:d3fec43b751f · sujo
- `edicoes/2026-10-09-alerta-norte-nordeste/video.mp4.envio-v3.json` · sha256:356bde79342d · sujo
- `edicoes/2026-10-09-el-nino/avatar/foto.jpg` · sha256:4a387696d84d · sujo
- `edicoes/2026-10-09-el-nino/fonte/painel-el-nino-4.pdf` · sha256:8058947c242b · sujo
- `edicoes/2026-10-09-el-nino/previa-16x9.mp4.envio-v3.json` · sha256:152d7f71b582 · sujo
- `edicoes/2026-10-09-el-nino/previa.mp4.envio-v3.json` · sha256:c99530b92148 · sujo
- `edicoes/2026-10-09-el-nino/sat/web/anomalia.png` · sha256:87c7e4f6737b · sujo
- `edicoes/2026-10-09-el-nino/video-avatar.mp4.envio-v3.json` · sha256:74c69c4a617b · sujo
- `edicoes/2026-10-10-el-nino-explicado/avatar/video_id.txt` · sha256:7bd8bef1f42e · sujo
- `edicoes/2026-10-10-el-nino-explicado/sat/web/anomalia.png` · sha256:3cf05867665b · sujo
- `edicoes/2026-10-10-el-nino-explicado/video-avatar-bot.mp4.envio-v3.json` · sha256:c222bf494599 · sujo
- `edicoes/2026-10-10-ultimas-24h/sat/web/ir_tempos.json` · sha256:0093b9fbcc3b · sujo
- `edicoes/2026-10-10-ultimas-24h/video-avatar.mp4.envio-v3.json` · sha256:93d5275dc291 · sujo
- `edicoes/2026-10-10-ultimas-24h/video.mp4.envio-v3.json` · sha256:3b73ea0d4b44 · sujo
- `edicoes/2026-10-11-semana/om/prev15_capitais.json` · sha256:de2d6ea61b90 · sujo
- `edicoes/2026-10-11-semana/om/prev15_grade.json` · sha256:a12abf1c36ec · sujo
- `edicoes/2026-10-11-semana/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:024651b3971b · sujo
- `edicoes/2026-10-11-semana/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:70740ae45e49 · sujo
- `edicoes/2026-10-11-semana/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:8139abb88947 · sujo
- `edicoes/2026-10-11-semana/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:ed0d7c1f0a1f · sujo
- `edicoes/2026-10-11-semana/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:06611266fcbb · sujo
- `edicoes/2026-10-11-semana/sat/web/ir_tempos.json` · sha256:e5c7c26860b8 · sujo
- `edicoes/2026-10-11-semana/video-avatar.mp4.envio-v3.json` · sha256:2735f7759277 · sujo
- `edicoes/2026-10-11-ultimas-24h/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:b14ba84c80c4 · sujo
- `edicoes/2026-10-11-ultimas-24h/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:7a36901321eb · sujo
- `edicoes/2026-10-11-ultimas-24h/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:b33519abe086 · sujo
- `edicoes/2026-10-11-ultimas-24h/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:d4d660256cf4 · sujo
- `edicoes/2026-10-11-ultimas-24h/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:d5c28f4d9663 · sujo
- `edicoes/2026-10-11-ultimas-24h/sat/web/ir_tempos.json` · sha256:9898057fe396 · sujo
- `edicoes/2026-10-11-ultimas-24h/video-avatar.mp4.envio-v3.json` · sha256:ebbd75b5e6b0 · sujo
- `edicoes/2026-10-12-amazonia-mundo/AVATAR-STATUS.txt` · sha256:58973896896b · sujo
- `edicoes/2026-10-12-amazonia-mundo/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-12-amazonia-mundo/avatar/video_id.txt` · sha256:8d2b0205a515 · sujo
- `edicoes/2026-10-12-amazonia-mundo/video-avatar-bot.mp4.envio-v3.json` · sha256:3c7806a71744 · sujo
- `edicoes/2026-10-12-amazonia-mundo/video-bot.mp4.envio-v3.json` · sha256:005b1a70c6df · sujo
- `edicoes/2026-10-12-amazonia-reel/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-12-amazonia-reel/avatar/video_id.txt` · sha256:fb51897b4973 · sujo
- `edicoes/2026-10-12-amazonia-reel/video-avatar.mp4.envio-v3.json` · sha256:06e8b61ab915 · sujo
- `edicoes/2026-10-12-amazonia-reel/video.mp4.envio-v3.json` · sha256:a9e6d3e9b0fa · sujo
- `edicoes/2026-10-12-mundo-clima/AVATAR-STATUS.txt` · sha256:f73b37dbbcd3 · sujo
- `edicoes/2026-10-12-mundo-clima/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-12-mundo-clima/avatar/fala.txt` · sha256:f8371ab6656c · sujo
- `edicoes/2026-10-12-mundo-clima/avatar/tempos.json` · sha256:45957a78d8ba · sujo
- `edicoes/2026-10-12-mundo-clima/avatar/video_id.txt` · sha256:2e18a64b6eee · sujo
- `edicoes/2026-10-12-mundo-clima/sat/web/anomalia.png` · sha256:93a6cd64b51a · sujo
- `edicoes/2026-10-12-mundo-clima/video-avatar-bot.mp4.envio-v3.json` · sha256:605d104a4328 · sujo
- `edicoes/2026-10-12-ultimas-24h/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:cc4897ad649e · sujo
- `edicoes/2026-10-12-ultimas-24h/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:28bd35263839 · sujo
- `edicoes/2026-10-12-ultimas-24h/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:7b901359f016 · sujo
- `edicoes/2026-10-12-ultimas-24h/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:0748fabcb069 · sujo
- `edicoes/2026-10-12-ultimas-24h/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:a9d4ee964f96 · sujo
- `edicoes/2026-10-12-ultimas-24h/sat/web/ir_tempos.json` · sha256:848644d2d9b0 · sujo
- `edicoes/2026-10-12-ultimas-24h/video-avatar.mp4.envio-v3.json` · sha256:7600d935ee46 · sujo
- `edicoes/2026-10-13-24h-foto/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-13-24h-foto/avatar/fala.txt` · sha256:35f7d5d5085f · sujo
- `edicoes/2026-10-13-24h-foto/avatar/retempo.py` · sha256:41e4acfe252f · sujo
- `edicoes/2026-10-13-24h-foto/avatar/tempos.json` · sha256:e756e0286f71 · sujo
- `edicoes/2026-10-13-24h-foto/avatar/video_id.txt` · sha256:8846c538f621 · sujo
- `edicoes/2026-10-13-24h-foto/falas.json` · sha256:bd7cacaca636 · sujo
- `edicoes/2026-10-13-24h-foto/gerar_cena.py` · sha256:a628ff9fa682 · sujo
- `edicoes/2026-10-13-24h-foto/narrar.py` · sha256:b2dc0ad38dc1 · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:8d45b4a93ef9 · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:73ddac0caa79 · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:802a051b6c1e · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:47173b7139ce · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:36bf59ffe2e2 · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/previsao7d.json` · sha256:a6412fc8a1cb · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/bruto/resumo.json` · sha256:474fd69f9176 · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/dados.md` · sha256:508e8bad69eb · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/noticias.md` · sha256:b71c6c80d7af · sujo
- `edicoes/2026-10-13-24h-foto/pesquisa/proposta.md` · sha256:0bccc7e17577 · sujo
- `edicoes/2026-10-13-24h-foto/previa/avatar/foto.png` · sha256:b73f7ef0c365 · sujo
- `edicoes/2026-10-13-24h-foto/previa/avatar/tempos.json` · sha256:716d08429e04 · sujo
- `edicoes/2026-10-13-24h-foto/previa/cena.js` · sha256:d230ba23e43c · sujo
- `edicoes/2026-10-13-24h-foto/previa/gerar_cena.py` · sha256:a628ff9fa682 · sujo
- `edicoes/2026-10-13-24h-foto/sat/web/ir_tempos.json` · sha256:a3a07cc5dacf · sujo
- `edicoes/2026-10-13-24h-foto/tempos.json` · sha256:716d08429e04 · sujo
- `edicoes/2026-10-13-24h-foto/video-avatar.mp4.envio-v3.json` · sha256:02f8c7e17e1d · sujo
- `edicoes/2026-10-13-24h-foto/video-previa.mp4.envio-v3.json` · sha256:b21b24b100e3 · sujo
- `edicoes/2026-10-13-24h-foto/yt.txt` · sha256:91f6e04c661d · sujo
- `edicoes/2026-10-13-clima-do-dia/REFAZER-VISUAL.md` · sha256:76732fdd5557 · sujo
- `edicoes/2026-10-13-clima-do-dia/VISUAL-OK.txt` · sha256:8ae3d17ddc35 · sujo
- `edicoes/2026-10-13-clima-do-dia/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-13-clima-do-dia/avatar/fala.txt` · sha256:aeb87eaedf74 · sujo
- `edicoes/2026-10-13-clima-do-dia/avatar/retempo.py` · sha256:8012bc9d48db · sujo
- `edicoes/2026-10-13-clima-do-dia/avatar/tempos.json` · sha256:81a3924aa399 · sujo
- `edicoes/2026-10-13-clima-do-dia/avatar/video_id.txt` · sha256:745189a6ee43 · sujo
- `edicoes/2026-10-13-clima-do-dia/capa-dia/LIMITES.md` · sha256:bdbf1caf92e5 · sujo
- `edicoes/2026-10-13-clima-do-dia/capa-dia/abertura.png` · sha256:21c07d0154ae · sujo
- `edicoes/2026-10-13-clima-do-dia/capa-dia/granizo.png` · sha256:95549d1f976a · sujo
- `edicoes/2026-10-13-clima-do-dia/coleta_colunas.py` · sha256:eea4295ead46 · sujo
- `edicoes/2026-10-13-clima-do-dia/dub_work/audio.wav` · sha256:35cfaf1576bc · sujo
- `edicoes/2026-10-13-clima-do-dia/dub_work/checkpoint.json` · sha256:abde5e7b34ef · sujo
- `edicoes/2026-10-13-clima-do-dia/dub_work/whisper_gpu_result.json` · sha256:734e3ec2f652 · sujo
- `edicoes/2026-10-13-clima-do-dia/fonte/transcript.json` · sha256:b08e4adba833 · sujo
- `edicoes/2026-10-13-clima-do-dia/fonte/transcript.srt` · sha256:dfe4f8b8db34 · sujo
- `edicoes/2026-10-13-clima-do-dia/fonte/transcript.txt` · sha256:57bb75176895 · sujo
- `edicoes/2026-10-13-clima-do-dia/fonte/transcript_summary.json` · sha256:a1a31002e897 · sujo
- `edicoes/2026-10-13-clima-do-dia/gerar_cena.v1.py` · sha256:f22d34263f8c · sujo
- `edicoes/2026-10-13-clima-do-dia/narrar.py` · sha256:b2dc0ad38dc1 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/boletim.md` · sha256:b8fcc50116d7 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:ea604d7b7891 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/colunas_sul_16d.json` · sha256:805795a5bba5 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:73ddac0caa79 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:ed0f6b0eb2e1 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:d84b7bd78035 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:7a886f5f4547 · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/previsao7d.json` · sha256:a6412fc8a1cb · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/bruto/resumo.json` · sha256:4c3e311968cd · sujo
- `edicoes/2026-10-13-clima-do-dia/pesquisa/proposta.md` · sha256:14b81c105bc4 · sujo
- `edicoes/2026-10-13-clima-do-dia/previa/avatar/foto.png` · sha256:b73f7ef0c365 · sujo
- `edicoes/2026-10-13-clima-do-dia/previa/avatar/tempos.json` · sha256:f333b9b530fc · sujo
- `edicoes/2026-10-13-clima-do-dia/previa/cena.js` · sha256:f477d8b8a95e · sujo
- `edicoes/2026-10-13-clima-do-dia/previa/gerar_cena.py` · sha256:f22d34263f8c · sujo
- `edicoes/2026-10-13-clima-do-dia/refazer-visual.sh` · sha256:4a952f0a007d · sujo
- `edicoes/2026-10-13-clima-do-dia/sat/web/anomalia.png` · sha256:37a492aa6cab · sujo
- `edicoes/2026-10-13-clima-do-dia/sat/web/ir_tempos.json` · sha256:fa8e52f6c9bd · sujo
- `edicoes/2026-10-13-clima-do-dia/tempos.json` · sha256:f333b9b530fc · sujo
- `edicoes/2026-10-13-clima-do-dia/video-avatar.mp4.envio-v3.json` · sha256:3a758fdd1171 · sujo
- `edicoes/2026-10-13-clima-do-dia/video-previa.mp4.envio-v3.json` · sha256:5f9a8b87ce66 · sujo
- `edicoes/2026-10-13-mundo-7d/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-13-mundo-7d/avatar/retempo.py` · sha256:8012bc9d48db · sujo
- `edicoes/2026-10-13-mundo-7d/avatar/tempos-original.json` · sha256:49e2c64aef94 · sujo
- `edicoes/2026-10-13-mundo-7d/avatar/video_id.txt` · sha256:5156f7e0f4d9 · sujo
- `edicoes/2026-10-13-mundo-7d/falas-original.json` · sha256:57e3ddd50803 · sujo
- `edicoes/2026-10-13-mundo-7d/gerar_cena-original.py` · sha256:88d67f202d93 · sujo
- `edicoes/2026-10-13-mundo-7d/narrar.py` · sha256:589de45d4fd8 · sujo
- `edicoes/2026-10-13-mundo-7d/pesquisa/noticias.md` · sha256:76e7fc608c15 · sujo
- `edicoes/2026-10-13-mundo-7d/pesquisa/proposta.md` · sha256:dd12796b350c · sujo
- `edicoes/2026-10-13-mundo-7d/previa/.mapa.html` · sha256:f607bc88a497 · sujo
- `edicoes/2026-10-13-mundo-7d/previa/avatar/foto.png` · sha256:f00259b33535 · sujo
- `edicoes/2026-10-13-mundo-7d/previa/avatar/tempos.json` · sha256:12aa32b862a5 · sujo
- `edicoes/2026-10-13-mundo-7d/previa/cena.js` · sha256:a103de9e5009 · sujo
- `edicoes/2026-10-13-mundo-7d/previa/gerar_cena.py` · sha256:88d67f202d93 · sujo
- `edicoes/2026-10-13-mundo-7d/video-avatar-v2.mp4.envio-v3.json` · sha256:48dd2feba514 · sujo
- `edicoes/2026-10-13-mundo-7d/video-avatar.mp4.envio-v3.json` · sha256:2a68d6d22606 · sujo
- `edicoes/2026-10-13-mundo-7d/yt-original.txt` · sha256:eac4426d9051 · sujo
- `edicoes/2026-10-13-semana-foto/avatar/APROVADO_HEYGEN` · sha256:f5f47743b1d3 · sujo
- `edicoes/2026-10-13-semana-foto/avatar/fala.txt` · sha256:a666780ddf77 · sujo
- `edicoes/2026-10-13-semana-foto/avatar/retempo.py` · sha256:41e4acfe252f · sujo
- `edicoes/2026-10-13-semana-foto/avatar/tempos.json` · sha256:6904d4f879a1 · sujo
- `edicoes/2026-10-13-semana-foto/avatar/video_id.txt` · sha256:2ed9030782ec · sujo
- `edicoes/2026-10-13-semana-foto/falas.json` · sha256:cf0502b393d3 · sujo
- `edicoes/2026-10-13-semana-foto/gerar_cena.py` · sha256:fbf2a1f36e93 · sujo
- `edicoes/2026-10-13-semana-foto/narrar.py` · sha256:b2dc0ad38dc1 · sujo
- `edicoes/2026-10-13-semana-foto/om/prev15_capitais.json` · sha256:f355ea5f94e2 · sujo
- `edicoes/2026-10-13-semana-foto/om/prev15_grade.json` · sha256:17c90fd9fc30 · sujo
- `edicoes/2026-10-13-semana-foto/om/prev15_resumo.json` · sha256:8374f57d120d · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/cemaden_getJson2_todas_ufs.json` · sha256:62b683e1db2f · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/inmet_avisos_ativos.json` · sha256:73ddac0caa79 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/inmet_estacoes_tentativas.json` · sha256:ed0f6b0eb2e1 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/noaa_metar_brasil_24h.json` · sha256:03f32480e20e · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/openmeteo_capitais_3d.json` · sha256:402694e4b665 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/previsao7d.json` · sha256:16a240552e84 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/bruto/resumo.json` · sha256:1e1211248eaf · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/dados.md` · sha256:fadeeb411aa5 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/noticias.md` · sha256:41b9d3ba0d16 · sujo
- `edicoes/2026-10-13-semana-foto/pesquisa/proposta.md` · sha256:441edcfcec14 · sujo
- `edicoes/2026-10-13-semana-foto/previa/avatar/foto.png` · sha256:b73f7ef0c365 · sujo
- `edicoes/2026-10-13-semana-foto/previa/avatar/tempos.json` · sha256:1fbb83e0642a · sujo
- `edicoes/2026-10-13-semana-foto/previa/cena.js` · sha256:a0e952c5feea · sujo
- `edicoes/2026-10-13-semana-foto/previa/gerar_cena.py` · sha256:fbf2a1f36e93 · sujo
<!-- handoff-estado:fim -->
