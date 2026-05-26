"""
AMDL Digital Audit & Mystery Shopping Processor
Ubicación: docs/vaults/u1-ape-02-marketing-agency/scripts/run_shadow_audit.py

Ejecuta el análisis cuantitativo de la Auditoría Digital Forense para 5 restaurantes en Loja.
Calcula el Índice de Ineficiencia Digital (DII), proyecta la fuga financiera y genera gráficos de alta calidad.
"""

import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Configurar rutas relativas con Path
SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_DIR = SCRIPT_DIR.parent
DATA_RAW_DIR = VAULT_DIR / "data" / "raw"
DATA_PROC_DIR = VAULT_DIR / "data" / "processed"
ASSETS_DIR = VAULT_DIR / "assets"

# Asegurar existencia de directorios
DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)
DATA_PROC_DIR.mkdir(parents=True, exist_ok=True)
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# 1. Definir la base de datos de la auditoría (5 restaurantes en Loja)
audit_data = [
    {
        "Restaurante": "200 Millas",
        "Especialidad": "Mariscos / Fusión",
        "Completitud_SEO_Local": 80,  # en % (Google Maps reclamado, faltan datos)
        "Reviews_Leak": 35,          # % de opiniones Google Maps sin responder
        "Instagram_Lead_Leak": 40,   # % de comentarios en IG sin responder
        "Unanswered_Leads_Month": 45, # Leads mensuales sin responder
        "TTR_Mystery_Shopping": 45    # Time to Response en minutos vía WhatsApp
    },
    {
        "Restaurante": "Carbonero",
        "Especialidad": "Carnes / Parrilla",
        "Completitud_SEO_Local": 90,
        "Reviews_Leak": 20,
        "Instagram_Lead_Leak": 15,
        "Unanswered_Leads_Month": 12,
        "TTR_Mystery_Shopping": 15
    },
    {
        "Restaurante": "Café Indera",
        "Especialidad": "Cafetería / Tradicional",
        "Completitud_SEO_Local": 40,  # No reclamado, datos obsoletos
        "Reviews_Leak": 75,
        "Instagram_Lead_Leak": 65,
        "Unanswered_Leads_Month": 60,
        "TTR_Mystery_Shopping": 180
    },
    {
        "Restaurante": "La Estancia",
        "Especialidad": "Gastronomía Lojana",
        "Completitud_SEO_Local": 60,
        "Reviews_Leak": 50,
        "Instagram_Lead_Leak": 50,
        "Unanswered_Leads_Month": 30,
        "TTR_Mystery_Shopping": 120
    },
    {
        "Restaurante": "Pizzería La Mía",
        "Especialidad": "Italiana / Pizzas",
        "Completitud_SEO_Local": 50,  # No reclamado, sin horarios
        "Reviews_Leak": 85,
        "Instagram_Lead_Leak": 80,
        "Unanswered_Leads_Month": 85,
        "TTR_Mystery_Shopping": 240
    }
]

df = pd.DataFrame(audit_data)

# 2. Fórmulas de Inferencia Cuantitativa
# Cuento del DII: (100 - Completitud_SEO) representa la ineficiencia SEO
# El TTR se normaliza dividiendo por 240 minutos (4 horas, tope máximo de ineficiencia de respuesta)
df["Ineficiencia_SEO"] = 100 - df["Completitud_SEO_Local"]
df["Ineficiencia_TTR"] = (df["TTR_Mystery_Shopping"] / 240) * 100
df["Ineficiencia_TTR"] = df["Ineficiencia_TTR"].clip(upper=100) # Capped al 100%

# Índice de Ineficiencia Digital (DII)
df["DII"] = (df["Ineficiencia_SEO"] + df["Reviews_Leak"] + df["Instagram_Lead_Leak"] + df["Ineficiencia_TTR"]) / 4

# Parámetros del modelo econométrico de fuga de dinero
CONVERSION_RATE = 0.30    # 30% de leads de comentarios son de alta intención y comprarían
TICKET_PROMEDIO = 15.50   # USD promedio por persona en Loja
GRUPO_PROMEDIO = 3.0       # Un lead digital representa un grupo de mesa promedio de 3 personas
BILL_PROMEDIO = TICKET_PROMEDIO * GRUPO_PROMEDIO # USD 46.50 por mesa

