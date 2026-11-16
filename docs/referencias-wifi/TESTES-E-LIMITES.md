# Testes e limites observados

## Testes reais de 15 de novembro de 2026

Os dois motores receberam os mesmos dados do Top 10 de 14/11 e o pedido de roteiro do gitbombando. Cada execução ficou em uma pasta isolada. O programa recebeu YAML, salvou a ficha e executou o portão real `python3 gb.py checar <pasta>`. Ambos passaram na primeira tentativa.

| Execução | Modelo e esforço | Resultado | Tempo total observado |
|---|---|---|---|
| API Anthropic | claude-opus-5-5, low | 13 partes e 2.275 caracteres de fala, aprovado | 37,87 s |
| Assinatura Codex | gpt-6.1-sol, medium | 13 partes e 1.945 caracteres de fala, aprovado | 42,15 s |

A Anthropic retornou o ID claude-opus-5-5 e uso medido de 22.138 tokens de entrada e 4.649 de saída, dos quais 1.643 de raciocínio. Não foi calculado custo em dinheiro nesta referência. O teste Codex usou a assinatura, sem chave de API.

Evidências locais:

- `~/projetos/gitbombando/tests/resultados/2026-11-15.json`.
- `~/projetos/output/gitbombando-testes-ia-2026-11-15/anthropic/`.
- `~/projetos/output/gitbombando-testes-ia-2026-11-15/codex/`.

Os testes reais cobrem geração e validação de roteiro. Não geraram imagem, avatar ou vídeo e não publicaram nada. Revisão visual e publicação por API não foram demonstradas por esses testes. OpenAI/OpenRouter tiveram apenas testes simulados, sem chamadas reais.

## Testes automáticos

Na implementação de referência:

```bash
cd ~/projetos/gitbombando
python3 -m unittest discover -s tests -v
./ia validar
bash -n ia auto/rodar.sh auto/carrossel.sh auto/metritds.sh
```

Os testes sem rede começaram com 18 casos; na v1.7.1 são 23, incluindo isolamento do MCP, trava concorrente e bloqueio de IAs na fala. Eles verificam:

- Valores explícitos de modelo/esforço, independentemente dos defaults do ambiente.
- Alteração de uma etapa sem mudar as outras.
- Preservação dos comentários `#`, inclusive inline, e recusa de configuração inválida.
- Claude/Codex por assinatura sem chaves de API herdadas.
- Bloqueio de API antes de carregar credencial/conectar à rede.
- Autorização Anthropic sem liberação de OpenAI/OpenRouter.
- Restrição por etapa e leitura de chave com nome contendo hífen.
- Protocolos de texto/visão e esforço de Anthropic, OpenAI e OpenRouter com respostas simuladas.
- Recusa de respostas incompletas e ausência de fallback pago.
- Correção pelo portão real de roteiro, contratos do carrossel e intervalo de publicação.

O script manual `tests/teste_motores_reais.py` faz chamadas reais. Não faz parte do comando unittest e não deve ser executado com API sem autorização explícita vigente. Ele usa uma pasta nova e restringe o teste Anthropic à etapa roteiro.

## Metricool e o limite da assinatura

**O Metricool ainda não funciona pela API do Claude neste executor.** A consulta de agenda e o agendamento usam agora o conector MCP no Codex por assinatura; Claude também é suportado. A API Anthropic implementada recebe texto/imagens, sem ponte para esse conector.

Uma chamada mínima ao Claude por assinatura encontrou limite semanal em 15/11/2026. A integração posterior removeu essa dependência do Metricool: as etapas passaram à assinatura Codex e publicaram de verdade após confirmar a conta e a agenda. Isso não significa que a API Anthropic ganhou ferramentas MCP; o adaptador de API continua somente texto/visão.

## Outros limites

