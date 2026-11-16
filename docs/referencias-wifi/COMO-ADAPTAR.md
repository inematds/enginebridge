# Como adaptar outro sistema

## 1. Ler as regras e mapear o fluxo

Leia AGENTS.md/CLAUDE.md, contexto, tarefas e documentação do projeto. Identifique o agendamento, o ponto de entrada e todas as chamadas de IA, inclusive as indiretas em scripts compartilhados.

Monte uma lista com etapa, entrada, saída, validador, efeitos externos, ferramentas necessárias e motor atual. No gitbombando, o filtro de tema e a consulta de agenda do Metricool estavam fora das chamadas mais visíveis do roteiro/revisor; também precisaram entrar no mapa.

Buscas úteis dentro do projeto, excluindo dependências e dados volumosos:

```bash
rg -n 'claude|codex|ANTHROPIC|OPENAI|openrouter|reasoning_effort|effortLevel' auto src scripts
```

Ajuste os diretórios ao projeto. Não exiba `.env`, tokens ou corpos de requisições autenticadas.

## 2. Definir o contrato de cada etapa

O sistema deve continuar recebendo o mesmo resultado, independentemente do provedor. Para cada etapa, defina os arquivos/dados enviados, imagens quando necessárias, formato retornado e critérios de aprovação.

No roteiro do gitbombando, o contrato é YAML com campos conhecidos. O script salva a resposta e executa `gb.py checar`. Se o resultado não passa, envia os erros e a resposta anterior ao modelo, com limite de duas tentativas. A API não precisa executar shell para isso.

Para revisores, o contrato é JSON com veredito e motivo. O script fornece as imagens e os dados de comparação. Não basta enviar o caminho local de uma imagem para uma API: o adaptador precisa anexar seus bytes em formato aceito pelo provedor.

Separe validação de negócio de transporte. O adaptador verifica resposta completa e extrai texto; o validador do sistema confere números, campos, ordem, tamanhos e regras próprias.

## 3. Criar configuração própria por etapa

Use [configuracao.exemplo.yaml](configuracao.exemplo.yaml) como referência. Nesse exemplo, os nomes de etapas continuam os do gitbombando para permitir validação pelo executor existente. Em outro sistema, renomeie as etapas e adapte a lista aceita pelo executor.

Mantenha os exemplos com `#` no próprio YAML. Declare tipos, motores, modelos e esforços explicitamente. Evite aliases móveis como `opus` na configuração final. Valide compatibilidade antes de executar: revisão exige visão; geração de imagem exige ferramenta própria; publicação exige um mecanismo autorizado de integração.

Se partir do código do gitbombando, ajuste pelo menos:

- `RAIZ`, `CONFIG`, nomes de etapas em `ETAPAS` e pontos de chamada.
- Restrições em `validar`, especialmente as específicas de capa e Metricool.
- Caminhos dos CLIs, sistema operacional, logins e conectores da máquina de destino.
- Nomes dos campos e contratos dos arquivos, validadores e limites de tentativas.
- Diretório dos registros e regras de publicação, retomada e prevenção de duplicação.

Esses ajustes acontecem na adaptação inicial. Trocar uma combinação já suportada depois deve exigir somente edição da configuração.

## 4. Colocar um executor entre o sistema e os motores

A interface usada como referência é:

```python
# Exemplo de integração, depois de instalar/adaptar o executor no projeto de destino.
from auto.ia import executar

resposta = executar(
    "roteiro",
    pedido,
    pasta_da_edicao,
    arquivos=[dados_json],
    imagens=[],
)
# O sistema salva a resposta, valida e decide a próxima etapa.
```

O executor carrega a configuração, escolhe o adaptador e devolve texto. Deve registrar etapa, tipo, motor, modelo, esforço, resultado e duração. Quando o provedor devolver uso ou modelo efetivo, registre esses dados separadamente do valor solicitado.

O cron chama os scripts do sistema. Evite colocar escolha de provedor, prompt, chave ou preço diretamente no agendamento.

