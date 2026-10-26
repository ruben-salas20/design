# Base: un DESIGN.md para empezar cualquier proyecto

`DESIGN.md` es un sistema visual listo para copiar en cualquier proyecto. Le da al agente de programación una base clara: qué colores, fuentes, espacios y componentes usar, y qué reglas seguir.

El archivo sigue la especificación [design.md de Google Labs](https://github.com/google-labs-code/design.md). En esa especificación, los tokens (los valores con nombre, como `primary: "#121212"`) son la norma, y el texto explica cómo aplicarlos.

## Qué hay en esta carpeta

| Archivo | Para qué sirve |
|---|---|
| `DESIGN.md` | El sistema visual. Es lo que se copia al proyecto. |
| `index.html` | Una muestra visual de todo lo que incluye `DESIGN.md`. |
| `serve.py` | Sirve `index.html` para verlo en el navegador, también desde otros dispositivos. |
| `README.md` | Este documento: cómo usar el archivo. |

## Ver la muestra visual

Desde la carpeta del proyecto, ejecuta:

```
./serve.py
```

El script muestra las direcciones donde se ve la página:

```
  Local:      http://localhost:8088/
  Tailscale:  http://mi-maquina.mi-red.ts.net:8088/
```

Pulsa `Ctrl+C` para pararlo. Solo necesita Python 3, sin instalar nada más.

### Qué hace

- **Elige el puerto solo.** Empieza por el 8088. Si está ocupado, prueba el siguiente.
- **Usa Tailscale si lo hay.** Tailscale es la red privada que une tus dispositivos. Si la máquina lo tiene, la página se ve también desde tus otros dispositivos de Tailscale, pero no desde el resto de la red local.
- **Muestra los cambios al recargar.** No hace falta reiniciar el script después de editar `index.html`.

### Opciones

| Comando | Para qué |
|---|---|
| `./serve.py` | Localhost y, si lo hay, Tailscale |
| `./serve.py 3000` | Empezar a buscar puerto libre desde el 3000 |
| `./serve.py --lan` | Visible para cualquier dispositivo de la red local |
| `./serve.py -h` | Ver la ayuda |

### Qué tener en cuenta

- **Es temporal.** La página se ve mientras el script siga abierto. Para dejarla fija, móntala en un servidor web permanente, como Caddy o Nginx.
- **Las fuentes vienen de Google Fonts.** Sin internet, la página usa las fuentes del sistema.
- **Sin el script** también se ve: abre `index.html` con doble clic en el navegador.

## Cómo es el sistema

- **Paleta:** grises, negro y blanco. El color solo aparece en seis estados: neutro, ámbar, violeta, azul, verde y rojo.
- **Tipografía:** Inter para la interfaz y JetBrains Mono para código.
- **Temas:** claro y oscuro, según la preferencia del sistema operativo.
- **Profundidad:** casi plana. Las capas se distinguen por el tono; solo lo que flota lleva sombra.
- **Plataformas:** web (CSS o Tailwind) y Android con Jetpack Compose.

## Cómo usarlo

### 1. Copia el archivo

Copia `DESIGN.md` a la raíz del proyecto. No le cambies el nombre: los agentes buscan `DESIGN.md` exactamente.

### 2. Pide al agente que lo adapte

El agente necesita saber si el proyecto es nuevo o ya existe. Puedes pegarle uno de estos mensajes.

**Proyecto nuevo:**

> Lee `DESIGN.md`. Es la base visual de este proyecto. Cambia `name` y `description` por los del proyecto y reescribe la sección Overview con lo que es el producto y para quién es. Usa los tokens tal como están. Pregúntame antes de cambiar la paleta, las fuentes o la densidad.

**Proyecto existente:**

> Lee `DESIGN.md`. Antes de tocar nada, extrae del código los colores, fuentes, tamaños de letra, espacios, radios y sombras que ya usa el proyecto. Compáralos con `DESIGN.md` y preséntame las diferencias en una tabla. Para cada diferencia te diré qué manda: el proyecto o el archivo. Después, deja el archivo y el código diciendo lo mismo.

### 3. Ajusta lo que depende del proyecto

Estas partes casi siempre cambian:

- **`name` y `description`** de la cabecera, y la sección **Overview**.
- **El significado de los estados.** La tabla de Colors trae usos sugeridos (por ejemplo, ámbar para «en curso»). Cámbialos por los estados reales del proyecto: los de un pedido, una tarea o un despliegue.
- **Los componentes.** Borra los que el proyecto no use y añade los propios. Usa siempre referencias a tokens, como `{colors.primary}`, nunca valores sueltos.
- **Una tercera fuente**, si el proyecto tiene texto largo para leer, como artículos o documentación. Una serif como Source Serif 4 funciona bien con esta paleta.
- **El logo y los iconos.** Anota en Iconography dónde viven los archivos.
- **Las secciones que sobren.** Si quitas una entera, anótala en el campo `omitted` de la cabecera.

### 4. Valida el archivo

Después de cada cambio, comprueba que el archivo cumple la especificación:

```
npx @google/design.md lint DESIGN.md
```

El validador avisa de referencias rotas, colores sin usar, contraste insuficiente y secciones fuera de orden. La versión de esta carpeta pasa sin errores ni avisos.

## Reglas que no conviene romper

- El color solo marca estados. Todo lo demás es gris, negro o blanco.
- El color de estado va en un punto, una franja o un fondo tintado, nunca en el texto.
- El rojo es solo para errores y acciones destructivas.
- El texto mantiene un contraste WCAG AA (4,5:1) en los dos temas.
- Cada pantalla se prueba en claro y en oscuro.
- El código no lleva colores, tamaños ni radios sueltos: todo sale de los tokens.

## Origen

`DESIGN.md` nace del sistema visual de Tinta, una herramienta personal de escritura. Se quitó todo lo propio de esa app y se dejó la paleta neutra, la escala de espacios, los radios y los componentes comunes.
