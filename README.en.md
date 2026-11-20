# EngineBridge

[![EngineBridge](guia/assets/banner-en.jpg)](https://inematds.github.io/enginebridge/guia/en/)

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

## What it is

Your automation can stop when a subscription reaches its quota, even if another one is available. EngineBridge is a local tool for choosing which AI engine handles each stage and using a declared alternative when allowed. It is for people who maintain bots, scripts, and routines with Claude Code and Codex. You define profiles, models, and effort; the program resolves the choice without consulting an AI. Running text requires Python and subscription-authenticated programs.

**Version 1.1.0 — functional local core; integration with real systems is still pending.**

[Complete guide](https://inematds.github.io/enginebridge/guia/en/) · [Architecture](docs/ARQUITETURA.md) (Portuguese) · [Adoption plan](docs/ADOCAO.md) (Portuguese) · [References and Astra review](docs/REFERENCIAS.md) (Portuguese)

## Install and verify

```bash
git clone https://github.com/inematds/enginebridge.git
cd enginebridge
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
python3 -m enginebridge resolve --project demonstracao --stage roteiro
```

Requires Python 3.11+ and PyYAML 6. The demonstration profiles use explicit models and can be resolved without signing in. Inherited levels use `~/.config/inema/modelos.env`; on another machine, configure `modelos_env` and the executable paths in the YAML. Resolution does not check whether the model is available in the subscription.

## Simulate a switch without consuming models

```bash
printf 'Create a short script.' | python3 -m enginebridge --state .state/demo.sqlite run --project demonstracao --stage roteiro --simulate --fail-first
python3 -m enginebridge --state .state/demo.sqlite status
```

The simulation produces a quota rejection in Codex, records a temporary suspension in SQLite, and delivers the same request to the mock Claude executor. The `simulado` field distinguishes this output from a real run. It does not modify services, check balances, or call models.

## Prepare accounts on a new machine

Install Claude Code and Codex, authenticate through your subscriptions in the terminal, and set `binario` in the YAML. Never use an API key. The optional `conta_env` field points to a data file with the account folder: `CODEX_HOME=/path` for Codex and `CLAUDE_CONFIG_DIR=/path` for Claude. Without the variable, each program uses its default folder. Quota follows the account: each folder gets its own pool (`claude-principal:claude-inematds`), and blocking the base pool suspends every account of that engine.

```bash
codex login
claude auth login
mkdir -p ~/.config/inema
test -f ~/.config/inema/modelos.env || cp config/modelos.example.env ~/.config/inema/modelos.env
```

The example models file is copied only if no central configuration exists. The `demonstracao/padrao` stage inherits the global engine and lets you observe the switch with `prefer`; roteiro and crítica remain tied to fixed profiles.

## Two Claude accounts: set up, maintain, and switch

Each Claude Code subscription uses its own login folder: the first in the default folder `~/.claude`, the second in `~/.claude-inematds`. Both stay logged in at the same time and remain separate. `claude-conta` chooses which one is used by default; in Codex, `codex-conta` serves the same purpose.

1. 🧠 Create the second account's folder, with links to rules, hooks, skills, agents, plugins, and memory: `claude-conta preparar inematds`.
2. 🧠 Sign in with your subscription in that folder, once: `CLAUDE_CONFIG_DIR=~/.claude-inematds claude auth login --claudeai --email <e-mail>`. If the browser does not open, copy the printed link, authorize with the right account, and paste the code into the terminal.
3. ⚙️ Check the logins and usage for each account: `claude-conta` and `claude-conta uso`.
4. 🧠 Switch the default: `claude-conta inematds` (or `claude-conta nei` to switch back). This applies to new terminals, timers, services started afterward, and EngineBridge; `--reinicia` also restarts services that are always running.
5. 🧠 Use the other account for just one session without changing the default: `CLAUDE_CONFIG_DIR=~/.claude-inematds claude`.
6. ⚙️ EngineBridge reads the selection from the claude engine's `conta_env`, gives each account its own quota pool (`claude-principal:claude-inematds`), and rejects work resolved under the previous account ("Conta alterada").

The status bar shows `cc:` and `cx:` with the Claude and Codex account for each session. Sessions and services that are already open stay on the old account until restarted. The account in the default folder is used without the `CLAUDE_CONFIG_DIR` variable: with it, Claude would read a different state file and lose its connectors. Connectors with their own login (MCP) require signing in again in the new folder.

### Second account login, one time only

You perform the login in your own terminal because this authorizes the subscription. Tested on 20/11/2026 on a machine where the browser does not open automatically:

1. In a terminal outside Claude, with the window wide enough that the link does not wrap, run `CLAUDE_CONFIG_DIR=~/.claude-inematds claude auth login --claudeai --email <e-mail-da-conta>`.
2. The command prints a `https://claude.ai/oauth/authorize?...` link and waits. Do not close it or press Enter.
3. Copy the entire link and open it in any browser. Use a private window or your phone if the browser is already logged into the other account, and check that the page shows the correct account before clicking Authorize.
4. The page shows a code. Paste the entire code, including the part after `#`, into the same terminal that is waiting, then press Enter. Pasting it into Claude chat will not work: the code is valid only for that command, once, and expires within a few minutes.
5. Check with `claude-conta`: the new folder should show the second account's email. If it shows "(sem login)", repeat from step 1 and use the new code.

**Pending:** cron jobs and other direct callers of `claude` do not follow the choice yet. Next step: have all of them read the active account, then let EngineBridge hold an active account and secondary accounts, using a secondary one when the active account hits its quota.

## Global preference and exceptions

```bash
python3 -m enginebridge prefer claude
python3 -m enginebridge resolve --project demonstracao --stage padrao
python3 -m enginebridge prefer codex
python3 -m enginebridge resolve --project demonstracao --stage padrao
```

`prefer` modifies only this YAML and preserves comments. Stages with an explicit `perfil` or `motor` remain fixed; the global switch affects stages without that choice. Inherited model and effort settings continue to come from the existing central source. Effort does not measure quality equivalence between model families.

```bash
python3 -m enginebridge --state .state/demo.sqlite block --pool codex-principal
python3 -m enginebridge --state .state/demo.sqlite unblock --pool codex-principal
```

Suspending an account prevents new admissions in EngineBridge, including for jobs that have already been resolved. Manually removing the block preserves any temporary quota suspension. By default, state is stored in `~/.local/state/enginebridge/state.sqlite`; all consumers on the same machine must share this path and configuration. Do not put this SQLite database on a network drive.

## Run text through your subscription

```bash
printf 'Reply with one sentence about profiles by stage.' | python3 -m enginebridge run --project demonstracao --stage roteiro
```

This command uses the selected subscription. It runs Claude Code or Codex in a temporary directory, without personal MCP, an enabled shell, or a shared native session. API credentials are removed from the environment. It does not run agent workflows, publishing, image generation, or translation. The binaries must accept the arguments documented by the adapter; local tests use mock executables and do not verify sign-in or the real operation of either CLI.

## Continuity contract

- Selection by call, stage, project, and global preference, always subject to permissions and fixed stages.
- An explicit alternative for fixed stages; for open stages, project-level or global alternatives.
- Quota shared by account (`quota_pool`), regardless of model name; one simultaneous run per pool in this core.
- A structured quota rejection, with no partial response or tools, allows trying the alternative and persisting the temporary suspension.
- A local error, timeout, prose-only error message, or result rejected by the validator stops the work without an automatic retry.
- Each job stores a resolved copy of the models; urgent blocks and account changes are checked before each attempt.

Examples of Python and CLI usage are in `examples/`. There is no active integration with OpenPCBotV3, Refazvideo, or cron jobs. OpenRouter is listed as a disabled future extension; this version has no API adapter, even if someone changes `habilitado` in the YAML.

## Development

```bash
python3 -m compileall -q enginebridge examples tests
python3 -m unittest discover -s tests -v
python3 -m enginebridge --version
```

[MIT License](LICENSE). The design reuses references to independent providers from WiFi and the Astra review, preserved in `docs/`.