## 5. Traduzir cada protocolo no adaptador

| Motor | Modelo e esforço | Entrada/saída na referência |
|---|---|---|
| Claude assinatura | `--model`, `--effort`, settings explícitos | Entrada por stdin; extrai `result` do JSON do CLI |
| Codex assinatura | `-m`, `-c model_reasoning_effort=...` | Entrada por stdin; imagens com `-i`; resposta final pelo arquivo de `-o` |
| Anthropic API | `model`, `output_config.effort` | Messages API, textos e imagens base64; exige `stop_reason: end_turn` |
| OpenAI API | `model`, `reasoning.effort` | Responses API, texto/imagem; exige `status: completed` |
| OpenRouter API | Slug completo, `reasoning.effort` | Chat Completions, texto/imagem; exige `finish_reason: stop` |

No OpenRouter da referência, `require_parameters` é true e `allow_fallbacks` é false. Isso evita omitir parâmetros incompatíveis ou acionar fallback de provedor silenciosamente. Não há fallback automático de assinatura para API paga.

Os níveis aceitos dependem do modelo. O exemplo usa low/medium; isso não garante que todo modelo aceite todos os níveis declarados no adaptador. Confirme a documentação vigente antes de mudar o protocolo, sem consultar APIs de catálogo sem autorização.

Na assinatura, remova do ambiente as chaves e seletores herdados que poderiam mudar autenticação/modelo/esforço. Preserve o login necessário, passe os valores escolhidos por argumentos e use o binário correto. No servidor INEMA há CLIs antigos em `/usr/bin`; a referência usa os caminhos atuais em `~/.local/bin` e `~/.npm-global/bin`.

## 6. Separar credenciais e autorização

O YAML contém o **nome** da chave e o caminho do arquivo, nunca o valor. O leitor do `.env` trata o conteúdo como dados: não usa `source`, não executa shell e aceita nomes com hífen, como inemapro-api-key.

Na referência, `api.autorizada/autorizacao` vale somente para Anthropic; OpenAI e OpenRouter têm seus próprios blocos. A lista `etapas_autorizadas` restringe o uso às etapas aprovadas. A execução recusa serviço/etapa não autorizado antes de ler a chave ou abrir conexão.

Ao adaptar outro sistema, inicie com todas as APIs desativadas. Permissão de teste não vira automaticamente permissão de operação diária. Não copie a autorização do gitbombando para outro sistema. Use as regras permanentes do usuário e registre uma autorização nova quando o serviço/finalidade não estiverem cobertos.

## 7. Tratar ferramentas como capacidade separada

Uma API de modelo pode produzir uma chamada de ferramenta; isso não executa o conector na máquina. Alguém precisa fornecer a ferramenta, executar a operação autorizada, devolver o resultado ao modelo e controlar o ciclo.

No gitbombando, o adaptador de API implementa somente texto/visão. O Metricool usa agora Codex por assinatura/MCP; Claude também pode ser selecionado. Para levá-lo à API seria necessário implementar uma ponte para o MCP ou um cliente direto do Metricool, respeitando suas autorizações, credenciais e a trava de intervalo. Isso não está implementado nesta referência. Outra alternativa é usar a assinatura do Codex com MCP, desde que o conector e a conta estejam disponíveis. Em 15/11/2026, o conector separado metricool-inematds foi autenticado no Codex e confirmou a conta e a leitura de agenda. A integração foi concluída na v1.7.0 e a publicação real foi testada. Na v1.7.1, uma trava por marca passou a envolver consulta, criação e recibo para impedir que retomadas paralelas escolhessem o mesmo horário.

A imagem continua em Codex/image_gen pela assinatura. Trocar o modelo do agente Codex não troca automaticamente o gerador de imagem.

Portanto, declare capacidades por etapa. Rejeite combinações incompatíveis, em vez de assumir que texto, imagem, shell e conectores existem em todos os provedores.

