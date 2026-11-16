# EngineBridge

[![EngineBridge](guia/assets/banner.jpg)](https://inematds.github.io/enginebridge/guia/)

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

## O que é

Sua automação pode parar quando uma assinatura atinge a cota, mesmo tendo outra disponível. O EngineBridge é uma ferramenta local para escolher qual motor de IA atende cada etapa e usar uma alternativa declarada quando isso for permitido. Serve para quem mantém bots, scripts e rotinas com Claude Code e Codex. Você define perfis, modelos e esforço; o programa resolve a escolha sem consultar uma IA. Para executar textos, precisa de Python e dos programas autenticados pela assinatura.

**Versão 1.0.0 — núcleo local funcional; integração com os sistemas reais ainda pendente.**

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

Instale Claude Code e Codex, autentique pela assinatura no terminal e ajuste `binario` no YAML. Nunca use uma chave de API. O campo opcional `conta_env` aponta para um arquivo de dados com `CODEX_HOME=/caminho/da/conta`; sem esse arquivo, vale a conta padrão do Codex.

```bash
codex login
claude auth login
mkdir -p ~/.config/inema
test -f ~/.config/inema/modelos.env || cp config/modelos.example.env ~/.config/inema/modelos.env
```

O exemplo de modelos só é copiado se não existir configuração central. A etapa `demonstracao/padrao` herda o motor global e permite observar a troca com `prefer`; roteiro e crítica continuam com perfis fixados.

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
