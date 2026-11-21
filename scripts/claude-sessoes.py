#!/usr/bin/env python3
"""claude-conta sessoes [pasta] — quais sessões do Claude estão abertas, em qual conta e terminal,
e quais da pasta foram fechadas há pouco, com o comando para retomar cada uma (21/11/2026).

Lê só arquivos locais: /proc (processos claude), <pasta-de-config>/sessions/<pid>.json
(qual conversa cada processo tem aberta) e ~/.claude/projects/<pasta>/*.jsonl (assunto)."""
import json
import os
import sys
import time
from pathlib import Path

HOME = Path.home()
PASTAS = {"nei": HOME / ".claude", "inematds": HOME / ".claude-inematds"}
PROJETOS = HOME / ".claude" / "projects"  # as duas contas compartilham (link)


def assunto(jsonl: Path) -> str:
    """Último pedido escrito pelo usuário na conversa (sem textos de skill, aviso ou comando)."""
    ultimo = ""
    try:
        with jsonl.open(errors="replace") as f:
            for linha in f:
                try:
                    d = json.loads(linha)
                except ValueError:
                    continue
                if d.get("type") != "user":
                    continue
                c = d.get("message", {}).get("content")
                t = c if isinstance(c, str) else " ".join(
                    x.get("text", "") for x in (c or []) if isinstance(x, dict) and x.get("type") == "text")
                t = t.strip()
                if t and not t.startswith(("<", "Base directory", "[Usage", "Caveat")):
                    ultimo = t
    except OSError:
        pass
    return " ".join(ultimo.split())[:90] or "(sem pedido escrito)"


def abertas():
    for pid in filter(str.isdigit, os.listdir("/proc")):
        try:
            cmd = Path(f"/proc/{pid}/cmdline").read_bytes().split(b"\0")
            if not cmd or os.path.basename(cmd[0].decode()) != "claude" or b"-p" in cmd or b"--print" in cmd:
                continue
            env = dict(x.split("=", 1) for x in Path(f"/proc/{pid}/environ").read_bytes().decode(errors="replace").split("\0") if "=" in x)
            tty = os.readlink(f"/proc/{pid}/fd/0").replace("/dev/", "")
        except (OSError, UnicodeDecodeError):
            continue
        ccd = env.get("CLAUDE_CONFIG_DIR", "")
        conta = next((n for n, p in PASTAS.items() if ccd and Path(ccd) == p), "nei" if not ccd else ccd)
        cfg = Path(ccd) if ccd else PASTAS["nei"]
        try:
            info = json.loads((cfg / "sessions" / f"{pid}.json").read_text())
        except (OSError, ValueError):
            info = {}
        yield {"pid": pid, "tty": tty, "conta": conta, "sid": info.get("sessionId", "?"), "cwd": info.get("cwd") or os.readlink(f"/proc/{pid}/cwd")}


def main():
    alvo = Path(sys.argv[1] if len(sys.argv) > 1 else os.getcwd()).resolve()
    proprio, p = set(), os.getpid()  # ancestrais: se chamado de dentro de uma sessão, marca "esta"
    while p > 1:
        proprio.add(p)
        try:
            p = int(Path(f"/proc/{p}/stat").read_text().rsplit(")", 1)[1].split()[1])
        except (OSError, ValueError, IndexError):
            break
    lista = list(abertas())
    abertos = {s["sid"] for s in lista}
    print("Sessões abertas agora:")
    for s in sorted(lista, key=lambda s: s["tty"]):
        j = PROJETOS / str(s["cwd"]).replace("/", "-") / f"{s['sid']}.jsonl"
        marca = "  ← esta" if int(s["pid"]) in proprio else ""
        print(f"  {s['tty']:7} conta {s['conta']:9} {s['sid']}  {s['cwd'].replace(str(HOME), '~')}{marca}")
        print(f"          assunto: {assunto(j)}")
    pasta = PROJETOS / str(alvo).replace("/", "-")
    fechadas = [f for f in sorted(pasta.glob("*.jsonl"), key=lambda f: f.stat().st_mtime, reverse=True)
                if f.stem not in abertos and f.stat().st_size > 2000][:5]
    print(f"\nFechadas há pouco em {str(alvo).replace(str(HOME), '~')} (mais recente primeiro):")
    for f in fechadas:
        quando = time.strftime("%d/%m %H:%M", time.localtime(f.stat().st_mtime))
        print(f"  {quando}  {f.stem}\n          assunto: {assunto(f)}")
    print("\nRetomar uma sessão (na pasta dela, já na conta escolhida pelo claude-conta):")
    print("  unset CLAUDE_CONFIG_DIR CLAUDE_CONTA_AUTO   # só se o terminal estava na outra conta")
    print("  claude --resume <id>")


if __name__ == "__main__":
    main()
