#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Econ. José Vicente Course - Test de Registro de Alumnos
Realiza peticiones HTTP POST simuladas para registrar profesionales en el curso en el puerto 8001.
"""

import time
import random
import requests

BACKEND_URL = "http://localhost:8001/api/leads"

ALUMNOS_POOL = [
    {
        "name": "Ing. Patricio Cárdenas",
        "business": "Curso JV - Sector: municipal",
        "whatsapp": "+593982058102"
    },
    {
        "name": "Econ. Diana Guamán",
        "business": "Curso JV - Sector: consultor",
        "whatsapp": "+593994827105"
    },
    {
        "name": "Arq. Xavier Vivanco",
        "business": "Curso JV - Sector: privado",
        "whatsapp": "+593981048203"
    },
    {
        "name": "Ing. Gissela Ordóñez",
        "business": "Curso JV - Sector: municipal",
        "whatsapp": "+593992857104"
    },
    {
        "name": "Gabriela Eras",
        "business": "Curso JV - Sector: estudiante",
        "whatsapp": "+593984719205"
    }
]

def run_simulation():
    print("\n" + "="*60)
    print("   CURSO JOSÉ VICENTE: SIMULACIÓN DE REGISTROS B2B (MOCK RUN)")
    print("="*60)
    print(f"[*] Enviando peticiones POST al backend del curso: {BACKEND_URL}\n")
    
    success_count = 0
    
    for i, alumno in enumerate(ALUMNOS_POOL, 1):
        print(f"[{i}/{len(ALUMNOS_POOL)}] Registrando alumno: {alumno['name']}...")
        time.sleep(random.uniform(0.8, 1.8))
        
        try:
            response = requests.post(BACKEND_URL, json=alumno, timeout=5)
            result = response.json()
            
            if response.status_code == 200 and result.get("status") == "success":
                print(f"    [✔] Alumno registrado con éxito! Msg: {result.get('message')}")
                success_count += 1
            else:
                print(f"    [❌] Error en el registro: {result.get('message')}")
                
        except requests.exceptions.ConnectionError:
            print("    [❌] Error: El servidor del curso no está activo en el puerto 8001.")
            print("         (Por favor, ejecuta 'python3 scripts/backend_server.py' en su directorio.)")
            break
            
    print("\n" + "="*60)
    print(f"   Simulación Finalizada. Alumnos Registrados: {success_count}/{len(ALUMNOS_POOL)}")
    print("="*60 + "\n")

if __name__ == "__main__":
    run_simulation()
