#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMDL Validation System - Test de Estrés y Registro en Tiempo Real
Simula tráfico de PYMEs lojanas reales registrándose en el formulario de la Landing Page,
enviando peticiones POST al backend HTTP local en el puerto 8000.
"""

import time
import random
import requests

BACKEND_URL = "http://localhost:8000/api/leads"

# Pool de Prospectos Realistas del Cantón Loja para Simular Validación de Mercado
EMPRESAS_POOL = [
    {
        "name": "Carlos Valdivieso",
        "business": "Restaurante Sabores Lojanos",
        "whatsapp": "+593984152630",
        "niche": "gastronomia",
        "message": "Invierto USD 150 al mes en Meta Ads pero no sé si me trae clientes reales o es gasto en vano."
    },
    {
        "name": "María José Espinoza",
        "business": "Boutique Elegancia Loja",
        "whatsapp": "+593992857410",
        "niche": "retail",
        "message": "Quiero posicionarme en Google Maps porque las franquicias grandes me están quitando todos los clientes de calzado."
    },
    {
        "name": "Dr. Fernando Riofrío",
        "business": "Consultorio Dental OdontoSana",
        "whatsapp": "+593981049285",
        "niche": "servicios",
        "message": "Tengo una página de Facebook inactiva, necesito un sistema automático que agende citas directo por WhatsApp."
    },
    {
        "name": "Jefferson Alexander",
        "business": "Cafetería Aroma de Altura",
        "whatsapp": "+593991857204",
        "niche": "gastronomia",
        "message": "Subo Reels y TikToks todas las semanas pero no sé cómo convertirlos en mesas llenas en el local."
    },
    {
        "name": "Kristie Susana",
        "business": "Zapatería CalzaModa Loja",
        "whatsapp": "+593984719205",
        "niche": "retail",
        "message": "Quiero medir el costo por lead y el ROAS real de mis campañas de pauta en Loja."
    }
]

def run_realtime_simulation():
    print("\n" + "="*60)
    print("   AMDL FULL-STACK SYSTEM: TEST DE VALIDACIÓN EN TIEMPO REAL")
    print("="*60)
    print(f"[*] Conectando con API del Backend en: {BACKEND_URL}")
    print("[*] Asegúrate de que python3 scripts/backend_server.py esté corriendo en otra terminal.\n")
    
    success_count = 0
    
    for i, empresa in enumerate(EMPRESAS_POOL, 1):
        print(f"[{i}/{len(EMPRESAS_POOL)}] Simulanado visita y registro de: {empresa['business']}...")
        
        # Simulación de tiempo de lectura en la página (sliders de la calculadora, etc.)
        delay = random.uniform(1.0, 2.5)
        time.sleep(delay)
        
        try:
            # Enviar el POST real al backend local de Python en el puerto 8000
            response = requests.post(BACKEND_URL, json=empresa, timeout=5)
            result = response.json()
            
            if response.status_code == 200 and result.get("status") == "success":
                print(f"    [✔] Registro Exitoso en Backend Local! Msg: {result.get('message')}")
                success_count += 1
            else:
                print(f"    [❌] Falla en el Registro. Status Code: {response.status_code} | Msg: {result.get('message')}")
                
        except requests.exceptions.ConnectionError:
            print("    [❌] Error de Conexión: El Servidor Backend no está activo en el puerto 8000.")
            print("         (Por favor, corre 'python3 scripts/backend_server.py' en otra terminal para activar la API real.)")
            break
        except Exception as e:
            print(f"    [❌] Error Inesperado: {str(e)}")
            
    print("\n" + "="*60)
    print(f"   Simulación Finalizada. Registros Exitosos: {success_count}/{len(EMPRESAS_POOL)}")
    print("="*60 + "\n")

if __name__ == "__main__":
    run_realtime_simulation()
