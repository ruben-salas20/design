#!/usr/bin/env python3
"""Sirve esta carpeta para ver index.html en el navegador.

Uso:
  ./serve.py            localhost y, si hay Tailscale, también por Tailscale
  ./serve.py 3000       en otro puerto
  ./serve.py --lan      además, visible para toda la red local
"""
import argparse
import functools
import http.server
import json
import shutil
import socket
import subprocess
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PORT_ATTEMPTS = 20


class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=3).stdout
    except (OSError, subprocess.TimeoutExpired):
        return ""


def tailscale():
    if not shutil.which("tailscale"):
        return None, None
    ips = run(["tailscale", "ip", "-4"]).split()
    if not ips:
        return None, None
    try:
        name = json.loads(run(["tailscale", "status", "--self", "--json"]))["Self"]["DNSName"].rstrip(".")
    except (ValueError, KeyError):
        name = None
    return ips[0], name


def lan_ip():
    # Conectar un socket UDP no envía nada; solo revela la IP de salida.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(("10.255.255.255", 1))
            return s.getsockname()[0]
        except OSError:
            return None


def bind(hosts, port):
    handler = functools.partial(Handler, directory=str(ROOT))
    servers = []
    try:
        for host in hosts:
            servers.append(http.server.ThreadingHTTPServer((host, port), handler))
    except OSError:
        for s in servers:
            s.server_close()
        return None
    return servers


def main():
    parser = argparse.ArgumentParser(description="Sirve esta carpeta para ver index.html.")
    parser.add_argument("port", nargs="?", type=int, default=8088, help="puerto inicial (8088 por defecto)")
    parser.add_argument("--lan", action="store_true", help="hacerlo visible para toda la red local")
    args = parser.parse_args()

    ts_ip, ts_name = tailscale()
    if args.lan:
        hosts = ["0.0.0.0"]
    else:
        hosts = ["127.0.0.1"] + ([ts_ip] if ts_ip else [])

    for port in range(args.port, args.port + PORT_ATTEMPTS):
        servers = bind(hosts, port)
        if servers:
            break
    else:
        raise SystemExit(f"No hay ningún puerto libre entre {args.port} y {args.port + PORT_ATTEMPTS - 1}.")

    print(f"\n  Sirviendo {ROOT}\n")
    if port != args.port:
        print(f"  El puerto {args.port} estaba ocupado; uso el {port}.\n")
    print(f"  Local:      http://localhost:{port}/")
    if ts_ip:
        print(f"  Tailscale:  http://{ts_name or ts_ip}:{port}/")
    if args.lan and (ip := lan_ip()):
        print(f"  Red local:  http://{ip}:{port}/")
    if not args.lan:
        print("\n  Usa --lan para verlo desde cualquier dispositivo de la red local.")
    print("  Pulsa Ctrl+C para parar.\n")
    sys.stdout.flush()

    for s in servers[1:]:
        threading.Thread(target=s.serve_forever, daemon=True).start()
    try:
        servers[0].serve_forever()
    except KeyboardInterrupt:
        print("\n  Servidor parado.")
    finally:
        for s in servers:
            s.server_close()


if __name__ == "__main__":
    main()
