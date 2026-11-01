#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMDL Backend Server - Servidor local de producción y API de leads
Sirve los archivos estáticos de la carpeta web/ y maneja el registro inmutable de prospectos.
"""

import os
import json
import http.server
import socketserver
from urllib.parse import urlparse

PORT = 8000
WEB_DIR = os.path.join(os.path.dirname(__file__), '..', 'web')
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
LEADS_FILE = os.path.join(DATA_DIR, 'leads.json')

class AMDLRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Configurar la carpeta web/ como la raíz para servir archivos estáticos
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_POST(self):
        parsed_url = urlparse(self.path)
        
        # Endpoint de API para registrar prospectos del Test de Humo
        if parsed_url.path == '/api/leads':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                lead_info = json.loads(post_data.decode('utf-8'))
                
                # Validar campos contractuales mínimos
                required_fields = ["name", "business", "whatsapp", "niche"]
                if not all(field in lead_info for field in required_fields):
                    self.send_error_response(400, "Faltan campos obligatorios en el registro.")
                    return
                
                # Persistencia inmutable local
                os.makedirs(DATA_DIR, exist_ok=True)
                leads = []
                if os.path.exists(LEADS_FILE):
                    try:
                        with open(LEADS_FILE, 'r', encoding='utf-8') as f:
                            leads = json.load(f)
                    except json.JSONDecodeError:
                        leads = []
                
                # Enriquecer con timestamp y metadatos
                lead_info["timestamp"] = datetime_str = datetime_str = os.popen('date -Iseconds').read().strip()
                leads.append(lead_info)
                
                with open(LEADS_FILE, 'w', encoding='utf-8') as f:
                    json.dump(leads, f, indent=4, ensure_ascii=False)
                
                # Responder con éxito
                self.send_success_response({"status": "success", "message": "Lead registrado en el backend local inmutable exitosamente."})
                print(f"[✔] Nuevo prospecto registrado: {lead_info['business']} ({lead_info['name']})")
                
            except Exception as e:
                self.send_error_response(500, f"Error interno del servidor de simulación: {str(e)}")
        else:
            self.send_error_response(404, "Ruta de API no encontrada.")

    def send_success_response(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def send_error_response(self, code, message):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "error", "message": message}).encode('utf-8'))

    # Agregar soporte para CORS Preflight en caso de llamadas externas
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

def run_server():
    # Asegurar que el socket se pueda reutilizar de inmediato al reiniciar
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), AMDLRequestHandler) as httpd:
        print(f"\n[🚀 Backend Activo] AMDL local full-stack server corriendo en: http://localhost:{PORT}")
        print(f"[*] Servidor de archivos estáticos sirviendo desde: {WEB_DIR}")
        print(f"[*] Endpoint de API para leads activo en: http://localhost:{PORT}/api/leads")
        print("[*] Presiona Ctrl+C para detener el servidor local.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[■] Deteniendo servidor de backend local de forma limpia.")

if __name__ == '__main__':
    run_server()
