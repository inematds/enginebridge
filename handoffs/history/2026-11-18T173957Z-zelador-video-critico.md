# Handoff — 2026-11-18 — Zelador no lives7: crítico aprovado e cadeia do vídeo em execução

## Projeto e escopo
Sessão aberta em ~/projetos/enginebridge, trabalho em ~/projetos/explicavideos (produção `textos/zelador-lives7`, ignorada pelo git). O Nei respondeu "sim pode publicar" à pergunta "rodo agora o crítico do Zelador e, se passar, sigo para o avatar?". Isso cobre crítico, avatar pelo estúdio HeyGen e publicação no lives7.

## Objetivo atual
Vídeo do Zelador publicado no lives7. Pronto quando `textos/zelador-lives7/cadeia.log` terminar em `ok: <BOT-FIM.md>` e o link do YouTube existir.

## Estado aceito
- [confirmed] Crítico da chamada aprovou com nota 8, 3 leituras, todas as 8 perguntas em sim — evidência: arquivo: ~/projetos/explicavideos/textos/zelador-lives7/chamada-critica.json
- [confirmed] Portão de forma passou — evidência: teste: `python3 engine/v2/checar_chamada.py textos/zelador-lives7` → `chamada ok`
- [confirmed] Configs e bloco prontos: 1 bloco, 10 cenas, 3527 caracteres — evidência: arquivo: ~/projetos/output/zelador-20261117/v1/blocos/manifest.json
- [confirmed] Ficha fechada à mão, sem novo `claude -p` — evidência: arquivo: ~/projetos/explicavideos/textos/zelador-lives7/ficha.recibo

## Proposto / tentado, não confirmado
- [unverified] Envio ao HeyGen, visual, render e publicação — a cadeia acabou de ser lançada, sem resultado observado.

## Decisões
- Não rodar de novo a fase ficha — o `regras.md` tinha a chamada antiga e o `claude -p` poderia reescrever a chamada que o Nei pediu em 18/11.
- `regras.md` atualizado para a chamada atual e selo "AGENTE ZELADOR" — a fase visual recebe esse arquivo como regra acima de tudo.

## Não fazer (restrições e travas)
- Nunca reenviar ao HeyGen se houver envio sem id; olhar Projetos no estúdio — fonte: ~/projetos/explicavideos/textos/zelador/avatar-fila.sh
- Nunca trocar plano do HeyGen; estúdio para criar, API só para status e download — fonte: ~/.claude/CLAUDE.md
- `CRITICO_SEGUE=1` e `CRITICO_RODADA_EXTRA=1` só por ordem do Nei — fonte: ~/projetos/explicavideos/prompts/bot-ficha.md
- Nada da máquina real na tela ou na fala — fonte: ~/projetos/explicavideos/textos/zelador/regras-comuns.md
- Exclusão no Telegram exige aprovação individual; publicar = commit + push; não consultar Vercel — fonte: ~/.claude/CLAUDE.md
- Não usar API sem autorização, exceto GitHub, publicação nas redes e status/download do HeyGen — fonte: ~/.claude/CLAUDE.md

## Arquivos alterados
- Fora do projeto: `~/projetos/explicavideos/textos/zelador-lives7/regras.md` — chamada atual; cópia anterior em `.tentativa1/regras-antes-18nov.md`
- Fora do projeto: `~/projetos/explicavideos/textos/zelador-lives7/RESUMO.md`, `ficha.recibo`, `v1.json`, `v2.json`, `chamada-critica.json` — fechamento da ficha
- Fora do projeto: `~/projetos/output/zelador-20261117/v1/APROVADO_HEYGEN` — registra o OK do Nei

## Memória e regras duráveis tocadas
- nenhuma nesta etapa; `~/.claude/projects/-home-nmaldaner-projetos-enginebridge/memory/zelador-publicacao.md` precisa ser atualizada quando o vídeo sair.

## Verificação
- Rodado: `python3 engine/v2/critico_chamada.py textos/zelador-lives7` → `chamada forte`, nota 8, saída 0
- Rodado: `python3 engine/v2/checar_chamada.py textos/zelador-lives7` → `chamada ok`
- Rodado: `python3 bot/configs.py` e `python3 explica.py --config .../v1.json prepare` → saída 0, 1 bloco, 3527 caracteres
- Não rodado: conferência do vídeo final — ainda não existe.

