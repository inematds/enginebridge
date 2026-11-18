# Handoff — 2026-11-18 — Mapa de públicos, reels no x3 e redes do lives2

## Projeto e escopo
Sessão aberta em ~/projetos/enginebridge, trabalho em ~/projetos/promoavatar, ~/projetos/promoavatar3, ~/projetos/inemaccbot, com leitura de ~/projetos/yt-pub-x3 e ~/projetos/radar-viral. O Nei aprovou o mapa de públicos, pediu o documento e a entrega dos reels no x3; depois perguntou por que o lives2 não tem nada nas redes, só YouTube, e disse que o lives3 está ligado no painel.

## Objetivo atual
Nei decidir se os shorts da imersão do lives2 também vão às redes. Pronto = decisão aplicada sem furar o limite de postagens do perfil inema.club24.

## Estado aceito
- [confirmed] Documento de públicos — evidência: arquivo: ~/projetos/promoavatar/docs/publicos.md
- [confirmed] Bot 0.27.12 entrega reels em yt-pub-x3/entrada/<canal> — evidência: arquivo: ~/projetos/inemaccbot/src/fila/tarefas/reel.ts; 1181 testes passaram nesta sessão
- [confirmed] Redes do lives2 ligadas no painel (canal_destino ligado=1), yaml diz false; o banco vence — evidência: arquivo: ~/projetos/yt-pub-x3/lib/runner.py
- [confirmed] Horários de redes do lives2 de 07:10 a 13:10 rodaram com "fila vazia": os 6 itens de hoje pediram só youtube — evidência: arquivo: ~/projetos/yt-pub-x3/data/x3.db
- [confirmed] Radar agenda por conta própria: finanças publicada 09:00 no Instagram e TikTok; direito pendente 15:00 — evidência: getScheduledPosts marca 7999284
- [confirmed] lives3 publicou nas redes 09:21 e 13:21; próximos 16:20 e 19:20 — evidência: arquivo: ~/projetos/yt-pub-x3/data/x3.db
- [confirmed] Crítico já usa público por canal (D29) — evidência: arquivo: ~/projetos/explicavideos/engine/v2/critico_chamada.py

## Proposto / tentado, não confirmado
- [unverified] Fluxo real do promoavatar até a publicação — só testado em pastas temporárias com textos simulados.

## Decisões
- Mapa de públicos aprovado: lives2 empreendedores, lives7 operadores, lives8 construtores.
- Perfil inema.club24 limitado pelo Nei: finanças 09:00, contábil 12:10, direito 15:00; saúde e futebol fora — fonte: ~/projetos/radar-viral/radar.json.

## Não fazer (restrições e travas)
- Não mudar destinos da imersão nem o limite do Radar sem decisão do Nei — dito em 12/11 e 17/11, gravado em ~/projetos/radar-viral/radar.json.
- Não trocar persona do crítico por conta própria; CRITICO_SEGUE=1 só com ordem dele — fonte: ~/projetos/enginebridge/handoffs/history/2026-11-18T075414Z-zelador-video-critico.md.
- Não registrar nota em nome do Nei; sem dados sensíveis no git; sem API não autorizada — dito pelo usuário, só nesta conversa.
- Commit e push só quando ele pedir — fonte: ~/.claude/CLAUDE.md.

## Arquivos alterados
- Nenhum nesta etapa (só leitura). Sem commit: `~/projetos/promoavatar` 9 itens, `~/projetos/promoavatar3` 11 itens, `~/projetos/inemaccbot` 9 itens.

## Memória e regras duráveis tocadas
- nenhuma nesta etapa

## Verificação
- Rodado: consultas sqlite só leitura em `~/projetos/yt-pub-x3/data/x3.db` → resultados acima.
- Rodado: getScheduledPosts da marca 7999284 → 4 posts em 18 e 19/11.
- Não rodado: publicação de teste nas redes do lives2 — depende da decisão.

## Estado em execução
- Processos em segundo plano: nenhum
- Servidores / portas: nenhum iniciado
- Worktrees / branches abertos: nenhum

## Perguntas abertas e adiados
- Aberta: os 3 shorts diários da imersão no lives2 vão às redes? Isso passa do limite do inema.club24.
- Aberta: commit e push dos três projetos e atualização dos guias.

## Pela metade
- Bot decide redes pelo yaml e ignora o painel — parou em: `~/projetos/inemaccbot/src/dominio/destinos.ts` linha 39 — falta: corrigir; reel do lives2 hoje iria só ao YouTube.
- Vídeo do Zelador — falta: rodar o crítico com o público novo, ficha, avatar e entrega.

## Próxima ação exata
Aguardar a resposta do Nei sobre a imersão nas redes; se sim, alterar o destino no agendador da imersão e corrigir o bot. Mudar destinos precisa da aprovação dele.

