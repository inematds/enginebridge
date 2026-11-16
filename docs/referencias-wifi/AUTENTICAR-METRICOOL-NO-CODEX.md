# Autenticar o Metricool no Codex

Na tentativa inicial de 15/11/2026, o Codex por assinatura respondeu ao teste, mas o MCP Metricool pediu OAuth (`AuthRequired`). O comando `codex mcp list --json` confirmou `auth_status: not_logged_in`. Nenhuma conta ou agenda foi consultada e nenhuma publicação foi alterada.

## Perfil e conta corretos

A sessão testada usa `CODEX_HOME=/home/nmaldaner/.codex-2`. Há também ~/.codex na máquina; autenticar um perfil não comprova o outro. Use o mesmo perfil dos processos que executarão o trabalho.

A conta necessária ao gitbombando é **inematds@gmail.com**, conector **metricool-inematds**. O conector chamado somente metricool é usado no Claude para inematime; não substituir seu login para tentar configurar inematds. No Codex, o teste encontrou somente o alias metricool, sem login.

A configuração do conector não é o login. O login da assinatura do Codex também não autentica automaticamente o Metricool.

## Fazer a conexão no terminal

Execute no terminal da máquina onde roda o Codex:

```bash
CODEX_HOME="$HOME/.codex-2" ~/.npm-global/bin/codex mcp add metricool-inematds --url https://ai.metricool.com/mcp
```

O comando de adicionar pode iniciar o login automaticamente. Se já concluir a autenticação, não precisa repetir o login. Caso contrário, execute:

```bash
CODEX_HOME="$HOME/.codex-2" ~/.npm-global/bin/codex mcp login metricool-inematds --no-browser
```

O modo `--no-browser` é útil no acesso remoto: imprime um link de autorização e recebe o endereço de retorno no terminal.

1. Mantenha o comando de login aberto e abra o link que ele mostrar no navegador.
2. Entre no Metricool como **inematds@gmail.com**, escolhendo essa conta se já houver outra sessão.
3. Confira a conta e autorize a conexão.
4. Se o navegador não conseguir abrir a página de retorno localhost/127.0.0.1, copie o endereço completo da barra e cole no terminal que aguarda o retorno. Esse fluxo é suportado pelo CLI; não precisa que o callback abra no computador do navegador.
5. Aguarde a confirmação de autenticação do CLI. O endereço de retorno contém código temporário: cole no terminal de login, não em documentação ou repositório.

Alternativa com abertura automática do navegador, quando o navegador e o callback estão acessíveis na mesma máquina:

```bash
CODEX_HOME="$HOME/.codex-2" ~/.npm-global/bin/codex mcp login metricool-inematds
```

Não é necessário chave de API do Metricool. O acesso usa OAuth do conector. Não copiar tokens do Claude para arquivos do Codex manualmente.

## Conferir e validar a conta

```bash
CODEX_HOME="$HOME/.codex-2" ~/.npm-global/bin/codex mcp list
```

O servidor metricool-inematds deve aparecer habilitado e autenticado. Essa listagem ainda não comprova a conta: abra uma nova execução do Codex e peça somente leitura:

```text
Use somente o MCP metricool-inematds, sem criar, editar, agendar ou apagar nada.
Leia getBrandSettings e confirme ownerUsername = inematds@gmail.com.
Confira as marcas inema.tds (7797870) e FTD (7908265).
Se a conta estiver correta, leia getScheduledPosts da inema.tds para os próximos
três dias, usando o schema real da ferramenta. Informe só a quantidade de posts.
Não use o conector metricool nem outra conta. Não exponha credenciais.
```

Critério de sucesso: ferramentas disponíveis, proprietário correto, marcas corretas e leitura real da agenda. Se o e-mail não vier na resposta, registre essa ausência; não afirme identidade só pelo nome da marca.

Depois do login, o executor de cada sistema precisa suportar o conector Codex e preservar a trava de intervalo. No gitbombando isso já foi implementado na v1.7.1, com publicação real autorizada pelo Nei. OAuth sozinho não muda o cron nem autoriza publicação de teste.

## Referências verificadas

- Ajuda local de `~/.npm-global/bin/codex mcp add --help` e `mcp login --help`, incluindo `--no-browser`.
- [MCP no Codex, documentação oficial](https://learn.chatgpt.com/docs/extend/mcp?surface=cli), seção de configuração pelo CLI e login OAuth.
- Conta e marcas: `~/projetos/metricool-inematds/README.md` e `docs/AUTENTICAR.md`.
- Resultado isolado: `~/projetos/output/gitbombando-testes-ia-2026-11-15/metricool-codex/resultado-modelo.json`; logs de diagnóstico ficam fora do git.

## Resultado da conexão feita em 15 de novembro de 2026

OAuth concluído no perfil ~/.codex-2, alias metricool-inematds. O callback já tinha encerrado seu listener quando foi reenviado, mas a listagem confirmou o_auth; a validação funcional posterior confirmou ownerUsername inematds@gmail.com, as cinco marcas e a leitura real de cinco agendamentos da inema.tds. O conector genérico metricool permanece separado, sem login.

A autenticação e a leitura pelo Codex estão validadas. Depois dessa validação, o cron foi integrado ao Codex/MCP na v1.7.1 e fez publicações reais autorizadas. Ver [resultado](validacao-metricool-codex-autenticado-2026-11-15.json). Códigos e URLs de callback não foram salvos nesta documentação.
