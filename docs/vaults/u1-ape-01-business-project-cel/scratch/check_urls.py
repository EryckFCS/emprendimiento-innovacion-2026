import requests
import re

def check_url(url):
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            return True, response.status_code
        else:
            return False, response.status_code
    except Exception as e:
        return False, str(e)

urls = [
    "https://www.eumed.net/rev/oel/2019/10/necesidades-consultoria-mipymes.pdf",
    "https://polodelconocimiento.com/ojs/index.php/es/article/download/9378/24589",
    "https://repositorio.uti.edu.ec/items/ae7de7c4-42b2-4a53-9079-6b02798c5cbe",
    "https://www.lahora.com.ec/tungurahua/Por-que-no-crecen-las-Pymes-en-Ecuador-20240424-0083.html",
    "https://repositorio.flacsoandes.edu.ec/handle/10469/25007",
    "https://www.instagram.com/consultora.agemic/",
    "https://www.competencias.gob.ec/wp-content/uploads/2026/01/PLANIFICACION-INSTITUCIONAL-CNC-2025-2029.pdf",
    "https://www.oikonomics.com.ec",
    "https://www.semanticscholar.org/paper/Lean-Canvas-and-the-Business-Model-Canvas-Model-in-Razabillah-Junaedi/867770ead0a809e74e59df8d6f87f13bd12bae0d",
    "https://www.canva.com/es_mx/pizarra-digital/lean-canvas/",
    "https://innokabi.com/lienzo-lean-canvas-el-lienzo-de-los-emprendedores/",
    "https://miro.com/es/planificacion-estrategica/que-es-lean-canvas/",
    "https://doi.org/10.22267/rtend.202101.136",
    "https://doi.org/10.56712/latam.v5i5.288110",
    "https://doi.org/10.18623/rvd.v22.n2.3185",
    "https://www.anefi.com.ec/noticias/perspectivas-2026-un-ano-de-crecimiento-moderado-y-riesgos-inminentes",
    "https://cronica.com.ec/2026/03/13/camara-de-comercio-de-loja-bajo-la-tutela-de-raul-flores/",
    "https://cronica.com.ec/2026/01/21/camara-de-industrias-de-loja-con-expectativas-que-2026-sera-un-ano-productivo/"
]

print("| URL | Status | Result |")
print("| :--- | :--- | :--- |")
for url in urls:
    ok, result = check_url(url)
    status = "✅ OK" if ok else "❌ FAIL"
    print(f"| {url} | {status} | {result} |")