| Limite | Consequência para outro sistema |
|---|---|
| Lista de oito etapas e caminhos próprios do gitbombando | Adaptar uma vez na implementação inicial; não copiar e anunciar como biblioteca universal |
| Visão depende do modelo escolhido | Texto aprovado não comprova revisão de imagem |
| Imagem da capa usa ferramenta image_gen do Codex | Modelo de texto/API não substitui o gerador |
| Autorização tem serviço, finalidade e etapas | Reutilizar código não transfere autorização de consumo |
| Modelos/acesso podem diferir entre assinatura e API | Exemplo de ID não garante disponibilidade pela chave |
| Configuração local não consulta catálogo/saldo | Validar YAML não comprova autenticação ou crédito |
| Timeout/max_tokens não são teto financeiro | Documentar orçamento separadamente, se existir |
| Logs não registram segredos, prompt ou resposta completa | Guardar artefatos de teste adequados, sem exigir que o log de uso substitua toda a evidência |
| Chamada em andamento já carregou sua configuração | Alterações valem para chamadas seguintes, podendo haver modelos diferentes na mesma edição se o YAML mudar no meio |

## Critério para declarar outro sistema adaptado

A configuração deve selecionar cada etapa sem edição posterior de código, preservar comentários e recusar combinações incompatíveis. Os validadores existentes precisam continuar passando, as permissões e credenciais precisam ficar isoladas, e os efeitos externos precisam continuar protegidos contra repetição.

Um teste real autorizado deve provar pelo menos uma tarefa concreta em cada motor que se deseja colocar em operação. Registre separadamente o que recebeu apenas teste simulado. Não declarar o sistema inteiro independente de um provedor enquanto uma etapa obrigatória, como um conector, ainda depende dele.

## Tentativa de Metricool pelo Codex

Teste real somente de leitura em 15/11/2026, gpt-6.1-sol/medium: o CLI concluiu em 11,15 s, mas o modelo retornou sem_ferramentas porque o MCP não autenticou. O transporte registrou AuthRequired; a listagem do CLI confirmou metricool habilitado e not_logged_in. A conta inematds e a agenda não foram validadas. Não houve operação de escrita. Ver [procedimento OAuth](AUTENTICAR-METRICOOL-NO-CODEX.md).

## Metricool autenticado no Codex e validado

Após o usuário concluir OAuth, o perfil ~/.codex-2 passou a listar metricool-inematds com auth_status o_auth. O teste real gpt-6.1-sol/medium chamou getBrandSettings e getScheduledPosts pelo conector correto, conforme o log de execução.

Resultado: ownerUsername inematds@gmail.com confirmado; marcas inema.tds, eventosextremos, FTD, Radar e VIBE; agenda da inema.tds lida para 15/11/2026 00:00 a 17/11/2026 23:59:59, America/Sao_Paulo, com cinco agendamentos. Tempo observado: 33,73 s. Nenhuma publicação foi criada, editada ou apagada. Não houve mudança no cron.

Evidência: [validacao-metricool-codex-autenticado-2026-11-15.json](validacao-metricool-codex-autenticado-2026-11-15.json). Esse teste inicial comprovou autenticação, conta, marcas e leitura de agenda. Na retomada posterior, a v1.7.1 integrou o executor e também fez publicações reais de carrosséis e vídeos pelo conector Codex.

## Publicação real na integração v1.7.1

O carrossel Top 10 de 15/11 foi aceito no Instagram/TikTok da marca FTD para 16h35, e o carrossel de 13/11 corrigido para seis projetos foi aceito para 17h35. Ambos foram publicados no Telegram. Os vídeos do dia e de 13/11 foram aceitos na inema.tds; uma corrida inicial escolheu 16h42 para ambos, corrigida antes da saída: dia às 16h42 e 13/11 às 17h42, no mesmo ID. A agenda foi relida e confirmou a correção. A trava por marca passou a cobrir a região inteira de consulta/criação/recibo.

Regras confirmadas pelo Nei: canais/marcas diferentes podem sair simultaneamente; o mesmo conteúdo pode ser enviado simultaneamente às redes Instagram e TikTok; manter 1 hora entre conteúdos diferentes da mesma marca. Não generalizar o intervalo para todas as marcas do sistema.
