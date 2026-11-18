# Handoff — 2026-11-18 — Guia da Imersão Jarvis 3D publicado

## Projeto e escopo
Trabalho em ~/projetos/imersao-jarvis-3d e ~/projetos/portal: guia PT/EN/ES e troca do link no portal.

## Objetivo atual
Concluído.

## Estado aceito
- [confirmed] Guia no ar nos 3 idiomas — evidência: commit 9370f81; teste: curl nas 3 URLs → 200
- [confirmed] Portal aponta para o guia — evidência: commit 76bb760

## Proposto / tentado, não confirmado
- [unverified] Atualização visível no inema.club — o Vercel não é consultado, por regra

## Decisões
- Publicado sem nova revisão, por decisão do Nei.

## Não fazer (restrições e travas)
- Não consultar o Vercel — fonte: ~/.claude/CLAUDE.md
- Não alterar `conteudo/evento.json` sem ordem do Nei — dito em 18/11, só nesta conversa

## Arquivos alterados
- Fora do projeto: ~/projetos/imersao-jarvis-3d, ~/projetos/portal, ~/projetos/inemabuscas, ~/projetos/inemapro-mono — publicados por commit

## Memória e regras duráveis tocadas
- nenhuma

## Verificação
- Rodado: `gh run watch` → sucesso; curl → 200 em /guia/, /guia/en/, /guia/es/
- Rodado: teste em 360 px → sem rolagem horizontal, sem imagem quebrada
- Não rodado: revisor novo na versão final; conferência no Vercel

## Estado em execução
- Processos em segundo plano: nenhum
- Servidores / portas: nenhum
- Worktrees / branches abertos: nenhum

## Perguntas abertas e adiados
- Aberta: corrigir a etapa 5 do evento; responder o tópico do INEMA.VIBE com o link do guia

## Pela metade
- nada

## Próxima ação exata
Aguardar o Nei sobre as perguntas abertas.

## Mapa de retomada
- `~/projetos/imersao-jarvis-3d/guia/index.html` — fonte PT

## Perguntas-teste
1. Qual é a tarefa atual e o critério de pronto? → Concluída — fonte: commit 76bb760 — chave: `concluída`
2. Qual foi a última decisão e por quê? → Publicar sem nova revisão, ordem do Nei — fonte: só nesta conversa — chave: `publicar`
3. O que não pode mudar? → Não tocar no Vercel — fonte: ~/.claude/CLAUDE.md — chave: `Vercel`
4. O que está pela metade? → Nada — fonte: commit 76bb760 — chave: `nada`
5. Qual é a próxima ação, por quê, e precisa de aprovação? → Esperar o Nei — fonte: só nesta conversa — chave: `Nei`

## Checagem de compartilhamento
- Sem segredos, tokens, cookies, dados pessoais ou endpoints privados: sim


<!-- handoff-estado:inicio -->
## Estado gravado pelo script (não editar)

Gravado por handoff-grava.py no momento do handoff. `--conferir` compara com o projeto agora.

- commit: 40cacbff02f2290c65edc1b3eae2f594418ebec8 · branch: main
- arquivos sujos fora de handoffs/: 0

### Repo do trabalho: /home/nmaldaner/projetos/imersao-jarvis-3d
- commit: 10e6a59aa0dd29b0c04a10665df48a3ea0820b02 · branch: main
- arquivos sujos: 0
- impressão de todos os sujos: e3b0c44298fc1c14

### Repo do trabalho: /home/nmaldaner/projetos/portal
- commit: 76bb7609b64b591d62cf26442df601f24cb9f8f8 · branch: main
- arquivos sujos: 0
- impressão de todos os sujos: e3b0c44298fc1c14

### Repo do trabalho: /home/nmaldaner/projetos/inemapro-mono
- commit: 5731554f1f79dcd0a67423b02b39413b28cfb237 · branch: main
- arquivos sujos: 0
- impressão de todos os sujos: e3b0c44298fc1c14

### Repo do trabalho: /home/nmaldaner/projetos/inemabuscas
- commit: 6051c8834508f1e5c5ab9fe42c34ef574176d55c · branch: main
- arquivos sujos: 1
- impressão de todos os sujos: 63646c65118cfc41
- `.claude/claudex/log` · sha256:93bedf6ca093 · sujo
<!-- handoff-estado:fim -->
