# Handoff — 2026-11-18 — Publicação do guia da Imersão Jarvis 3D em andamento

## Projeto e escopo
Sessão aberta em ~/projetos/enginebridge, trabalho em ~/projetos/imersao-jarvis-3d e ~/projetos/portal. O Nei reclamou que o item no portal só levava à simulação; pediu página de projeto de verdade. Depois de 5 revisões reprovadas (5, 6, 6, 6,5, 7) respondeu "pode continuar e publicar".

## Objetivo atual
Guia publicado em PT/EN/ES e portal apontando para ele. Pronto = `/guia/`, `/guia/en/`, `/guia/es/` respondem 200 e o push do portal entrou no origin.

## Estado aceito
- [confirmed] Publicação autorizada pelo Nei — evidência: só nesta conversa ("pode continuar e publicar")
- [confirmed] Link do portal trocado localmente, sem commit — evidência: arquivo: ~/projetos/portal/src/data/courses.ts, ~/projetos/portal/src/components/Portal.tsx, ~/projetos/portal/src/data/translated-courses.ts (id 10247)
- [confirmed] Workflow de Pages criado, sem commit — evidência: arquivo: ~/projetos/imersao-jarvis-3d/.github/workflows/pages.yml

## Proposto / tentado, não confirmado
- [unverified] Tradução EN/ES de guia e README — rodando em segundo plano, resultado ainda não visto
- [?] Últimas correções do guia PT não passaram por revisor novo — o Nei aceitou publicar assim

## Decisões
- Publicar sem nova revisão — decisão do Nei.
- Portal aponta para o guia com badge "Guia"; o evento segue acessível pelo botão do guia.
- Evento e vídeos só existem em português; EN/ES avisam isso.

## Não fazer (restrições e travas)
- Não consultar nem cutucar o Vercel — fonte: ~/.claude/CLAUDE.md
- Não rodar `gh auth refresh -s workflow`; push de workflow vai por SSH — fonte: ~/.claude/CLAUDE.md
- Tradução só por inema-traduz, nunca API — fonte: ~/.claude/CLAUDE.md
- Autor: inematds no repo do projeto, NeiMaldaner no portal — fonte: ~/.claude/CLAUDE.md
- Não alterar `conteudo/evento.json` (etapa 5) sem ordem do Nei — dito nesta conversa, só nesta conversa

## Arquivos alterados
- `~/projetos/imersao-jarvis-3d/guia/`, `README.md`, `capa/`, `.github/workflows/pages.yml` — guia, artes e deploy, sem commit
- `~/projetos/portal/src/data/courses.ts`, `src/components/Portal.tsx`, `src/data/translated-courses.ts` — link e entradas EN/ES, sem commit

## Memória e regras duráveis tocadas
- nenhuma

## Verificação
- Rodado: `gh api repos/inematds/imersao-jarvis-3d/pages` → build_type legacy, status built
- Não rodado: conferência das traduções, push, URLs publicadas — ainda não chegou nessa etapa

## Estado em execução
- Processos em segundo plano: bu0qg0esv — traduz_guia.py no scratchpad da sessão
- Servidores / portas: nenhum
- Worktrees / branches abertos: nenhum

## Perguntas abertas e adiados
- Aberta: corrigir ou não a etapa 5 do evento (placa de vídeo x só Python)
- Adiado: registrar veredito do dono no revisor-nota.py quando ele julgar

## Pela metade
- Publicação — parou em: tradução rodando — falta: conferir EN/ES, commit, push por SSH, Pages em workflow, 200 nas 3 URLs, `publica.sh`, linha no FALHAS.md

## Próxima ação exata
Ao terminar a tradução, conferir tags e sobras de português em EN/ES, commitar e publicar. Já aprovado pelo Nei nesta conversa.

## Mapa de retomada
- `~/projetos/imersao-jarvis-3d/guia/index.html` — fonte PT
- `~/.claude/skills/atualiza-portal/scripts/publica.sh` — publicação do portal

## Perguntas-teste
1. Qual é a tarefa atual e o critério de pronto? → Publicar guia PT/EN/ES e apontar o portal — fonte: só nesta conversa — chave: `guia`
2. Qual foi a última decisão e por quê? → Publicar sem nova revisão, por ordem do Nei — fonte: só nesta conversa — chave: `publicar`
3. O que não pode mudar? → Não tocar no Vercel — fonte: ~/.claude/CLAUDE.md — chave: `Vercel`
4. O que está pela metade? → Tradução e publicação — fonte: só nesta conversa — chave: `tradução`
5. Qual é a próxima ação, por quê, e precisa de aprovação? → Conferir traduções e publicar; já aprovado — fonte: só nesta conversa — chave: `conferir`

## Checagem de compartilhamento
- Sem segredos, tokens, cookies, dados pessoais ou endpoints privados: sim


<!-- handoff-estado:inicio -->
## Estado gravado pelo script (não editar)

Gravado por handoff-grava.py no momento do handoff. `--conferir` compara com o projeto agora.

- commit: 130f2dab42ea94efddd60ad0b13204d755d898a8 · branch: main
- arquivos sujos fora de handoffs/: 0
- `README.md` · sha256:8e7407f3839a · citado
- `.github/workflows/pages.yml` · sha256:c2f5ebf259c4 · citado

### Repo do trabalho: /home/nmaldaner/projetos/imersao-jarvis-3d
- commit: ac51f39ec674a0714ee0515c587f998f12b08466 · branch: main
- arquivos sujos: 15
- impressão de todos os sujos: 9673cea35b64b0e9
- `.github/workflows/pages.yml` · sha256:475e621919e3 · sujo
- `README.en.md` · sha256:8f4c11a0594d · sujo
- `README.es.md` · sha256:75c6c54deea5 · sujo
- `README.md` · sha256:6481f32c0204 · sujo
- `capa/capa.png` · sha256:356df7b03cbb · sujo
- `guia/assets/banner-en.jpg` · sha256:a32d1a67e619 · sujo
- `guia/assets/banner-es.jpg` · sha256:05eb32235d56 · sujo
- `guia/assets/banner-grade-en.jpg` · sha256:5b47cbd9b18a · sujo
- `guia/assets/banner-grade-es.jpg` · sha256:5a3a98f3005b · sujo
- `guia/assets/banner-grade.jpg` · sha256:0a1d0327f352 · sujo
- `guia/assets/banner.jpg` · sha256:10f0fe922add · sujo
- `guia/assets/hangar.jpg` · sha256:8c3191b29e0a · sujo
- `guia/assets/robo-pronto.jpg` · sha256:29aa3636d4bb · sujo
- `guia/assets/telao.jpg` · sha256:008a85a4c190 · sujo
- `guia/index.html` · sha256:3c7a8fc0eca0 · sujo

### Repo do trabalho: /home/nmaldaner/projetos/portal
- commit: d5a895f0e7fd34168d9e934182fbef7cf8af3754 · branch: main
- arquivos sujos: 3
- impressão de todos os sujos: b5939c425757fd26
- `src/components/Portal.tsx` · sha256:57e54eedb032 · sujo
- `src/data/courses.ts` · sha256:44f3b22ad963 · sujo
- `src/data/translated-courses.ts` · sha256:17d04dbb36d2 · sujo
<!-- handoff-estado:fim -->
