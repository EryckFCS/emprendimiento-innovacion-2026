#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Econ. José Vicente Course Server - Servidor y API de Alumnos
Sirve la landing page del curso en el puerto 8001 y gestiona el registro de leads del curso.
"""

import os
import json
import http.server
import socketserver
from urllib.parse import urlparse

PORT = 8001
WEB_DIR = os.path.join(os.path.dirname(__file__), '..', 'web')
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
LEADS_FILE = os.path.join(DATA_DIR, 'leads.json')

class JVCourseRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_POST(self):
        parsed_url = urlparse(self.path)
        
        if parsed_url.path == '/api/leads':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                lead_info = json.loads(post_data.decode('utf-8'))
                
                # Validar campos
                required_fields = ["name", "business", "whatsapp"]
                if not all(field in lead_info for field in required_fields):
                    self.send_error_response(400, "Faltan campos obligatorios.")
                    return
                
                # Guardar en base de datos local del curso
                os.makedirs(DATA_DIR, exist_ok=True)
                leads = []
                if os.path.exists(LEADS_FILE):
                    try:
                        with open(LEADS_FILE, 'r', encoding='utf-8') as f:
                            leads = json.load(f)
                    except json.JSONDecodeError:
                        leads = []
                
                # Agregar metadatos
                lead_info["timestamp"] = os.popen('date -Iseconds').read().strip()
                leads.append(lead_info)
                
                with open(LEADS_FILE, 'w', encoding='utf-8') as f:
                    json.dump(leads, f, indent=4, ensure_ascii=False)
                
                self.send_success_response({"status": "success", "message": "Alumno registrado exitosamente en el backend."})
                print(f"[✔] Nuevo alumno pre-inscrito: {lead_info['name']} ({lead_info['whatsapp']})")
                
            except Exception as e:
                self.send_error_response(500, f"Error del servidor: {str(e)}")
        else:
            self.send_error_response(404, "Endpoint no encontrado.")

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

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), JVCourseRequestHandler) as httpd:
        print(f"\n[🚀 Backend del Curso Activo] Corriendo en: http://localhost:{PORT}")
        print(f"[*] Carpeta de la Landing Page del Curso: {WEB_DIR}")
        print(f"[*] Base de datos de alumnos en: {LEADS_FILE}")
        print("[*] Presiona Ctrl+C para detener el servidor del curso.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[■] Servidor del curso detenido.")

if __name__ == '__main__':
    run_server()