## Estado em execução
- Processos em segundo plano: shell b3s2lcgil, `bash ../zelador/roda.sh` em `textos/zelador-lives7`, com log em `cadeia.log`; se a sessão fechar, relançar retoma pelo id gravado no manifest.
- Servidores / portas: nenhum
- Worktrees / branches abertos: nenhum

## Perguntas abertas e adiados
- Adiado: embed no lugar de `<!-- VIDEO` nos 3 guias, linha "Vídeo:" nos READMEs, portal e resposta no tópico — dependem do link do YouTube.

## Pela metade
- Vídeo do Zelador — parou em: cadeia lançada na fase avatar — falta: avatar, visual, render e publicação.

## Próxima ação exata
Aguardar o fim da cadeia e ler `cadeia.log`. Se `ok`, conferir o vídeo e fazer as entregas adiadas; se `erro`, tratar sem reenviar ao HeyGen sem olhar o estúdio.

## Mapa de retomada
- `~/projetos/explicavideos/textos/zelador-lives7/cadeia.log` — estado da cadeia
- `~/projetos/explicavideos/textos/zelador/roda.sh` — ordem das fases
- `~/projetos/explicavideos/textos/zelador-lives7/regras.md` — regras vigentes
- `~/.claude/projects/-home-nmaldaner-projetos-enginebridge/memory/zelador-publicacao.md` — entregas depois do vídeo

## Perguntas-teste
1. Qual é a tarefa atual e o critério de pronto? → Publicar o Zelador no lives7, com `ok:` no log — fonte: ~/projetos/explicavideos/textos/zelador/roda.sh — chave: `lives7`
2. Qual foi a última decisão e por quê? → Não refazer a ficha, para preservar a chamada do Nei — fonte: ~/projetos/explicavideos/textos/zelador-lives7/regras.md — chave: `CHAMADA FECHADA`
3. O que não pode mudar? → Não reenviar ao HeyGen sem id — fonte: ~/projetos/explicavideos/textos/zelador/avatar-fila.sh — chave: `reenvi`
4. O que está pela metade? → A cadeia avatar, visual, entrega — fonte: ~/projetos/explicavideos/textos/zelador-lives7/cadeia.log — chave: `avatar`
5. Qual é a próxima ação, por quê, e precisa de aprovação? → Ler o log ao fim da cadeia; publicação já aprovada, exclusões não — fonte: só nesta conversa — chave: `cadeia.log`

## Checagem de compartilhamento
- Sem segredos, tokens, cookies, dados pessoais ou endpoints privados: sim


<!-- handoff-estado:inicio -->
## Estado gravado pelo script (não editar)

Gravado por handoff-grava.py no momento do handoff. `--conferir` compara com o projeto agora.

- commit: ae94c7dad4a7ccd14c97f70f382760be5b26ce0d · branch: main
- arquivos sujos fora de handoffs/: 0