## 8. Manter os mecanismos de operação

Preserve as travas, horários, arquivos de etapa concluída, validadores e retomada já existentes no projeto. Não republique uma edição só para testar outro motor. Coloque limites explícitos de duração, saída e tentativas.

`max_tokens` limita saída/raciocínio conforme o provedor; não é teto em dólares. O executor de referência não implementa orçamento monetário por rodada. Para adicioná-lo, será necessário definir preços confiáveis, contabilização e política de interrupção; não apresentar um limite de tokens como orçamento financeiro.

Alterações no YAML precisam ser atômicas, com trava durante gravação e preservação dos comentários. A referência usa os índices dos nós do parser YAML para trocar apenas os escalares; reserializar o arquivo inteiro com safe_dump apagava os comentários.

## 9. Verificar e ativar

Primeiro teste sem rede: seleção por etapa, independência de defaults globais, comentários preservados, credenciais isoladas, bloqueio antes da conexão, respostas incompletas e regressão dos validadores existentes.

Depois faça um teste real pequeno em pasta isolada, usando dados iguais nos motores comparados. Para API, use somente a autorização expressa válida. Não gere avatar, publique ou altere o agendamento para provar uma simples troca de motor.

Registre o que passou e seu alcance. Testar um roteiro não prova revisão visual nem conector. Só ative a operação diária depois de autorização nesse escopo. Atualize documentação, versões e changelog conforme as regras do projeto; faça commit apenas dos arquivos da adaptação.

## Aprendizados adicionais da publicação real

Consultar a agenda e só depois criar, sem trava entre essas operações, permite corrida: dois processos veem o mesmo horário livre. Use um lock por conta/marca durante toda a sequência consulta → criação → recibo, e confira o recibo novamente dentro da trava. Marcas diferentes continuam independentes. O gitbombando faz isso em auto/metricool_lock.py e no shell de publicação do vídeo.

Verifique também a ingestão da mídia: o conector aceitou imagens, mas teve timeout ao baixar MP4 de 31 MB. Uma cópia social 720p de 11 MB, com faststart e URL CDN resolvida, funcionou, sem alterar o master aprovado. Isso é uma limitação do caminho de distribuição, não do modelo de texto. A referência está em auto/resolver_midia.py e auto/metritds.sh.

Se precisar mover um post já criado, atualize o mesmo ID. No Metricool, o leitor pode devolver networkData vazio de redes que não pertencem a providers; reenviar esses campos causa erro. Mantenha somente as redes ativas e preserve seu conteúdo. Não apagar/recriar para contornar isso sem autorização individual de exclusão.

## Exemplos adicionais validados em 15/11/2026

- Cinco virais: o modelo retorna um JSON com arquivos permitidos; o executor valida toda a resposta antes de gravar, e o checar.py original valida os fatos. O transporte não executa ferramentas. Implementação-base: ferramentas/roteiro_arquivos.py.
- Clima e continuação: etapas que geram código/render precisam de agente Claude/Codex pela assinatura. APIs de texto são recusadas para esse contrato.
- Hindsight: aproveitar o adaptador nativo de assinatura openai-codex/claude-code em vez de criar uma API intermediária. O launcher traduz cada etapa do YAML para a configuração nativa; vetores e banco ficam preservados.
- Schedulers: migrar o script filho permite aplicar a configuração na próxima execução, sem encerrar cortes/uploads ativos. Cada canal mantém ia.yaml próprio; o sync copia só código e inicializa configuração ausente a partir de exemplo sem APIs liberadas.
- Aplicação que carrega vários projetos num único processo Python: importar o executor por caminho absoluto e nome de módulo exclusivo. Trocar apenas sys.path pode reutilizar o módulo ia_motor já carregado de outro projeto. Isso foi corrigido e testado conjuntamente no resumo Telegram e no Cérebro VIP.

A lista de alvos e exceções externas está em ADAPTACAO-TODOS.md; o comando ia-crons é o ponto de controle local.
