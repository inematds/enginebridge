# EngineBridge

[![EngineBridge](guia/assets/banner-es.jpg)](https://inematds.github.io/enginebridge/guia/es/)

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

## Qué es

Tu automatización puede detenerse cuando una suscripción alcanza su cuota, aunque haya otra disponible. EngineBridge es una herramienta local para elegir qué motor de IA atiende cada etapa y usar una alternativa declarada cuando esté permitido. Está pensada para quienes mantienen bots, scripts y rutinas con Claude Code y Codex. Tú defines los perfiles, modelos y esfuerzo; el programa resuelve la elección sin consultar a una IA. Para ejecutar textos, se necesitan Python y los programas autenticados mediante suscripción.

**Versión 1.2.1 — núcleo local funcional; la integración con los sistemas reales aún está pendiente.**

[Guía completa](https://inematds.github.io/enginebridge/guia/es/) · [Arquitectura](docs/ARQUITETURA.md) · [Plan de adopción](docs/ADOCAO.md) · [Referencias y revisión de Astra](docs/REFERENCIAS.md)

> Los documentos técnicos enlazados están en portugués.

## Instalar y verificar

```bash
git clone https://github.com/inematds/enginebridge.git
cd enginebridge
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
python3 -m enginebridge resolve --project demonstracao --stage roteiro
```

Requiere Python 3.11+ y PyYAML 6. Los perfiles de demostración usan modelos explícitos y se pueden resolver sin iniciar sesión. Los niveles heredados usan `~/.config/inema/modelos.env`; en otra máquina, configura `modelos_env` y las rutas de los ejecutables en el YAML. La resolución no comprueba si el modelo está disponible en la suscripción.

## Simular el cambio sin consumir modelos

```bash
printf 'Crie um roteiro curto.' | python3 -m enginebridge --state .state/demo.sqlite run --project demonstracao --stage roteiro --simulate --fail-first
python3 -m enginebridge --state .state/demo.sqlite status
```

La simulación provoca un rechazo por cuota en Codex, registra una suspensión temporal en SQLite y entrega la misma solicitud al ejecutor ficticio Claude. El campo `simulado` distingue esta salida de una ejecución real. No modifica servicios, no consulta el saldo ni llama a modelos.

## Preparar cuentas en una máquina nueva

Instala Claude Code y Codex, inicia sesión con tu suscripción desde la terminal y ajusta `binario` en el YAML. Nunca uses una clave de API. El campo opcional `conta_env` apunta a un archivo de datos con la carpeta de la cuenta: `CODEX_HOME=/ruta` en Codex y `CLAUDE_CONFIG_DIR=/ruta` en Claude. Sin la variable, cada programa usa su carpeta predeterminada. La cuota sigue a la cuenta: cada carpeta tiene su propio pool (`claude-principal:claude-inematds`), y bloquear el pool base suspende todas las cuentas de ese motor.

```bash
codex login
claude auth login
mkdir -p ~/.config/inema
test -f ~/.config/inema/modelos.env || cp config/modelos.example.env ~/.config/inema/modelos.env
```

El ejemplo de modelos solo se copia si no existe una configuración central. La etapa `demonstracao/padrao` hereda el motor global y permite observar el cambio con `prefer`; roteiro y crítica siguen usando perfiles fijados.

## Dos cuentas de Claude: tener, mantener y cambiar

Cada suscripción de Claude Code queda en una carpeta de inicio de sesión propia: la primera en la carpeta predeterminada `~/.claude`, la segunda en `~/.claude-inematds`. Las dos quedan con la sesión iniciada al mismo tiempo y no se mezclan. `claude-conta` elige cuál se usa por defecto; en Codex, la misma función corresponde a `codex-conta`.

1. 🧠 Crear la carpeta de la segunda cuenta, con enlaces a reglas, hooks, skills, agentes, plugins y memoria: `claude-conta preparar inematds`.
2. 🧠 Iniciar sesión con la suscripción en esa carpeta, una vez: `CLAUDE_CONFIG_DIR=~/.claude-inematds claude auth login --claudeai --email <e-mail>`. Si el navegador no se abre, copie el enlace impreso, autorice con la cuenta correcta y pegue el código en la propia terminal.
3. ⚙️ Comprobar los inicios de sesión y el uso de cada cuenta: `claude-conta` y `claude-conta uso`.
4. 🧠 Cambiar la cuenta predeterminada: `claude-conta inematds` (o `claude-conta nei` para volver). Se aplica a terminales nuevos, temporizadores, servicios que se inicien después y EngineBridge; `--reinicia` también reinicia los servicios que están siempre activos.
5. 🧠 Usar la otra cuenta en una sola sesión, sin cambiar la predeterminada: `CLAUDE_CONFIG_DIR=~/.claude-inematds claude`.
6. ⚙️ EngineBridge lee la selección mediante `conta_env` del motor claude, asigna a cada cuenta su propio pool de cuota (`claude-principal:claude-inematds`) y rechaza el trabajo resuelto en la cuenta anterior ("Conta alterada").

La barra de estado muestra `cc:` y `cx:` con la cuenta de Claude y Codex de cada sesión. Las sesiones y los servicios ya abiertos siguen usando la cuenta anterior hasta reiniciarse. Se usa la cuenta de la carpeta predeterminada cuando no está la variable `CLAUDE_CONFIG_DIR`: con ella, Claude leería otro archivo de estado y perdería los conectores. Los conectores con inicio de sesión propio (MCP) piden iniciar sesión de nuevo en la carpeta nueva.

### Inicio de sesión de la segunda cuenta, una sola vez

El inicio de sesión lo haces tú, en tu terminal, porque es la autorización de la suscripción. Probado el 20/11/2026 en una máquina en la que el navegador no se abre solo:

1. En un terminal fuera de Claude, con la ventana ancha para que el enlace no se corte, ejecuta `CLAUDE_CONFIG_DIR=~/.claude-inematds claude auth login --claudeai --email <e-mail-da-conta>`.
2. El comando imprime un enlace `https://claude.ai/oauth/authorize?...` y queda esperando. No lo cierres ni pulses Enter.
3. Copia el enlace completo y ábrelo en cualquier navegador. Usa una ventana privada o el celular si el navegador ya tiene iniciada la sesión en la otra cuenta, y comprueba que la página muestre la cuenta correcta antes de hacer clic en Authorize.
4. La página muestra un código. Pega el código completo, incluida la parte después de `#`, en el mismo terminal que está esperando y pulsa Enter. Pegar en el chat de Claude no funciona: el código solo es válido para ese comando, una vez, y caduca en pocos minutos.
5. Comprueba con `claude-conta`: la carpeta nueva debe mostrar el correo electrónico de la segunda cuenta. Si aparece "(sem login)", repite desde el paso 1 y usa el código nuevo.

### Cambiar de cuenta con sesiones abiertas (se agotó la cuota a mitad de camino)

Una sesión abierta no cambia de cuenta por sí sola. Cierra y vuelve a abrir cada una con la cuenta nueva; la conversación continúa, porque ambas cuentas usan la misma carpeta de conversaciones (`~/.claude-inematds/projects` es un enlace a `~/.claude/projects`). Probado el 21/11/2026, con inematds en el límite de 5 h:

1. 🧠 Elegir la cuenta: `claude-conta nei` (o `claude-conta inematds`). Comprobar el margen antes con `claude-conta uso`.
2. ⚙️ Ver qué sesiones están abiertas, en qué terminal y cuenta, y cuáles se cerraron: `claude-conta sessoes` (o `claude-conta sessoes ~/projetos/<pasta>`). Muestra el id y la última solicitud de cada una; `← esta` marca la sesión desde la que se llamó al comando.
3. 🧠 En cada terminal: salir con `/exit` y, en la misma carpeta, ejecutar `unset CLAUDE_CONFIG_DIR CLAUDE_CONTA_AUTO` (solo si el terminal estaba en la otra cuenta) y `claude --resume <id>`.
4. 🧠 Comprobar en la barra de estado: `cc:nei` (o `cc:inematds`).

No uses `claude --continue` cuando haya más de una sesión en la misma carpeta: abre la conversación más reciente de la carpeta, que puede ser otra. Con el id, `--resume` abre la correcta; sin el id, muestra la lista para elegir.

**Pendiente:** el cron y otros llamadores directos de `claude` todavía no siguen la elección. Próximo paso: que todos lean la cuenta activa y, después, que EngineBridge tenga una cuenta activa y cuentas secundarias, usando la secundaria cuando la activa alcance su cuota.

## Preferencia global y excepciones

```bash
python3 -m enginebridge prefer claude
python3 -m enginebridge resolve --project demonstracao --stage padrao
python3 -m enginebridge prefer codex
python3 -m enginebridge resolve --project demonstracao --stage padrao
```

`prefer` modifica solo este YAML y conserva los comentarios. Las etapas con `perfil` o `motor` explícito permanecen fijadas; el cambio global afecta a las etapas sin esa selección. El modelo y el esfuerzo heredados siguen obteniéndose de la fuente central existente. El esfuerzo no mide la equivalencia de calidad entre familias de modelos.

```bash
python3 -m enginebridge --state .state/demo.sqlite block --pool codex-principal
python3 -m enginebridge --state .state/demo.sqlite unblock --pool codex-principal
```

Suspender una cuenta impide nuevas admisiones en EngineBridge, incluso en trabajos ya resueltos. Quitar el bloqueo manual mantiene cualquier suspensión temporal por cuota. El estado predeterminado se guarda en `~/.local/state/enginebridge/state.sqlite`; todos los consumidores de la misma máquina deben compartir esta ruta y la configuración. No pongas este SQLite en una red.

## Ejecutar un texto con la suscripción

```bash
printf 'Responda com uma frase sobre perfis por etapa.' | python3 -m enginebridge run --project demonstracao --stage roteiro
```

Este comando consume la suscripción seleccionada. Usa Claude Code o Codex en un directorio temporal, sin MCP personal, shell habilitado ni sesión nativa compartida. Se eliminan del entorno las credenciales de API. No ejecuta workflows de agente, publicación, imágenes ni traducción. Los binarios deben aceptar los argumentos documentados por el adaptador; las pruebas locales usan ejecutables ficticios y no comprueban el inicio de sesión ni el funcionamiento real de ninguna de las dos CLI.

## Contrato de continuidad

- Selección por llamada, etapa, proyecto y preferencia global, siempre sujeta a los permisos y las etapas fijadas.
- Alternativa explícita en las etapas fijadas; en las etapas libres, alternativas del proyecto o globales.
- Cuota compartida por cuenta (`quota_pool`), independiente del nombre del modelo; en este núcleo, una ejecución simultánea por pool.
- Un rechazo estructurado por cuota, sin respuesta parcial ni herramientas, permite probar la alternativa y guardar la suspensión temporal.
- Un error local, timeout, un mensaje de error solo en prosa o un resultado rechazado por el validador interrumpen el trabajo, sin reintentos automáticos.
- Cada trabajo guarda una copia resuelta de los modelos; los bloqueos urgentes y los cambios de cuenta se comprueban antes de cada intento.

Hay ejemplos de uso con Python y CLI en `examples/`. No hay integración activada con OpenPCBotV3, Refazvideo ni crons. OpenRouter aparece deshabilitado como una posible extensión futura; esta versión no incluye ningún adaptador de API, aunque alguien cambie `habilitado` en el YAML.

## Desarrollo

```bash
python3 -m compileall -q enginebridge examples tests
python3 -m unittest discover -s tests -v
python3 -m enginebridge --version
```

[Licencia MIT](LICENSE). El diseño reutiliza las referencias de proveedores independientes de WiFi y la crítica de Astra, conservadas en `docs/`.