### Repo do trabalho: /home/nmaldaner/projetos/explicavideos
- commit: 0422720b5939de8000d51d725921039f19cd0bec · branch: main
- arquivos sujos: 408 (lista cortada)
- impressão de todos os sujos: 8bc88ea71872c716
- `FALHAS.md` · sha256:684fe2d8b4fb · sujo
- `engine/build_visual_block.py` · sha256:cad49c345580 · sujo
- `engine/v2/build_block.py` · sha256:9051bdec5ca6 · sujo
- `engine/v2/runtime/viral.js` · sha256:78ba890403fe · sujo
- `examples/1AzRvvF3n5-v2.json` · sha256:2e008191171a · sujo
- `examples/1AzRvvF3n5.json` · sha256:8c5223f53b62 · sujo
- `examples/1DamuwTfJa-v2.json` · sha256:c35c0d100f41 · sujo
- `examples/1DamuwTfJa.json` · sha256:443bb5f65468 · sujo
- `examples/1KXMjGvJ3V-v2.json` · sha256:fea40c513394 · sujo
- `examples/1KXMjGvJ3V.json` · sha256:211be4f9d107 · sujo
- `examples/agent-skills-addy-v2.json` · sha256:9ad0204762dc · sujo
- `examples/agent-skills-addy.json` · sha256:5c442c38f282 · sujo
- `examples/agentes-autoaprimoram-v2-916.json` · sha256:2c1923c98eee · sujo
- `examples/agentes-autoaprimoram-v2.json` · sha256:3d4e514cbc17 · sujo
- `examples/agentes-autoaprimoram.json` · sha256:ad131c05ebeb · sujo
- `examples/agentic-app-framework-v2-916.json` · sha256:4aa119ffcdd0 · sujo
- `examples/agentic-app-framework-v2.json` · sha256:139af6d17f17 · sujo
- `examples/agentic-app-framework.json` · sha256:9e2734a970f1 · sujo
- `examples/agentic-app-ideia-v2-916.json` · sha256:86020923fe2c · sujo
- `examples/agentic-app-ideia-v2.json` · sha256:18888b26ac25 · sujo
- `examples/agentic-app-ideia.json` · sha256:2468f5c9a821 · sujo
- `examples/agentic-app-v2.json` · sha256:c99f76d6c8f7 · sujo
- `examples/agentic-app.json` · sha256:94b0e4c2807b · sujo
- `examples/ai-harness-en-v2.json` · sha256:b09427331b28 · sujo
- `examples/ai-harness-en.json` · sha256:7f55ecd84689 · sujo
- `examples/ai-harness-es-v2.json` · sha256:8c225a40ad85 · sujo
- `examples/ai-harness-es.json` · sha256:c1caae4e3c7e · sujo
- `examples/ai-harness-pro-en-v2.json` · sha256:6044d99333a0 · sujo
- `examples/ai-harness-pro-es-v2.json` · sha256:c46dcd225af0 · sujo
- `examples/ai-harness-pro-v2.json` · sha256:82a0cf7b27ce · sujo
- `examples/ai-harness-v2.json` · sha256:17615e01eecd · sujo
- `examples/ai-harness.json` · sha256:53a388c69613 · sujo
- `examples/ai2027-adiantado-v2-916.json` · sha256:ec73dff41d69 · sujo
- `examples/ai2027-adiantado-v2.json` · sha256:d6c46f3108ed · sujo
- `examples/ai2027-adiantado.json` · sha256:06089649c824 · sujo
- `examples/apagao-sem-gerador-v2-916.json` · sha256:d11be9da34b9 · sujo
- `examples/apagao-sem-gerador-v2.json` · sha256:dcc706677bed · sujo
- `examples/apagao-sem-gerador.json` · sha256:5b759516ea09 · sujo
- `examples/apocalipse-seguranca-v2-916.json` · sha256:a3db2de5e145 · sujo
- `examples/apocalipse-seguranca-v2.json` · sha256:f866ea2cabd2 · sujo
- `examples/apocalipse-seguranca.json` · sha256:53dbaf20c009 · sujo
- `examples/astra-caixa-preta-v2-916.json` · sha256:25464dede49f · sujo
- `examples/astra-caixa-preta-v2.json` · sha256:cf15c5357aa6 · sujo
- `examples/astra-caixa-preta.json` · sha256:eb4c6efd95d5 · sujo
- `examples/atende-academia-promo-v2.json` · sha256:fead886d2dd7 · sujo
- `examples/atende-academia-promo.json` · sha256:7ff7e4c97848 · sujo
- `examples/atende-fisioterapia-promo-v2.json` · sha256:63b963dcff02 · sujo
- `examples/atende-fisioterapia-promo.json` · sha256:80f787091913 · sujo
- `examples/atende-leads-demo-v2-916.json` · sha256:a175f3e76db7 · sujo
- `examples/atende-leads-demo-v2.json` · sha256:0840bd1c893d · sujo
- `examples/atende-leads-demo.json` · sha256:84b23ed447c1 · sujo
- `examples/atende-leads-promo-v2-916.json` · sha256:c1d04ef36254 · sujo
- `examples/atende-leads-promo-v2.json` · sha256:d9546c0d96b5 · sujo
- `examples/atende-leads-promo.json` · sha256:f7ecd433457e · sujo
- `examples/atende-nutricao-promo-v2.json` · sha256:990e1b2b5929 · sujo
- `examples/atende-nutricao-promo.json` · sha256:d8abd91ee368 · sujo
- `examples/bigtech-boazinhas-v2.json` · sha256:73a6c6fc36a0 · sujo
- `examples/bigtech-boazinhas.json` · sha256:6e725dd88814 · sujo
- `examples/bigtech-paga-b-v2.json` · sha256:65316fd6e7cd · sujo
- `examples/bigtech-paga-v2.json` · sha256:191277923e1e · sujo
- `examples/bigtech-paga.json` · sha256:8ebefd1a9d24 · sujo
- `examples/camada-contexto-v2.json` · sha256:2fdee0374316 · sujo
- `examples/camada-contexto.json` · sha256:d43a6c31b6ae · sujo
- `examples/ccdashboard-reel-v2.json` · sha256:0c5d76cea62d · sujo
- `examples/ccdashboard-reel.json` · sha256:d838b9059038 · sujo
- `examples/cerebro-niveis-v2.json` · sha256:a95ad96a56b5 · sujo
- `examples/cerebro-niveis.json` · sha256:8d4ce7c43df9 · sujo
- `examples/cga-a1-v2.json` · sha256:91e0b46ce07e · sujo
- `examples/cga-a1.json` · sha256:260c4ce04c6a · sujo
- `examples/cga-a2-v2.json` · sha256:6ed4a1b200d6 · sujo
- `examples/cga-a2.json` · sha256:8bf12d77d988 · sujo
- `examples/cga-a3-v2.json` · sha256:c479e734495d · sujo
- `examples/cga-a3.json` · sha256:54b7b58d96fb · sujo
- `examples/cga-a4-v2.json` · sha256:48310a8f7b6e · sujo
- `examples/cga-a4.json` · sha256:1ec38bc6d4dd · sujo
- `examples/cga-a5-v2.json` · sha256:0825ac19fe22 · sujo
- `examples/cga-a5.json` · sha256:9f5a8b2ab6fb · sujo
- `examples/cga-a6-v2.json` · sha256:09358cb46bb0 · sujo
- `examples/cga-a6.json` · sha256:ef4d5bd66ec4 · sujo
- `examples/cga-a7-v2.json` · sha256:6f424c7a63ac · sujo
- `examples/cga-a7.json` · sha256:6e9b4d429bc4 · sujo
- `examples/cga-a8-v2.json` · sha256:588f87836979 · sujo
- `examples/cga-a8.json` · sha256:3a3ff44dfd05 · sujo
- `examples/chatgpt-16-ferramentas-v2-916.json` · sha256:55be535b713c · sujo
- `examples/chatgpt-16-ferramentas-v2.json` · sha256:03761b9b83f6 · sujo
- `examples/chatgpt-16-ferramentas.json` · sha256:93f2a412f3db · sujo
- `examples/claude-estudio-video-v2.json` · sha256:afdb9a0f9528 · sujo
- `examples/claude-estudio-video.json` · sha256:7d9da0be39b8 · sujo
- `examples/clone-viral-hypit-v2.json` · sha256:c0dea4fb3de1 · sujo
- `examples/clone-viral-hypit.json` · sha256:2fffc442ec1d · sujo
- `examples/concat-anim-v2-916.json` · sha256:4a5a3aece349 · sujo
- `examples/concat-anim.json` · sha256:53c225fd0fad · sujo
- `examples/concat-viral-916-v2.json` · sha256:6ef93f48af79 · sujo
- `examples/concat-viral-916.json` · sha256:4791c7ce5b26 · sujo
- `examples/consultor-ia-2027-en-v2.json` · sha256:d1053f809fc7 · sujo
- `examples/consultor-ia-2027-en.json` · sha256:2b0c27df929b · sujo
- `examples/consultor-ia-2027-es-v2.json` · sha256:975981b70925 · sujo
- `examples/consultor-ia-2027-es.json` · sha256:0c3d5105d16a · sujo
- `examples/consultoria-ia-caminhos-en-v2.json` · sha256:7872b51291be · sujo
- `examples/consultoria-ia-caminhos-en.json` · sha256:73df53a074b1 · sujo
- `examples/consultoria-ia-caminhos-es-v2.json` · sha256:2ea5d5ef3fc1 · sujo
- `examples/consultoria-ia-caminhos-es.json` · sha256:43e3531e09a2 · sujo
- `examples/consultoria-ia-na-pratica-en-v2.json` · sha256:9a4260a201c9 · sujo
- `examples/consultoria-ia-na-pratica-en.json` · sha256:dbc7168400f7 · sujo
- `examples/consultoria-ia-na-pratica-es-v2.json` · sha256:59ba851b7cdc · sujo
- `examples/consultoria-ia-na-pratica-es.json` · sha256:bf626e47b22c · sujo
- `examples/consultoria-ia-na-pratica-v2.json` · sha256:bf69082e5382 · sujo
- `examples/consultoria-ia-na-pratica.json` · sha256:e2e5b348ae67 · sujo
- `examples/contexto-portatil-v2.json` · sha256:78153674fb68 · sujo
- `examples/contexto-portatil.json` · sha256:8e71552e5c0e · sujo
- `examples/craft-anything-v2-916.json` · sha256:bcec22b2cea3 · sujo
- `examples/craft-anything-v2.json` · sha256:666a5c7a80e2 · sujo
- `examples/craft-anything.json` · sha256:9b853ae8f8b1 · sujo
- `examples/csm-a1-v2.json` · sha256:79f5be7a983a · sujo
- `examples/csm-a1.json` · sha256:6e94ee938289 · sujo
- `examples/csm-a2-v2.json` · sha256:e3a874ce18e4 · sujo
- `examples/csm-a2.json` · sha256:4c238de76063 · sujo
- `examples/csm-a3-v2.json` · sha256:eff2c2d11dea · sujo
- `examples/csm-a3.json` · sha256:683bccf051bd · sujo
- `examples/csm-a4-v2.json` · sha256:808e25435339 · sujo
- `examples/csm-a4.json` · sha256:8b1e8a863de6 · sujo
- `examples/csm-a5-v2.json` · sha256:bec2a40d2068 · sujo
- `examples/csm-a5.json` · sha256:0748302f8bd0 · sujo
- `examples/csm-a6-v2.json` · sha256:b8253af48c0a · sujo
- `examples/csm-a6.json` · sha256:c4a6be50155f · sujo
- `examples/csm-a7-v2.json` · sha256:2434205d6321 · sujo
- `examples/csm-a7.json` · sha256:32d7e2086d43 · sujo
- `examples/csm-visao-v2.json` · sha256:4a19eb7474e6 · sujo
- `examples/csm-visao.json` · sha256:47e22b8195b4 · sujo
- `examples/decisions-jev-en-v2.json` · sha256:8ecb238e4653 · sujo
- `examples/decisions-jev-en.json` · sha256:676529ccb25d · sujo
- `examples/decisions-jev-es-v2.json` · sha256:f193bb3d2c2b · sujo
- `examples/decisions-jev-es.json` · sha256:84c618d6a478 · sujo
- `examples/decisions-jev-v2.json` · sha256:74806bcc1a3c · sujo
- `examples/decisions-jev.json` · sha256:5d3863296f9a · sujo
- `examples/deepseek-ia-hacker-v2-916.json` · sha256:1bd95abe02cd · sujo
- `examples/deepseek-ia-hacker-v2.json` · sha256:485a395b9cab · sujo
- `examples/deepseek-ia-hacker.json` · sha256:215e8d604fe5 · sujo
- `examples/devia62-m1-v2.json` · sha256:95aac03bab69 · sujo
- `examples/devia62-m1.json` · sha256:0fb26b5bad2c · sujo
- `examples/diga-o-que-importa-v2.json` · sha256:3a990601df58 · sujo
- `examples/diga-o-que-importa.json` · sha256:b30efd31b1c1 · sujo
- `examples/diga-v1-v2.json` · sha256:06de6e73d08e · sujo
- `examples/diga-v1.json` · sha256:231e9ddc6b1e · sujo
- `examples/empresas-2027-en-v2.json` · sha256:324c3a9d1ce0 · sujo
- `examples/empresas-2027-en.json` · sha256:908f12e38fb4 · sujo
- `examples/empresas-2027-es-v2.json` · sha256:7b221127a6b4 · sujo
- `examples/empresas-2027-es.json` · sha256:9ae4854d5505 · sujo
- `examples/empresas-2027-v2.json` · sha256:1a682c49638b · sujo
- `examples/empresas-2027.json` · sha256:e4f1d8b77e9e · sujo
- `examples/emudhra-chave-4-v2.json` · sha256:4c0ff49dc558 · sujo
- `examples/emudhra-chave-4.json` · sha256:9d74ea643f0d · sujo
- `examples/esforco-fable-testes-v2-916.json` · sha256:80169187d862 · sujo
- `examples/esforco-fable-testes-v2.json` · sha256:0141f3d16666 · sujo
- `examples/esforco-fable-testes.json` · sha256:1e52d324e40f · sujo
- `examples/execucao-longa-pratica-v2.json` · sha256:6ece5cd6235b · sujo
- `examples/execucao-longa-pratica.json` · sha256:53615a8ca489 · sujo
- `examples/fable-opus-esforco-v2-916.json` · sha256:65953e4da967 · sujo
- `examples/fable-opus-esforco-v2.json` · sha256:fc0045bf116f · sujo
- `examples/fable-opus-esforco.json` · sha256:1af5b62e02de · sujo
- `examples/faxina-agentes-v2.json` · sha256:067c4fb48293 · sujo
- `examples/faxina-agentes.json` · sha256:1d22366b8e86 · sujo
- `examples/fim-capitalismo-v2.json` · sha256:a0b54e1d5dd1 · sujo
- `examples/fim-capitalismo.json` · sha256:acef6679f896 · sujo
- `examples/fim-dos-agentes-v2-916.json` · sha256:8110479f1ec1 · sujo
- `examples/fim-dos-agentes-v2.json` · sha256:5f03948d0857 · sujo
- `examples/fim-dos-agentes.json` · sha256:ad95f0351db5 · sujo
- `examples/fim-mundo-1960-v2-916.json` · sha256:1a46781eec35 · sujo
- `examples/fim-mundo-1960-v2.json` · sha256:c5ba8e7b9aef · sujo
- `examples/fim-mundo-1960.json` · sha256:18d8d71dc026 · sujo
- `examples/form-gestao-v2.json` · sha256:143cc45600dd · sujo
- `examples/form-gestao.json` · sha256:6f7f6b54d880 · sujo
- `examples/form-loopr-v2.json` · sha256:488201c9f6ef · sujo
- `examples/form-loopr.json` · sha256:b31203efc0e9 · sujo
- `examples/form-prof2030-v2.json` · sha256:76ab9a045c6f · sujo
- `examples/form-prof2030.json` · sha256:c25dbad58cb0 · sujo
- `examples/form-seo-v2.json` · sha256:7ca2f25a8930 · sujo
- `examples/form-seo.json` · sha256:19f3bf532401 · sujo
- `examples/form-vendas-v2.json` · sha256:d2c7bb91a2aa · sujo
- `examples/form-vendas.json` · sha256:d75f11f41253 · sujo
- `examples/gates-sofrer-2027-v2-916.json` · sha256:1452b3c98e95 · sujo
- `examples/gates-sofrer-2027-v2.json` · sha256:a52d05546ed2 · sujo
- `examples/gates-sofrer-2027.json` · sha256:1842dccd8e66 · sujo
- `examples/gerente-de-agentes-en-v2.json` · sha256:ba9d00d8c13a · sujo
- `examples/gerente-de-agentes-en.json` · sha256:1291208e45a3 · sujo
- `examples/gerente-de-agentes-es-v2.json` · sha256:4ca686706cc4 · sujo
- `examples/gerente-de-agentes-es.json` · sha256:6526a599d511 · sujo
- `examples/gestao-ia-caminhos-en-v2.json` · sha256:6177c0beaf3e · sujo
- `examples/gestao-ia-caminhos-en.json` · sha256:e14b05d9c0d7 · sujo
- `examples/gestao-ia-caminhos-es-v2.json` · sha256:09ec9a427a69 · sujo
- `examples/gestao-ia-caminhos-es.json` · sha256:a7045fa2dcc8 · sujo
- `examples/gestao-ia-caminhos-v2.json` · sha256:83bcb001106f · sujo
- `examples/gestao-ia-caminhos.json` · sha256:41b43a9b4f80 · sujo
- `examples/gestor-de-agentes-en-v2.json` · sha256:a0e96df7d2fb · sujo
- `examples/gestor-de-agentes-en.json` · sha256:7a45007cd09c · sujo
- `examples/gestor-de-agentes-es-v2.json` · sha256:b05461471627 · sujo
- `examples/gestor-de-agentes-es.json` · sha256:5589bfeaccf8 · sujo
- `examples/git-jardineiro-v2.json` · sha256:5f88a9cb0cb9 · sujo
- `examples/git-jardineiro.json` · sha256:1023e190c3d8 · sujo
- `examples/google-carbon-v2.json` · sha256:f9432f930afe · sujo
<!-- handoff-estado:fim -->