# Fuga Financiera Mensual (USD)
df["Fuga_Financiera_Mensual"] = df["Unanswered_Leads_Month"] * CONVERSION_RATE * BILL_PROMEDIO

# Redondear para estética de presentación
df["DII"] = df["DII"].round(2)
df["Fuga_Financiera_Mensual"] = df["Fuga_Financiera_Mensual"].round(2)

# 3. Guardar Datasets
df.to_csv(DATA_RAW_DIR / "shadow_audit_dataset.csv", index=False)

# Exportar JSON limpio con estadísticas clave para el motor
statistics = {
    "total_audited": len(df),
    "average_dii": float(df["DII"].mean()),
    "total_financial_leakage_month": float(df["Fuga_Financiera_Mensual"].sum()),
    "highest_leakage_business": df.loc[df["Fuga_Financiera_Mensual"].idxmax(), "Restaurante"],
    "highest_leakage_value": float(df["Fuga_Financiera_Mensual"].max()),
    "average_ttr_minutes": float(df["TTR_Mystery_Shopping"].mean())
}

with open(DATA_PROC_DIR / "shadow_audit_results.json", "w", encoding="utf-8") as f:
    json.dump(statistics, f, indent=4, ensure_ascii=False)

print("[*] Datasets guardados con éxito.")

# 4. Generación de Visualizaciones Premium (Seaborn / Matplotlib)
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 14,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10
})

# Gráfico 1: Índice de Ineficiencia Digital (DII) por Local
plt.figure(figsize=(9, 5))
colors_dii = sns.color_palette("flare", n_colors=len(df))
ax1 = sns.barplot(
    x="DII", 
    y="Restaurante", 
    data=df.sort_values(by="DII", ascending=False), 
    palette=colors_dii,
    hue="Restaurante",
    legend=False
)
plt.title("Índice de Ineficiencia Digital (DII) en Gastronomía de Loja", pad=15, fontweight="bold", color="#1e293b")
plt.xlabel("DII (%) - (Mayor porcentaje implica peor desempeño digital)", labelpad=10, fontweight="semibold", color="#475569")
plt.ylabel("Establecimiento", labelpad=10, fontweight="semibold", color="#475569")
plt.xlim(0, 100)

# Añadir etiquetas de datos en las barras
for p in ax1.patches:
    width = p.get_width()
    plt.text(
        width + 2, 
        p.get_y() + p.get_height() / 2, 
        f"{width:.1f}%", 
        ha="left", 
        va="center", 
        fontsize=10, 
        fontweight="bold", 
        color="#1e293b"
    )

plt.tight_layout()
plt.savefig(ASSETS_DIR / "shadow_audit_dii.png", dpi=300)
plt.close()

# Gráfico 2: Fuga Financiera Proyectada (USD Mensual)
plt.figure(figsize=(9, 5))
df_sorted_leak = df.sort_values(by="Fuga_Financiera_Mensual", ascending=True)
colors_leak = sns.color_palette("crest", n_colors=len(df))

ax2 = sns.barplot(
    x="Fuga_Financiera_Mensual", 
    y="Restaurante", 
    data=df_sorted_leak, 
    palette=colors_leak,
    hue="Restaurante",
    legend=False
)
plt.title("Fuga de Facturación Mensual Estimada por Ineficiencia Digital", pad=15, fontweight="bold", color="#1e293b")
plt.xlabel("Ingresos Perdidos Proyectados (USD / Mes)", labelpad=10, fontweight="semibold", color="#475569")
plt.ylabel("Establecimiento", labelpad=10, fontweight="semibold", color="#475569")

# Añadir etiquetas de datos en las barras
for p in ax2.patches:
    width = p.get_width()
    plt.text(
        width + 15, 
        p.get_y() + p.get_height() / 2, 
        f"USD ${width:,.2f}", 
        ha="left", 
        va="center", 
        fontsize=10, 
        fontweight="bold", 
        color="#0f766e"
    )

plt.tight_layout()
plt.savefig(ASSETS_DIR / "shadow_audit_financial.png", dpi=300)
plt.close()

print("[*] Gráficos de alta definición generados en assets/ con éxito.")
print(f"[*] Fuga total calculada en Loja: USD ${statistics['total_financial_leakage_month']:,.2f} al mes.")
