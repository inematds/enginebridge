# EngineBridge

[![EngineBridge](guia/assets/banner.jpg)](https://inematds.github.io/enginebridge/guia/)

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

## O que é

Sua automação pode parar quando uma assinatura atinge a cota, mesmo tendo outra disponível. O EngineBridge é uma ferramenta local para escolher qual motor de IA atende cada etapa e usar uma alternativa declarada quando isso for permitido. Serve para quem mantém bots, scripts e rotinas com Claude Code e Codex. Você define perfis, modelos e esforço; o programa resolve a escolha sem consultar uma IA. Para executar textos, precisa de Python e dos programas autenticados pela assinatura.

**Versão 1.2.1 — núcleo local funcional; integração com os sistemas reais ainda pendente.**

[Guia completo](https://inematds.github.io/enginebridge/guia/) · [Arquitetura](docs/ARQUITETURA.md) · [Plano de adoção](docs/ADOCAO.md) · [Referências e revisão Astra](docs/REFERENCIAS.md)

## Instalar e verificar

```bash
git clone https://github.com/inematds/enginebridge.git
cd enginebridge
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
python3 -m enginebridge resolve --project demonstracao --stage roteiro
```

Requer Python 3.11+ e PyYAML 6. Os perfis de demonstração usam modelos explícitos e podem ser resolvidos sem login. Os níveis herdados usam `~/.config/inema/modelos.env`; em outra máquina, configure `modelos_env` e os caminhos dos executáveis no YAML. A resolução não verifica a existência do modelo na assinatura.

## Simular a troca sem consumir modelos

```bash
printf 'Crie um roteiro curto.' | python3 -m enginebridge --state .state/demo.sqlite run --project demonstracao --stage roteiro --simulate --fail-first
python3 -m enginebridge --state .state/demo.sqlite status
```

A simulação produz uma rejeição de cota no Codex, registra uma suspensão temporária no SQLite e entrega o mesmo pedido ao executor fictício Claude. O campo `simulado` diferencia essa saída de uma execução real. Não altera serviços, não consulta saldo e não chama modelos.

## Preparar contas em uma máquina nova

Instale Claude Code e Codex, autentique pela assinatura no terminal e ajuste `binario` no YAML. Nunca use uma chave de API. O campo opcional `conta_env` aponta para um arquivo de dados com a pasta da conta: `CODEX_HOME=/caminho` no Codex e `CLAUDE_CONFIG_DIR=/caminho` no Claude. Sem a variável, vale a pasta padrão de cada programa. A cota segue a conta: cada pasta ganha seu próprio pool (`claude-principal:claude-inematds`), e bloquear o pool base suspende todas as contas daquele motor.

```bash
codex login
claude auth login
mkdir -p ~/.config/inema
test -f ~/.config/inema/modelos.env || cp config/modelos.example.env ~/.config/inema/modelos.env
```

O exemplo de modelos só é copiado se não existir configuração central. A etapa `demonstracao/padrao` herda o motor global e permite observar a troca com `prefer`; roteiro e crítica continuam com perfis fixados.

## Duas contas do Claude: ter, manter e trocar

Cada assinatura do Claude Code fica numa pasta própria de login: a primeira na pasta padrão `~/.claude`, a segunda em `~/.claude-inematds`. As duas ficam logadas ao mesmo tempo e não se misturam. O `claude-conta` escolhe qual vale por padrão; no Codex, o mesmo papel é do `codex-conta`.

1. 🧠 Criar a pasta da segunda conta, com links para regras, ganchos, skills, agentes, plugins e memória: `claude-conta preparar inematds`.
2. 🧠 Logar pela assinatura nessa pasta, uma vez: `CLAUDE_CONFIG_DIR=~/.claude-inematds claude auth login --claudeai --email <e-mail>`. Se o navegador não abrir, copie o link impresso, autorize com a conta certa e cole o código no próprio terminal.
3. ⚙️ Conferir os logins e o uso de cada conta: `claude-conta` e `claude-conta uso`.
4. 🧠 Trocar o padrão: `claude-conta inematds` (ou `claude-conta nei` para voltar). Vale para terminais novos, timers, serviços que iniciarem depois e o EngineBridge; `--reinicia` também reinicia os serviços sempre ligados.
5. 🧠 Usar a outra conta numa sessão só, sem mudar o padrão: `CLAUDE_CONFIG_DIR=~/.claude-inematds claude`.
6. ⚙️ O EngineBridge lê a escolha pelo `conta_env` do motor claude, dá a cada conta seu próprio pool de cota (`claude-principal:claude-inematds`) e recusa trabalho resolvido na conta anterior ("Conta alterada").

A barra de status mostra `cc:` e `cx:` com a conta do Claude e do Codex de cada sessão. Sessões e serviços já abertos continuam na conta antiga até reiniciar. A conta da pasta padrão é usada sem a variável `CLAUDE_CONFIG_DIR`: com ela, o Claude leria outro arquivo de estado e perderia conectores. Conectores com login próprio (MCP) pedem login de novo na pasta nova.

### Login da segunda conta, uma vez só

O login é feito por você, no seu terminal, porque é a autorização da assinatura. Testado em 20/11/2026 numa máquina em que o navegador não abre sozinho:

1. Num terminal fora do Claude, com a janela larga para o link não quebrar, rode `CLAUDE_CONFIG_DIR=~/.claude-inematds claude auth login --claudeai --email <e-mail-da-conta>`.
2. O comando imprime um link `https://claude.ai/oauth/authorize?...` e fica esperando. Não feche nem aperte Enter.
3. Copie o link inteiro e abra em qualquer navegador. Use janela privada ou o celular se o navegador já estiver logado na outra conta, e confira que a página mostra a conta certa antes de clicar em Authorize.
4. A página mostra um código. Cole o código inteiro, inclusive a parte depois do `#`, no mesmo terminal que está esperando, e dê Enter. Colar no chat do Claude não funciona: o código só vale para aquele comando, uma vez, e expira em poucos minutos.
5. Confira com `claude-conta`: a pasta nova deve mostrar o e-mail da segunda conta. Se aparecer "(sem login)", repita a partir do passo 1 e use o código novo.

### Trocar de conta com sessões abertas (cota acabou no meio)

Uma sessão aberta não troca de conta sozinha. Feche e reabra cada uma na conta nova; a conversa continua, porque as duas contas usam a mesma pasta de conversas (`~/.claude-inematds/projects` é link para `~/.claude/projects`). Testado em 21/11/2026, com a inematds no limite de 5 h:

1. 🧠 Escolher a conta: `claude-conta nei` (ou `claude-conta inematds`). Conferir a folga antes com `claude-conta uso`.
2. ⚙️ Ver quais sessões estão abertas, em qual terminal e conta, e quais foram fechadas: `claude-conta sessoes` (ou `claude-conta sessoes ~/projetos/<pasta>`). Mostra o id e o último pedido de cada uma; `← esta` marca a sessão de onde o comando foi chamado.
3. 🧠 Em cada terminal: sair com `/exit` e, na mesma pasta, rodar `unset CLAUDE_CONFIG_DIR CLAUDE_CONTA_AUTO` (só se o terminal estava na outra conta) e `claude --resume <id>`.
4. 🧠 Conferir na barra de status: `cc:nei` (ou `cc:inematds`).

Não use `claude --continue` quando houver mais de uma sessão na mesma pasta: ele abre a conversa mais recente da pasta, que pode ser outra. Com o id, o `--resume` abre a certa; sem o id, mostra a lista para escolher.

**Pendente:** o cron e outros chamadores diretos do `claude` ainda não seguem a escolha. Próximo passo: todos lerem a conta ativa, e depois o EngineBridge passar a ter conta ativa e contas secundárias, usando a secundária quando a ativa bater na cota.

## Preferência global e exceções

```bash
python3 -m enginebridge prefer claude
python3 -m enginebridge resolve --project demonstracao --stage padrao
python3 -m enginebridge prefer codex
python3 -m enginebridge resolve --project demonstracao --stage padrao
```

`prefer` modifica apenas este YAML e preserva comentários. Etapas com `perfil` ou `motor` explícito permanecem fixadas; a troca global afeta as etapas sem essa escolha. Modelo e esforço herdados continuam na fonte central existente. Esforço não mede equivalência de qualidade entre famílias de modelos.

```bash
python3 -m enginebridge --state .state/demo.sqlite block --pool codex-principal
python3 -m enginebridge --state .state/demo.sqlite unblock --pool codex-principal
```

Suspender uma conta impede novas admissões no EngineBridge, inclusive em trabalhos já resolvidos. Retirar o bloqueio manual preserva eventual suspensão temporária por cota. O estado padrão fica em `~/.local/state/enginebridge/state.sqlite`; todos os consumidores da mesma máquina devem compartilhar esse caminho e a configuração. Não coloque esse SQLite em rede.

## Executar um texto pela assinatura

```bash
printf 'Responda com uma frase sobre perfis por etapa.' | python3 -m enginebridge run --project demonstracao --stage roteiro
```

Este comando consome a assinatura escolhida. Usa Claude Code ou Codex em diretório temporário, sem MCP pessoal, sem shell habilitado e sem sessão nativa compartilhada. As credenciais de API são removidas do ambiente. Não executa workflows de agente, publicação, imagens ou tradução. Os binários precisam aceitar os argumentos documentados pelo adaptador; os testes locais usam executáveis fictícios, sem comprovar login ou funcionamento real de ambos os CLIs.

## Contrato de continuidade

- Seleção por chamada, etapa, projeto e preferência global, sempre sujeita às permissões e às etapas fixadas.
- Alternativa explícita em etapas fixadas; em etapas livres, alternativas do projeto ou globais.
- Cota compartilhada por conta (`quota_pool`), independente do nome do modelo; uma execução simultânea por pool neste núcleo.
- Rejeição estruturada de cota, sem resposta parcial nem ferramentas, permite tentar a alternativa e persistir a suspensão temporária.
- Erro local, timeout, mensagem de erro apenas em prosa ou resultado recusado pelo validador interrompem o trabalho, sem repetição automática.
- Cada trabalho guarda uma cópia resolvida dos modelos; bloqueios urgentes e mudança da conta são conferidos antes de cada tentativa.

Há exemplos de consumo Python e CLI em `examples/`. Não há integração ativada com OpenPCBotV3, Refazvideo ou crons. OpenRouter aparece desabilitado como extensão futura; não existe adaptador de API nesta versão, mesmo que alguém altere `habilitado` no YAML.

## Desenvolvimento

```bash
python3 -m compileall -q enginebridge examples tests
python3 -m unittest discover -s tests -v
python3 -m enginebridge --version
```

[Licença MIT](LICENSE). O desenho reaproveita as referências de provedores independentes do WiFi e a crítica do Astra, preservadas em `docs/`.
