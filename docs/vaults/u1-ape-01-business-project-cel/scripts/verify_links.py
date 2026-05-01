import requests

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
    "https://anefi.com.ec/blog/perspectivas-economicas-ecuador-2026",
    "https://cronica.com.ec/2026/01/20/fernando-flores-camara-comercio/",
    "https://cronica.com.ec/2026/02/15/industria-loja-resiliencia/",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

for url in urls:
    try:
        response = requests.head(url, headers=headers, allow_redirects=True, timeout=10)
        if response.status_code < 400:
            print(f"[OK] {response.status_code} - {url}")
        else:
            # Fallback to GET if HEAD is not supported
            response = requests.get(
                url, headers=headers, allow_redirects=True, timeout=10, stream=True
            )
            if response.status_code < 400:
                print(f"[OK] {response.status_code} - {url}")
            else:
                print(f"[FAIL] {response.status_code} - {url}")
    except Exception as e:
        print(f"[ERROR] {str(e)} - {url}")
