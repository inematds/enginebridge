# Handoff — ia-sem-estrago-videos — 18/11/2026

Vídeos A e B do kit IA sem estrago na fila do yt-pub-x3; faltam conferir a publicação e fazer guia, portal e Telegram.

Assunto novo: esta sessão não tinha handoff próprio. O `zelador-video-critico` do índice é outro trabalho (nenhum snapshot dele cita este kit), por isso não usei esse nome.

## Pedidos do Nei (literais)
- "pode póstar os videos no x3"
- "pode montar mesmo assim com a narracao, se o critico questionar eu disewe q pode sari e publcia no x3 ok"
- Ordem de 17/11: "faca dois videos um para quenm conhece o cluade, e outros para quem esta comecando e coloca eles no guia, o q ja conhece no lvies4 e o comecando lives3"

## Confirmado (visto nesta sessão, até 18/11 05:30)
- Kit v1.2.4 publicado: commit 38596f3 em inematds/ia-sem-estrago; guia PT/EN/ES respondendo 200.
- Vídeo A: `/home/nmaldaner/projetos/output/fora-do-volante-20261117/entrega/fora-do-volante-20261117.mp4` (3:02, −14,1 LUFS, pico −1,3; primeiro quadro vazio cortado).
- Vídeo B: `/home/nmaldaner/projetos/output/fora-do-volante-inicio-20261117/entrega/fora-do-volante-inicio-20261117.mp4` (2:08, −14,2 LUFS, pico −1,1).
- Fila do x3, só YouTube, status "aguardando" às 05:30:
  - A: item 3560, entrega 3562, lives4.
  - B: item 3561, entrega 3563, lives3.
- O serviço `yt-pub-x3` está ativo com X3_PUBLICAR=1.
- Descrições apontam para https://inematds.github.io/ia-sem-estrago/guia/ (original em `yt.txt.orig`, ao lado de cada `yt.txt` em `/home/nmaldaner/projetos/explicavideos/textos/`).

## Não verificado
- Se os vídeos já saíram. 11:00 (A) e 16:20 (B) são estimativa minha pela ordem da fila e pelos horários dos canais.
- O vigia em segundo plano (bctjyztid) foi interrompido quando a sessão parou: nada mais está esperando os links.
- Não ouvi o áudio. A transcrição automática traz "Cloud Code" e "Antropic"; a legenda gravada não traz (vem do roteiro).
- "x3 nunca publicou em canal real" veio do README dele; eu disse isso ao Nei sem conferir o histórico do banco.

## Correção do que eu disse ao Nei
Na última mensagem chamei 3562 e 3563 de "item". São os números das ENTREGAS; os itens são 3560 e 3561.

## Decisões minhas, sem o Nei ter pedido
- Só YouTube (`destinos: ["youtube"]`), embora os canais tenham TikTok e Instagram ligados. Ele foi avisado.
- Títulos mantidos com "Fora do volante"; a descrição explica que é o nome antigo.
- Duas frases novas na tela do A (cenas 2 e 9), em `/home/nmaldaner/projetos/output/explica-8Pg6G5h05hk/visual/gerar_visual.py`.

## Próxima ação exata
1. Ler `/home/nmaldaner/projetos/output/fora-do-volante-fase2/CONTINUAR.md` (bloco ESTADO no topo).
2. Em `/home/nmaldaner/projetos/yt-pub-x3`, consultar status e url das entregas 3562 e 3563 na tabela `entregas` (`from lib import db`). NÃO reenfileirar.
3. Com os links, seguir os passos 5 a 9 do bilhete: guia nos 3 idiomas e READMEs (bump de patch), portal (`atualiza-portal`, quadro de vídeos), uma mensagem no tópico 7484 do INEMA.CCODE, `PRODUCOES-VIDEO.md`, avisos e `CONTINUAR.resultado`.

## Pendente e não pedido agora
- rtex do lives8: `/home/nmaldaner/projetos/rtex/edicoes/2026-11-17-fora-do-volante-v2` sem avatar; o Nei não falou dele nesta rodada.
- Pergunta sem resposta: postar a atualização v1.2.4 no tópico do INEMA.CCODE. A abertura "A IA não estraga nada que não tenha volta" perdeu efeito para A e B, que saem com a narração antiga.
- Revisor independente do guia v1.2.4 não rodou.
- Sem `socat` nesta máquina, o sandbox do kit fica desligado.
- O quadro 0 vazio do A ainda não foi registrado em `FALHAS.md`/`LICOES.md` do refazvideo.

## Não fazer
Não reenfileirar nem republicar; não excluir nada no Telegram sem aprovação individual; não consultar o Vercel; não reenviar avatar ao HeyGen.


<!-- handoff-estado:inicio -->
## Estado gravado pelo script (não editar)

Gravado por handoff-grava.py no momento do handoff. `--conferir` compara com o projeto agora.

- commit: fefcb32898af53e89498e51f14ac38ee6a48df43 · branch: main
- arquivos sujos fora de handoffs/: 0
- `FALHAS.md` · sha256:42b709a6d74f · citado

### Repo do trabalho: /home/nmaldaner/projetos/ia-sem-estrago
- commit: 38596f391145639ff17f33faedeb203ca3cfd354 · branch: main
- arquivos sujos: 0
- impressão de todos os sujos: e3b0c44298fc1c14
<!-- handoff-estado:fim -->
