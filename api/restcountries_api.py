import requests

BASE_URL = "https://restcountries.com/v3.1"
COMMON_FIELDS = "name,capital,population,region,subregion,flags,latlng,languages,cca2,cca3"

# Seteando del JSON de respuestas los campos que necesitamos
def _normalize_country_payload(d: dict) -> dict:
    return{
        "name": d.get("name",{}).get("common", "N/A"),
        "capital": (d.get("capital") or ["Desconocida"])[0],
        "population": d.get("population", 0),
        "region": d.get("region", "N/A"),
        "subregion": d.get("subregion", "N/A"),
        "flag_url": d.get("flags", {}).get("png") or d.get("flags", {}).get("svg"),
        "latlng": d.get("latlng") or [0, 0],
        "languages": ", ".join((d.get("languages") or {}).values()) or "N/A",
        "cca2": d.get("cca2", "NA"),
        "cca3": d.get("cca3", "NA"),        
    }

# Función que devuelve un dict normalizado del país o NONE si no lo encuentra...
def get_country_by_name(name: str):
    params = {"fields": COMMON_FIELDS}
    r = requests.get(f"{BASE_URL}/name/{name}", params=params, timeout=12)
    if r.status_code != 200:
        return None
    try:
        data = r.json()
        if not data:
            return None
        name_lower = name.strip().lower()
        exact = next((c for c in data if c.get("name", {}).get("common", "").lower() == name_lower), None)
        chosen = exact or data[0]
        return _normalize_country_payload(chosen)
    except Exception:
        return None

# Devolver un país por código ISO 
def get_country_by_code(code: str):
    params = {"fields": COMMON_FIELDS}
    r = requests.get(f"{BASE_URL}/alpha/{code}", params=params, timeout=12)
    if r.status_code != 200:
        return None
    try:
        data = r.json()
        if isinstance(data, list) and data:
            data = data[0]
        return _normalize_country_payload(data)
    except Exception:
        return None


