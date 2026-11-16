# Adaptação dos crons — 15/11/2026

Nei autorizou adaptar todos os crons que usam IA. Preservar horários, filas, validações e estados desabilitados. Rotinas determinísticas não precisam ganhar IA. APIs de modelos ficam desativadas fora do escopo explicitamente autorizado do gitbombando. Tradução continua no inema-traduz.

| Grupo | Estado | Evidência |
|---|---|---|
| aventurasinemavideo | adaptado e ativo | produção e classificação configuráveis; Codex gpt-6.1-sol/medium assinatura; cinco contratos, agente real com escrita/releitura e classificação visual real passaram; #209 retomado às 21h29 de 15/11; fila yt-pubx preservada |
| portal: atualização automática | tradutor central preservado; sem configuração própria nova | gera-novidades e sync-agente-catalogo não usam LLM; traduz-feeds chama inema-traduz, hoje Codex/gpt-6-luna pela assinatura; reservas antigas de API não foram ativadas |
| gitbombando | concluído | configuração por etapa, testes reais Anthropic/Codex e publicação |
| eventosextremospub | adaptado | commit 436cdd9; 13 etapas; 5 testes; agente e MCP reais isolados; sem produção completa nova |
| r7ex/rtex/rtexjp | adaptados | 18 contratos + 45 conferências de produção; 3 revisões visuais reais; commits finais e6eabfb, 8acce30, 762cfca |
| cinco virais | adaptados | 30 testes de contrato; 5 roteiros reais aprovados pelos checar.py; commits finais 68bbaa6/b0302d2/a2be6f4/1dedbe2/80dc69c |
| Metricool e verdade-das-redes | adaptados e verificados | Metritds Codex autenticado; pub2 mantém Claude e depende reset da cota semanal em 16/11 21h |
| 19 schedulers YouTube ativos | adaptados e verificados | configuração exclusiva por canal; análise real Codex passou; imagem fixa Codex; sem reiniciar jobs ativos |
| rotinas noturnas com IA | integradas; testes finais | resumos, wiki e notícias; News PT e tradução central EN/ES reais passaram; build passou |
| continua/vigias/radar | adaptados e verificados | seleção/produção/retomada/ficha/visual configuráveis; nove testes Radar passaram |
| minha-escada/Hindsight | adaptados e verificados | Minha Escada preserva kit; Hindsight usa adaptador nativo da assinatura com etapas independentes |

Inventário: CRONS-2026-11-15.md. A conferência de canais yt-pubx indica configuração local ok, não comprova publicação nova.

## Evidências observadas

- Aventura: incluído após conferir serviços contínuos, fora do inventário original de timers. auto/ia.yaml separa produção/classificação; imagens continuam Codex. Falhas do motor preservam a matéria para retomar. Serviço reiniciado em pausa; última matéria comprovadamente barrada pela cota Claude foi restaurada a em_producao, com backup privado, e iniciou no Codex às 21h29. O Codex avaliou a primeira matéria e a descartou por ser boletim administrativo, conforme a regra editorial; o laço iniciou a próxima às 21h30. Vídeo novo ainda não concluído nessa conferência.

- 43 alvos de configuração válidos no comando ia-crons (incluem 19 canais YouTube e 24 sistemas/executores); não são 43 timers diferentes. Inventário original: 72 arquivos de timer do usuário, 64 carregados, 15 linhas de crontab, 19 schedulers YouTube ativos.
- r7ex/rtex/rtexjp: revisão visual real via Codex nas folhas de edições existentes, JSON aprovado; 45 verificações de produção existentes e 18 contratos IA passaram. Sem publicar no ensaio.
- Cinco virais: 30 testes de arquivos permitidos/saída inválida passaram; cinco roteiros reais pela assinatura Codex passaram no checar.py de cada área. Evidências em ~/projetos/output/crons-multiprovedor-2026-11-15/<sistema>/. Não geraram avatar/render/publicação.
- Clima: cinco contratos locais, agente real isolado com escrita/releitura e identidade real do MCP. A rodada mundo de 18h executou roteiro_mundo com Codex gpt-6.1-sol/medium (166,47 s); o portão editorial não confirmou 5–7 eventos e avisou o v3 (msg 4920), sem vídeo/publicação. Isso não foi falha de transporte do modelo.
- Métricas: 67 linhas de FTD recebidas, contagem validada e primeira linha conhecida preservada exatamente (data numérica e texto); somente leitura.
- YouTube: análise de cortes real com JSON válido; imagem real pela assinatura Codex em yt-imagem/codex.png. Os 19 schedulers continuam ativos, adotando scripts filhos na próxima execução; nenhum corte/upload foi encerrado para reiniciar.
- yt-pubx: dry-run real com metadados pelo Codex e arte pronta; thumb conferida visualmente e plano gravado, sem enviar nada ao YouTube. Configuração ativa fora do repo, em ~/.config/yt-pubx/ia.yaml.
- News: criação PT e tradução central EN/ES reais, estrutura conferida; seis testes e build Next passaram.
- Resumo Telegram e Cérebro VIP: respostas reais pelo gpt-6-luna/low; cache do resumo preservado. Isolamento dos módulos conferido ao carregar os dois no mesmo processo.
- Continua: uma sessão Codex escreveu/releu CONTINUAR.resultado em pasta isolada, sem bot ou publicação. Radar: nove testes existentes passaram. Minha escada: relatório e missões reais com entrada sintética, sem mexer no painel do usuário.
- Hindsight: cinco configurações nativas por fase, ambiente isolado/chaves removidas; carga simulada e reflect real pela assinatura Codex. Banco e vetores locais preservados.

## Limite externo conhecido

Metricool pub2 foi integrado e mantém a conta correta inemafuturostds@gmail.com no Claude assinatura. O teste real parou no limite semanal do Claude (login válido; reset informado para 16/11/2026, 21h America/Sao_Paulo). Não houve chamada de publicação nem uso de API paga. Pode voltar pela assinatura após a liberação ou exigir autenticação própria do conector pub2 no Codex; o OAuth da conta inematds não substitui essa conta.

## Rotinas preservadas sem novo motor

Backups, limpeza, watchdogs, git gc, índices, medidores de logs, coletores de ocorrências (loop-r/jardineiro), monitor de pagamentos e notificações não chamam LLM. Não receberam IA. Sincronizadores de catálogos e índices preservados. Embeddings de inemapro-mono/projetos usam Ollama local e mantêm o contrato vetorial; não são etapas de raciocínio. Inemaseo é coleta/relatório Search Console sem LLM. Filas de cidades, espanhol, lives7 e Radar Viral recebem o motor do publicador yt-pubx e/ou Metricool compartilhado. Traduções continuam no inema-traduz; timers desabilitados e schedulers inativos não foram ativados.

## Pendências anteriores recuperadas

As cinco pendências do Gitbombando foram concluídas. O avatar semanal chegou e o trabalhador terminou em 15/11: vídeo de 154 s aprovado, publicado no YouTube lives4 e enviado ao Telegram. Link: https://www.youtube.com/shorts/ppmMYIpofAQ . Instagram/TikTok inema.tds agendados para 18h42 de 15/11, respeitando o diário das 16h42, o vídeo de 13/11 às 17h42 e a trava por marca. Recibo Metricool: 2865392736350128769. Não há mais retomada de avatar pendente nesse lote.
