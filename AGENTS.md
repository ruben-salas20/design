# AGENTS.md

Plantilla de sistema visual (`DESIGN.md`) para copiar a cualquier proyecto.

## Archivos

- `DESIGN.md`: el sistema visual. Sigue la [especificación design.md](https://github.com/google-labs-code/design.md).
- `index.html`: muestra visual de `DESIGN.md`.
- `serve.py`: sirve `index.html` con `./serve.py`.
- `README.md`: cómo usar la plantilla.

## Reglas

- `DESIGN.md` e `index.html` dicen lo mismo. Si cambias uno, cambia el otro.
- Valida con `npx @google/design.md lint DESIGN.md`: 0 errores y 0 avisos.
- `DESIGN.md` describe el sistema, sin instrucciones de uso. Esas van en `README.md`.
- No pongas datos privados (IP, nombres de máquinas): el repo es público.
