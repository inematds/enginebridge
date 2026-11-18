# Handoff: guia da Imersão Jarvis 3D e link no portal

## Objetivo
O Nei pediu em 18/11 "publica no portal no inema.vibe" e reclamou: "nao apareceu o projeto nos ultimos projetos, apenas colocou ali o link para a simulacao". Todo projeto da lista "Últimas Atualizações de Projetos" aponta para `github.io/<repo>/guia/`; este aponta para https://eventos.inema.club/imersao-jarvis-3d/ porque nunca teve guia. Correção: criar o guia no repo `~/projetos/imersao-jarvis-3d` e trocar o link do portal para https://inematds.github.io/imersao-jarvis-3d/guia/.

## Decisão pendente (bloqueia tudo abaixo)
Pergunta feita ao Nei e ainda sem resposta: publicar o guia com a última nota 7, sem nova revisão?

## Não fazer
- Não publicar o guia, não dar push e não mexer no portal antes da resposta do Nei.
- Não consultar nem re-disparar o Vercel; o trabalho termina no push.
- Não usar API para traduzir: só `inema-traduz`, pela assinatura.
- Não gerar imagem com o inemaimg nem com modelo local sem aprovação; imagem é pelo Codex.
- Não usar capa com rosto de pessoa: a primeira saiu parecida com um ator famoso e foi descartada.
- Não pôr comando nem parte técnica no guia; isso fica no README.
- Não editar `fonte/`, `marca/`, `vendor/`, `tools/`, `processo/BRIEFING.md`, `processo/prompts/`, `processo/rodadas/` nem `longrun/` do projeto.
- Não alterar `conteudo/evento.json` sem o Nei decidir.
- Autor: inematds no repo imersao-jarvis-3d; NeiMaldaner no portal.

## Estado
- Já no ar e sem mudança: evento, tópico no INEMA.VIBE (https://t.me/c/3650752323/4147), vídeo https://www.youtube.com/watch?v=zH75hEE2pzE, linha e card no portal apontando para a simulação.
- Sem commit em `~/projetos/imersao-jarvis-3d`: `guia/index.html` (PT), `guia/assets/` (banner e banner-grade em PT/EN/ES, hangar.jpg, robo-pronto.jpg, telao.jpg), `capa/capa.png`, `README.md` reescrito.
- Revisor independente (persona leiga): 5, 6, 6, 6,5 e 7, todas reprovadas e registradas em revisor-nota.py. Depois da nota 7 apliquei os 5 defeitos sem nova revisão.
- Testes do projeto passaram antes das últimas edições de texto do guia: `tools/validar_conteudo.py`, `node --check` em `src/*.js`, páginas locais com 200. Um revisor relatou que os comandos do README funcionaram em clone novo; meu próprio teste de clone foi negado pela permissão.

## Próximos passos, se o Nei aprovar
1. Traduzir `guia/index.html` para `guia/en/index.html` e `guia/es/index.html` com `inema-traduz` (preservar estrutura, ids, URLs; `lang`; imagens `../assets/`; banners `banner-<lang>.jpg` e `banner-grade-<lang>.jpg`; seletor de idioma com `a.on` certo). Criar `README.en.md` e `README.es.md`, que o README já cita.
2. Conferir os 3 idiomas: mesma contagem de tags, sem português sobrando, imagens carregando, sem rolagem lateral em 360 px.
3. Commit e push. O Pages hoje publica da branch main na raiz; a skill projetos-landing-guia pede GitHub Actions (`.github/workflows/pages.yml`, `build_type=workflow`). O remote é SSH.
4. Conferir `/guia/`, `/guia/en/`, `/guia/es/` com 200.
5. Portal (`~/projetos/portal`): trocar a URL em `src/components/Portal.tsx` (card, badge de App para Guia), `src/data/courses.ts` (projectUpdatesData) e `src/data/courses.data.json` (2 lugares); incluir EN/ES em `src/data/translated-courses.ts`; rodar `~/.claude/skills/atualiza-portal/scripts/publica.sh "imersao-jarvis-3d"`. Com URL github.io, o nome do repo passa a sair em destaque na lista.
6. Registrar a linha da falha em `FALHAS.md` do projeto (portal publicado sem guia; menor correção: exigir página de guia antes de publicar projeto) e a avaliação do Nei com `revisor-nota.py --quem dono`.

## Avisos
- `conteudo/evento.json` diz que a etapa 5 pede placa de vídeo, mas o guia do jarvis-painel pede só Python. O guia novo segue o painel.
- O servidor local e a pasta temporária da sessão não existem mais; capturas de revisão precisam ser refeitas.

## Perguntas-teste
1. O que impede publicar agora? Resposta: falta o Nei dizer se aceita a nota 7 sem nova revisão.
2. Por que o projeto não apareceu como os outros? Resposta: o portal aponta para a simulação, porque não havia guia em `github.io/imersao-jarvis-3d/guia/`.
3. Onde está o trabalho não commitado? Resposta: em `guia/`, `capa/` e `README.md` do repo imersao-jarvis-3d.
4. Quais arquivos do portal mudam? Resposta: `Portal.tsx`, `courses.ts`, `courses.data.json` e `translated-courses.ts`.
5. Com o que traduzir, e o que falta criar além do guia EN/ES? Resposta: `inema-traduz`; faltam `README.en.md` e `README.es.md`.


<!-- handoff-estado:inicio -->
## Estado gravado pelo script (não editar)

Gravado por handoff-grava.py no momento do handoff. `--conferir` compara com o projeto agora.

- commit: 1a34b35d1fe4b2a4279cb95fc78fdce93200d211 · branch: main
- arquivos sujos fora de handoffs/: 0
- `guia/index.html` · sha256:c83834f0cc99 · citado
- `README.md` · sha256:8e7407f3839a · citado
- `guia/en/index.html` · sha256:9b122635632a · citado
- `guia/es/index.html` · sha256:cd85385d9659 · citado
- `README.en.md` · sha256:326bcd591edb · citado
- `README.es.md` · sha256:0e6b0f7133ff · citado
- `.github/workflows/pages.yml` · sha256:c2f5ebf259c4 · citado
- `FALHAS.md` · sha256:42b709a6d74f · citado

### Repo do trabalho: /home/nmaldaner/projetos/imersao-jarvis-3d
- commit: ac51f39ec674a0714ee0515c587f998f12b08466 · branch: main
- arquivos sujos: 12
- impressão de todos os sujos: 02cd6d2161228419
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
- commit: 204145111fae5baa93b615f00a1f70bf99236087 · branch: main
- arquivos sujos: 0
- impressão de todos os sujos: e3b0c44298fc1c14
<!-- handoff-estado:fim -->
