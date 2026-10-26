---
version: alpha
name: Base
description: Sistema visual base para cualquier proyecto. Grises, negro y blanco, con color solo para estados y avisos. Tema claro y oscuro. Se copia al proyecto y se adapta.
---

# Base

## Overview

Este archivo es un punto de partida. Define un sistema visual sobrio y neutro que sirve para casi cualquier interfaz: aplicaciones web, paneles de gestión, herramientas internas y apps móviles.

- **Personalidad:** callada y precisa. La interfaz no compite con el contenido.
- **Paleta:** grises, negro y blanco. El color solo aparece en los estados y avisos, con una escala viva pero contenida.
- **Tipografía:** Inter para la interfaz y JetBrains Mono para código y datos técnicos.
- **Densidad:** espaciosa donde se lee o se escribe, compacta en listas y tablas.
- **Temas:** claro y oscuro, según el sistema. Los dos tienen el mismo peso; ninguno es una versión secundaria del otro.

## Colors

Todo es gris salvo los estados. La tinta es casi negra en claro y casi blanca en oscuro, y hace de color principal: texto, botón principal y selección.

**Tema claro**

- **Tinta (#121212):** texto principal, botón principal, selección activa y bordes de lo seleccionado.
- **Papel (#F4F4F4):** el fondo de la app.
- **Hoja (#FFFFFF):** tarjetas, barra lateral, paneles, ventanas y campos.
- **Gris suave (#EFEFEF) y gris medio (#E6E6E6):** fondos de chips, código, pestañas y elementos activos de la navegación.
- **Línea (#E0E0E0) y línea marcada (#C9C9C9):** separadores, bordes de tarjetas y de campos.
- **Texto secundario (#666666):** descripciones, metadatos y etiquetas de campo.
- **Texto tenue (#9B9B9B):** fechas, contadores, ayudas y texto desactivado. Nunca para texto que haya que leer.
- **Resaltado (#E4E4E4):** fondo de texto marcado o de una coincidencia de búsqueda.

**Tema oscuro**

- **Tinta (#ECECEC)** sobre **papel (#0C0C0C)** y **hoja (#161616)**.
- **Gris suave (#1D1D1D)**, **gris medio (#262626)**, **línea (#2A2A2A)** y **línea marcada (#3A3A3A)**.
- **Texto secundario (#9A9A9A)**, **texto tenue (#6A6A6A)** y **resaltado (#2E2E2E)**.

**Estados: la única nota de color**

Seis colores marcan el estado de algo: una tarea, un pedido, un despliegue o un aviso.

| Token | Uso | Claro | Oscuro |
|---|---|---|---|
| `state-neutral` | Inactivo, pendiente, sin empezar | #878787 | #8F8F8F |
| `state-amber` | En curso, aviso | #C27C0E | #EEAB3A |
| `state-violet` | En revisión, destacado | #7452D6 | #AE95FF |
| `state-blue` | Listo, programado, información | #1F6FD1 | #5FA6FF |
| `state-green` | Hecho, correcto, publicado | #1C9152 | #4CCF86 |
| `state-red` | Error, fallo, acción destructiva | #D0393B | #FF7A70 |

El color de estado nunca va en el texto. Se usa de tres formas:

- **Punto de 6 px** delante del nombre del estado, dentro de un chip.
- **Fondo tintado:** el color de estado al 10 % sobre la hoja. El borde mezcla el color al 35 % con la línea.
- **Franja de 3 px** a la izquierda de una fila o tarjeta.

El texto encima sigue siendo tinta, así que el contraste no depende del color de estado.

```yaml
colors:
  primary: "#121212"
  on-primary: "#FFFFFF"
  background: "#F4F4F4"
  surface: "#FFFFFF"
  surface-container: "#EFEFEF"
  surface-container-high: "#E6E6E6"
  outline: "#E0E0E0"
  outline-strong: "#C9C9C9"
  on-surface: "#121212"
  on-surface-variant: "#666666"
  on-surface-faint: "#9B9B9B"
  highlight: "#E4E4E4"
  state-neutral: "#878787"
  state-amber: "#C27C0E"
  state-violet: "#7452D6"
  state-blue: "#1F6FD1"
  state-green: "#1C9152"
  state-red: "#D0393B"
  primary-dark: "#ECECEC"
  on-primary-dark: "#111111"
  background-dark: "#0C0C0C"
  surface-dark: "#161616"
  surface-container-dark: "#1D1D1D"
  surface-container-high-dark: "#262626"
  outline-dark: "#2A2A2A"
  outline-strong-dark: "#3A3A3A"
  on-surface-dark: "#ECECEC"
  on-surface-variant-dark: "#9A9A9A"
  on-surface-faint-dark: "#6A6A6A"
  highlight-dark: "#2E2E2E"
  state-neutral-dark: "#8F8F8F"
  state-amber-dark: "#EEAB3A"
  state-violet-dark: "#AE95FF"
  state-blue-dark: "#5FA6FF"
  state-green-dark: "#4CCF86"
  state-red-dark: "#FF7A70"
```

## Typography

Dos familias, cada una con un papel fijo:

- **Inter** para toda la interfaz: títulos, botones, menús, listas, tablas y formularios.
- **JetBrains Mono** para bloques de código, atajos de teclado, identificadores y cifras que se comparan en columna.

Las etiquetas de grupo (por ejemplo «AJUSTES DE LA CUENTA») van en mayúsculas, con letra de 11 px y espaciado de 0,07 em.

En móvil, los títulos de pantalla usan `screen-title-mobile`. El cuerpo de texto no baja de 14 px.

```yaml
typography:
  display:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.03em
  headline:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.02em
  title-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.01em
  title-md:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
  screen-title-mobile:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.07em
  code-md:
    fontFamily: JetBrains Mono
    fontSize: 12.5px
    fontWeight: 400
    lineHeight: 1.65
  code-badge:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.04em
```

## Layout

**Escritorio.** Estructura de partida con dos o tres columnas:

- **Barra lateral** de 224 px: logo, secciones y, abajo, el estado de la cuenta o de la sincronización.
- **Contenido** flexible. El texto largo mide como mucho 660 px de ancho y queda centrado.
- **Panel lateral** opcional de 340 px para detalles, propiedades o historial.

La cabecera mide 56 px y es fija. Por debajo de 900 px de ancho se esconde la barra lateral.

**Ritmo vertical.** 48 px entre secciones grandes, 24 px entre grupos y 16 px entre elementos de un grupo. Si algo se siente cargado, gana espacio antes que reducir la letra.

**Móvil.** Margen lateral de 16 px. Navegación inferior con tres a cinco destinos. El botón flotante queda a 18 px del borde.

La escala de espacios es de 4 px, con pasos de 8, 12, 16, 20, 24, 32 y 48.

```yaml
spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 48px
  sidebar-width: 224px
  panel-width: 340px
  content-max-width: 660px
  header-height: 56px
  control-height: 32px
  control-height-mobile: 40px
  mobile-nav-height: 72px
  fab-size: 56px
```

## Elevation & Depth

El sistema es casi plano. La jerarquía sale de capas de tono, no de sombras:

1. **Papel** al fondo.
2. **Hoja** para lo que se usa: tarjetas, paneles y campos.
3. **Grises suaves** para lo que agrupa: chips, código y pestañas.

Los bordes de 1 px (línea) separan casi todo. La selección se marca con un borde de tinta, no con color.

Solo flota lo que de verdad está encima: menús, ventanas, hojas inferiores de móvil, avisos emergentes y el botón flotante. Usan una sombra doble y suave:

- **Claro:** `0 1px 2px rgb(0 0 0 / 0.04), 0 8px 24px rgb(0 0 0 / 0.06)`.
- **Oscuro:** `0 1px 2px rgb(0 0 0 / 0.4), 0 8px 24px rgb(0 0 0 / 0.4)`.

Detrás de una ventana o una hoja inferior va un velo negro al 35–40 %.

## Shapes

Esquinas redondeadas y moderadas, que crecen con el tamaño del elemento:

- **4 px:** atajos de teclado y marcas pequeñas.
- **6 px:** elementos de menú y filas seleccionables.
- **8 px:** botones, campos y la búsqueda.
- **10 px:** tarjetas pequeñas, código, menús y avisos.
- **12 px:** listas, tablas e imágenes.
- **16 px:** ventanas y tarjetas de móvil.
- **18 px:** el botón flotante.
- **26 px:** la parte superior de las hojas inferiores de móvil.
- **Píldora:** chips, el indicador de la navegación móvil y los botones de móvil.

```yaml
rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 10px
  xl: 12px
  2xl: 16px
  fab: 18px
  sheet: 26px
  full: 9999px
```

## Iconography

- **Iconos de interfaz:** de trazo, 24 × 24, grosor 1,7, extremos y uniones redondeados, sin relleno. Se dibujan a 16 px en escritorio (14 px en chips) y a 20 px en móvil. Una librería que encaja con este estilo es Lucide.
- **Logos de terceros:** los oficiales, en un solo color y en el color del texto. Simple Icons (CC0) cubre la mayoría.
- **Logo:** en un solo color, para que funcione sobre fondo claro y oscuro.

## Components

**Botones.** Altura de 32 px, borde de línea y fondo de hoja. El principal es tinta con texto blanco (en oscuro, al revés). El fantasma no tiene borde ni fondo. En móvil miden 40 px y son píldoras.

**Campos.** Altura de 32 px, fondo de hoja y borde de línea marcada. Con el foco, el borde pasa a tinta. Con un error, el borde pasa a rojo y el mensaje va debajo, en tinta, con un punto rojo delante.

**Chips.** Píldoras de 22 px con fondo gris suave y texto secundario. El chip de estado lleva un punto del color de estado, fondo tintado y texto en tinta.

**Tarjetas.** Fondo de hoja, borde de línea y radio de 10 px. La tarjeta seleccionada lleva borde de tinta.

**Tablas y listas.** Filas de 40 px separadas por línea. La fila activa usa gris suave de fondo. Las cifras van alineadas a la derecha.

**Ventanas.** Fondo de hoja, radio de 16 px, sombra de lo que flota y velo detrás.

**Móvil.** La navegación inferior usa un indicador gris en píldora tras el destino activo. Las hojas inferiores tienen un asa de 36 × 4 px.

```yaml
components:
  app:
    backgroundColor: "{colors.background}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
  app-dark:
    backgroundColor: "{colors.background-dark}"
    textColor: "{colors.on-surface-dark}"
  page-title:
    textColor: "{colors.primary}"
    typography: "{typography.headline}"
  hero-title:
    textColor: "{colors.primary}"
    typography: "{typography.display}"
  section-title:
    textColor: "{colors.on-surface}"
    typography: "{typography.title-lg}"
  sidebar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-variant}"
    width: "{spacing.sidebar-width}"
    padding: "{spacing.lg}"
  sidebar-item-active:
    backgroundColor: "{colors.surface-container}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.sm}"
  header:
    backgroundColor: "{colors.background}"
    textColor: "{colors.on-surface}"
    typography: "{typography.title-md}"
    height: "{spacing.header-height}"
    padding: "{spacing.xl}"
  side-panel:
    backgroundColor: "{colors.surface}"
    width: "{spacing.panel-width}"
    padding: "{spacing.xl}"
  group-title:
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.label-caps}"
  content:
    width: "{spacing.content-max-width}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-lg}"
  button:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    height: "{spacing.control-height}"
    padding: "{spacing.md}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    height: "{spacing.control-height}"
  button-primary-dark:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary-dark}"
  button-ghost:
    textColor: "{colors.on-surface}"
    rounded: "{rounded.md}"
    height: "{spacing.control-height}"
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    height: "{spacing.control-height}"
    padding: "{spacing.sm}"
  input-placeholder:
    textColor: "{colors.on-surface-faint}"
  input-placeholder-dark:
    textColor: "{colors.on-surface-faint-dark}"
  chip:
    backgroundColor: "{colors.surface-container}"
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.label-md}"
    rounded: "{rounded.full}"
    height: 22px
    padding: "{spacing.sm}"
  chip-dark:
    backgroundColor: "{colors.surface-container-dark}"
    textColor: "{colors.on-surface-variant-dark}"
  state-dot-neutral:
    backgroundColor: "{colors.state-neutral}"
    size: 6px
  state-dot-amber:
    backgroundColor: "{colors.state-amber}"
    size: 6px
  state-dot-violet:
    backgroundColor: "{colors.state-violet}"
    size: 6px
  state-dot-blue:
    backgroundColor: "{colors.state-blue}"
    size: 6px
  state-dot-green:
    backgroundColor: "{colors.state-green}"
    size: 6px
  state-dot-red:
    backgroundColor: "{colors.state-red}"
    size: 6px
  state-dot-neutral-dark:
    backgroundColor: "{colors.state-neutral-dark}"
    size: 6px
  state-dot-amber-dark:
    backgroundColor: "{colors.state-amber-dark}"
    size: 6px
  state-dot-violet-dark:
    backgroundColor: "{colors.state-violet-dark}"
    size: 6px
  state-dot-blue-dark:
    backgroundColor: "{colors.state-blue-dark}"
    size: 6px
  state-dot-green-dark:
    backgroundColor: "{colors.state-green-dark}"
    size: 6px
  state-dot-red-dark:
    backgroundColor: "{colors.state-red-dark}"
    size: 6px
  divider:
    backgroundColor: "{colors.outline}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.outline-strong}"
    height: 1px
  divider-dark:
    backgroundColor: "{colors.outline-dark}"
    height: 1px
  divider-strong-dark:
    backgroundColor: "{colors.outline-strong-dark}"
    height: 1px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-surface-dark}"
  list:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.xl}"
  list-row-active:
    backgroundColor: "{colors.surface-container}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.sm}"
  meta-text:
    textColor: "{colors.on-surface-faint}"
    typography: "{typography.label-md}"
  meta-text-dark:
    textColor: "{colors.on-surface-faint-dark}"
  highlight:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.xs}"
  highlight-dark:
    backgroundColor: "{colors.highlight-dark}"
    textColor: "{colors.on-surface-dark}"
  kbd:
    backgroundColor: "{colors.surface-container}"
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.code-badge}"
    rounded: "{rounded.xs}"
  code-block:
    backgroundColor: "{colors.surface-container}"
    textColor: "{colors.on-surface}"
    typography: "{typography.code-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  code-block-dark:
    backgroundColor: "{colors.surface-container-dark}"
    textColor: "{colors.on-surface-dark}"
  modal:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.2xl}"
    padding: "{spacing.xl}"
  mobile-screen-title:
    textColor: "{colors.on-surface}"
    typography: "{typography.screen-title-mobile}"
  mobile-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: "{spacing.control-height-mobile}"
    padding: "{spacing.xl}"
  mobile-card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.2xl}"
    padding: "{spacing.lg}"
  mobile-nav:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-variant}"
    height: "{spacing.mobile-nav-height}"
  mobile-nav-indicator:
    backgroundColor: "{colors.surface-container-high}"
    rounded: "{rounded.full}"
    width: 56px
    height: 30px
  mobile-nav-indicator-dark:
    backgroundColor: "{colors.surface-container-high-dark}"
    rounded: "{rounded.full}"
  mobile-fab:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.fab}"
    size: "{spacing.fab-size}"
  mobile-sheet:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.sheet}"
    padding: "{spacing.lg}"
```

### Adaptación por plataforma

Los tokens son los mismos en todas las plataformas. Solo cambia dónde se declaran:

- **Web con CSS:** variables en `:root` para el tema claro y en `@media (prefers-color-scheme: dark)` para el oscuro.
- **Tailwind:** los tokens van en `theme.extend` y el modo oscuro usa `darkMode: "media"`.
- **Android con Jetpack Compose:** el `ColorScheme` de Material 3 se llena con estos tokens. No uses el color dinámico de Android (el que toma los tonos del fondo de pantalla), porque rompe la paleta neutra. Los colores de estado van en un objeto aparte, fuera del `ColorScheme`.

| Rol de Material 3 | Claro | Oscuro |
|---|---|---|
| `primary` | `primary` | `primary-dark` |
| `onPrimary` | `on-primary` | `on-primary-dark` |
| `background` | `background` | `background-dark` |
| `surface` | `surface` | `surface-dark` |
| `surfaceContainer` | `surface-container` | `surface-container-dark` |
| `surfaceContainerHigh` | `surface-container-high` | `surface-container-high-dark` |
| `onSurface` | `on-surface` | `on-surface-dark` |
| `onSurfaceVariant` | `on-surface-variant` | `on-surface-variant-dark` |
| `outline` | `outline-strong` | `outline-strong-dark` |
| `outlineVariant` | `outline` | `outline-dark` |

## Do's and Don'ts

- Do usar el color solo para los estados. Todo lo demás es gris, negro o blanco.
- Do poner el color de estado en el punto, la franja o el fondo tintado, nunca en el texto.
- Do marcar la selección con un borde de tinta, no con color.
- Do mantener el contraste WCAG AA (4,5:1) del texto en los dos temas.
- Do probar cada pantalla en claro y en oscuro antes de darla por buena.
- Do usar siempre tokens. Si falta uno, se añade a este archivo antes de usarlo en el código.
- Don't usar el texto tenue para nada que haya que leer: solo fechas, contadores y ayudas.
- Don't añadir sombras a tarjetas o paneles: solo flota lo que está encima.
- Don't usar el rojo para decorar: solo para errores y acciones destructivas.
- Don't usar los colores de marca de terceros: sus logos van en el color del texto.
- Don't reducir la letra para ganar sitio: se gana con espacio.
- Don't escribir colores, tamaños o radios sueltos en el código.
