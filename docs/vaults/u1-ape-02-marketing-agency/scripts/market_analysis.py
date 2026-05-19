"""
Script de Análisis de Mercado - AMDL
Calcula proyecciones de ROAS y CPA basadas en benchmarks de 2026.
"""

def calculate_projections(investment, industry="Gastronomía"):
    # Benchmarks 2026 (Ecuador/Loja)
    benchmarks = {
        "Gastronomía": {"cpc": 0.35, "roas": 3.5, "conv_rate": 0.05},
        "Retail": {"cpc": 0.75, "roas": 4.2, "conv_rate": 0.03},
        "Salud": {"cpc": 1.10, "roas": 3.9, "conv_rate": 0.02}
    }
    
    data = benchmarks.get(industry)
    if not data:
        return "Industria no encontrada"
    
    clics = investment / data["cpc"]
    conversiones = clics * data["conv_rate"]
    ingresos_proyectados = investment * data["roas"]
    cpa = investment / conversiones if conversiones > 0 else 0
    
    return {
        "Inversión": investment,
        "Clics Estimados": round(clics, 0),
        "Conversiones": round(conversiones, 0),
        "Ingresos Proyectados": round(ingresos_proyectados, 2),
        "CPA Estimado": round(cpa, 2),
        "ROAS": data["roas"]
    }

if __name__ == "__main__":
    inv = 500
    ind = "Gastronomía"
    results = calculate_projections(inv, ind)
    
    print(f"--- Proyección de Performance para {ind} ---")
    for key, value in results.items():
        print(f"{key}: {value}")
