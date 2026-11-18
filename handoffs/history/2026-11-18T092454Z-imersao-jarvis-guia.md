# Handoff: guia da Imersão Jarvis 3D e link no portal

## Objetivo
O Nei pediu em 18/11 "publica no portal no inema.vibe" e reclamou: "nao apareceu o projeto nos ultimos projetos, apenas colocou ali o link para a simulacao". Todo projeto da lista "Últimas Atualizações de Projetos" aponta para `github.io/<repo>/guia/`; este aponta para https://eventos.inema.club/imersao-jarvis-3d/ porque nunca teve guia. Correção: criar o guia no repo `~/projetos/imersao-jarvis-3d` e trocar o link do portal para https://inematds.github.io/imersao-jarvis-3d/guia/.

## Decisão pendente (bloqueia tudo abaixo)
Pergunta feita ao Nei e ainda sem resposta: publicar o guia com a última nota 7, sem nova revisão? Não publicar, não traduzir para publicar e não mexer no portal antes da resposta.

## Estado
- Já no ar e sem mudança: evento, tópico no INEMA.VIBE (https://t.me/c/3650752323/4147), vídeo https://www.youtube.com/watch?v=zH75hEE2pzE, linha e card no portal apontando para a simulação.
- Sem commit em `~/projetos/imersao-jarvis-3d`: `guia/index.html` (PT), `guia/assets/` (banner e banner-grade em PT/EN/ES, hangar.jpg, robo-pronto.jpg, telao.jpg), `capa/capa.png`, `README.md` reescrito.
- A capa usa a captura real do robô. A primeira capa do Codex saiu parecida com um ator famoso e foi descartada; não voltar a gerar com rosto.
- Revisor independente (persona leiga): 5, 6, 6, 6,5 e 7, todas reprovadas e registradas em revisor-nota.py. Depois da nota 7 apliquei os 5 defeitos sem nova revisão.
- Testes do projeto passaram antes das últimas edições de texto do guia: `tools/validar_conteudo.py`, `node --check` em `src/*.js`, páginas locais com 200. Um revisor relatou que os comandos do README funcionaram em clone novo; meu próprio teste de clone foi negado pela permissão.

## Próximos passos, se o Nei aprovar
1. Traduzir `guia/index.html` para `guia/en/index.html` e `guia/es/index.html` com `inema-traduz` (preservar estrutura, ids, URLs; `lang`; imagens `../assets/`; banners `banner-<lang>.jpg` e `banner-grade-<lang>.jpg`; seletor de idioma com `a.on` certo). Criar `README.en.md` e `README.es.md`, que o README já cita.
2. Conferir os 3 idiomas: mesma contagem de tags, sem português sobrando, imagens carregando, sem rolagem lateral em 360 px.
3. Commit com autor inematds e push. O Pages hoje publica da branch main na raiz; a skill projetos-landing-guia pede GitHub Actions (`.github/workflows/pages.yml`, `build_type=workflow`). O remote é SSH.
4. Conferir `/guia/`, `/guia/en/`, `/guia/es/` com 200.
5. Portal (`~/projetos/portal`, autor NeiMaldaner): trocar a URL em `src/components/Portal.tsx` (card, badge de App para Guia), `src/data/courses.ts` (projectUpdatesData) e `src/data/courses.data.json` (2 lugares); incluir EN/ES em `src/data/translated-courses.ts`; rodar `~/.claude/skills/atualiza-portal/scripts/publica.sh "imersao-jarvis-3d"`. Com URL github.io, o nome do repo passa a sair em destaque na lista. Não consultar o Vercel.
6. Registrar a linha da falha em `FALHAS.md` do projeto (portal publicado sem guia; menor correção: exigir página de guia antes de publicar projeto) e a avaliação do Nei com `revisor-nota.py --quem dono`.

## Avisos
- `conteudo/evento.json` diz que a etapa 5 pede placa de vídeo, mas o guia do jarvis-painel pede só Python. O guia novo segue o painel. O evento não foi alterado; depende do Nei.
- O servidor local e a pasta temporária da sessão não existem mais; capturas de revisão precisam ser refeitas.


<!-- handoff-estado:inicio -->
## Estado gravado pelo script (não editar)

Gravado por handoff-grava.py no momento do handoff. `--conferir` compara com o projeto agora.

- commit: 1a7fa73f488ae840240e9aab9a15bb1047dd6005 · branch: main
- arquivos sujos fora de handoffs/: 0
- `guia/index.html` · sha256:c83834f0cc99 · citado
- `README.md` · sha256:8e7407f3839a · citado
- `guia/en/index.html` · sha256:9b122635632a · citado
- `guia/es/index.html` · sha256:cd85385d9659 · citado
- `README.en.md` · sha256:326bcd591edb · citado
- `README.es.md` · sha256:0e6b0f7133ff · citado
- `.github/workflows/pages.yml` · sha256:c2f5ebf259c4 · citado
- `FALHAS.md` · sha256:42b709a6d74f · citado
<!-- handoff-estado:fim -->