## Mapa de retomada
- `~/projetos/radar-viral/radar.json` — limite e horários das redes
- `~/projetos/yt-pub-x3/lib/entrada.py` — como nascem as entregas
- `~/projetos/imersao2026/diaria/agendador.py` — envia só youtube
- `~/projetos/inemaccbot/src/dominio/destinos.ts` — leitura do yaml

## Perguntas-teste
1. Qual é a tarefa atual e o critério de pronto? → Decidir redes dos shorts da imersão no lives2 sem furar o limite — fonte: ~/projetos/radar-viral/radar.json — chave: `imersão`
2. Qual foi a última decisão e por quê? → Mapa de públicos aprovado, para alinhar canal e conteúdo — fonte: ~/projetos/promoavatar/docs/publicos.md — chave: `públicos`
3. O que não pode mudar? → Limite de postagens do inema.club24 sem o Nei — fonte: ~/projetos/radar-viral/radar.json — chave: `inema.club24`
4. O que está pela metade? → Bot lê o yaml e ignora o painel; vídeo do Zelador — fonte: ~/projetos/inemaccbot/src/dominio/destinos.ts — chave: `yaml`
5. Qual é a próxima ação, por quê, e precisa de aprovação? → Esperar a decisão, pois muda o limite; precisa — fonte: só nesta conversa — chave: `decisão`

## Checagem de compartilhamento
- Sem segredos, tokens, cookies, dados pessoais ou endpoints privados: sim


<!-- handoff-estado:inicio -->
## Estado gravado pelo script (não editar)

Gravado por handoff-grava.py no momento do handoff. `--conferir` compara com o projeto agora.

- commit: 556d26548ceadf688dae63d053e04c1edc2ef404 · branch: main
- arquivos sujos fora de handoffs/: 0

### Repo do trabalho: /home/nmaldaner/projetos/promoavatar
- commit: 326dd66664e73e009e8eb26a3b4c822d9d074c09 · branch: master
- arquivos sujos: 9
- impressão de todos os sujos: 3b8d8f336400d97d
- `.claude/skills/inemaclub-textos/SKILL.md` · sha256:40e2e2a4e60e · sujo
- `CLAUDE.md` · sha256:8fd1b3ba5707 · sujo
- `HELP.md` · sha256:cfa3409b2481 · sujo
- `README.en.md` · sha256:d96916cdd693 · sujo
- `README.es.md` · sha256:f07866b3cc79 · sujo
- `README.md` · sha256:f818335e7529 · sujo
- `docs/canais-e-destinos.md` · sha256:ad22733886bc · sujo
- `docs/publicos.md` · sha256:18d413c4c8c5 · sujo
- `flow.json` · sha256:c192a8b20cb3 · sujo

### Repo do trabalho: /home/nmaldaner/projetos/promoavatar3
- commit: 1ee7473609d8d0e67152de3edafe1a0e13ec8be4 · branch: master
- arquivos sujos: 11
- impressão de todos os sujos: f11b9f546253cf85
- `.claude/skills/inemaclub-textos/SKILL.md` · sha256:5af887447515 · sujo
- `CLAUDE.md` · sha256:2adcac47e621 · sujo
- `HELP.md` · sha256:da9e0fac38ec · sujo
- `docs/publicos.md` · sha256:2438793d1ebf · sujo
- `flow.json` · sha256:2b6a98e9c136 · sujo
- `prompts/fase1-3versoes.md` · sha256:01d56ba08221 · sujo
- `prompts/fase1-manifesto.md` · sha256:148434c7952b · sujo
- `prompts/fase1-viral.md` · sha256:b37ff0cfa59b · sujo
- `scripts/gen_c161.py` · sha256:ef5715e33c78 · sujo
- `scripts/gen_c180.py` · sha256:fe7860476ce8 · sujo
- `scripts/gen_c92.py` · sha256:8bda52ba3ee8 · sujo

### Repo do trabalho: /home/nmaldaner/projetos/inemaccbot
- commit: 63c773e64c32b711199b03191fcffb7ab1476d93 · branch: master
- arquivos sujos: 9
- impressão de todos os sujos: 3780b49f601e9e05
- `CHANGELOG.md` · sha256:9eea99818932 · sujo
- `FALHAS.md` · sha256:80b320c7082a · sujo
- `package.json` · sha256:f4d292e508ac · sujo
- `src/dominio/destinos.ts` · sha256:6c787d4d3eaf · sujo
- `src/fila/tarefas/reel.test.ts` · sha256:ea8be7b91002 · sujo
- `src/fila/tarefas/reel.ts` · sha256:e32444acef57 · sujo
- `src/fluxos/entrada-fase.ts` · sha256:9447d8dbe9ee · sujo
- `src/integracao/promoavatar.test.ts` · sha256:ac1b804f14f2 · sujo
- `src/integracao/promoavatar3.test.ts` · sha256:f2bc5e742881 · sujo
<!-- handoff-estado:fim -->
