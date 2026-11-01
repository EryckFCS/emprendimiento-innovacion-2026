#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMDL Agency Simulator - Generación Forense de Métricas de Campaña
Simula la extracción de APIs de Meta y Google Ads basándose en credenciales locales.
"""

import os
import json
import csv
import random
from datetime import datetime, timedelta

def load_mock_credentials():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'credentials_template.json')
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("[Alerta] No se encontró config/credentials_template.json. Usando credenciales de respaldo.")
        return {}

def generate_daily_simulation(days=30):
    credentials = load_mock_credentials()
    
    # Validar que existan "credenciales" (incluso si son mock/simuladas)
    if "meta_ads_api" not in credentials:
        print("[Error] Estructura de credenciales corrupta o no inicializada.")
        return

    print(f"[*] Autenticando con Meta Ads API Account: {credentials['meta_ads_api']['ad_account_id']}...")
    print(f"[*] Autenticando con Google Ads API Customer ID: {credentials['google_ads_api']['customer_id']}...")
    
    # Crear carpeta de datos si no existe
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    csv_path = os.path.join(data_dir, 'daily_metrics.csv')
    
    # Benchmarks de Simulación (Loja Gastronómica)
    cpc_meta = 0.12
    cpc_google = 0.18
    conversion_rate = 0.027 # 2.7%
    ticket_promedio = 22.50 # USD 22.50 por pedido gastronómico
    
    start_date = datetime.now() - timedelta(days=days)
    
    headers = ["Fecha", "Meta_Spend_USD", "Google_Spend_USD", "Total_Spend_USD", "Clics_Meta", "Clics_Google", "Leads_Convertidos", "Ventas_USD", "ROAS", "CAC_Proyectado"]
    
    rows = []
    for i in range(days):
        current_date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        
        # Variabilidad aleatoria diaria de presupuesto
        meta_spend = round(random.uniform(5.0, 15.0), 2)
        google_spend = round(random.uniform(3.0, 10.0), 2)
        total_spend = round(meta_spend + google_spend, 2)
        
        clics_meta = int(meta_spend / cpc_meta)
        clics_google = int(google_spend / cpc_google)
        total_clics = clics_meta + clics_google
        
        # Tasa de conversión aleatoria con media de 2.7%
        daily_cr = random.normalvariate(conversion_rate, 0.005)
        daily_cr = max(0.01, min(daily_cr, 0.05)) # límites lógicos
        
        leads = int(total_clics * daily_cr)
        
        # Simulación de ventas atribuibles
        tasa_cierre = 0.60 # 60% de los leads cualificados terminan comprando
        ventas_num = int(leads * tasa_cierre)
        ventas_usd = round(ventas_num * ticket_promedio, 2)
        
        roas = round(ventas_usd / total_spend, 2) if total_spend > 0 else 0.0
        cac = round(total_spend / ventas_num, 2) if ventas_num > 0 else 0.0
        
        rows.append([
            current_date,
            meta_spend,
            google_spend,
            total_spend,
            clics_meta,
            clics_google,
            leads,
            ventas_usd,
            roas,
            cac
        ])
        
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
        
    print(f"[✔] Simulación finalizada. Reporte forense generado con éxito en: {csv_path}")

if __name__ == "__main__":
    generate_daily_simulation()
