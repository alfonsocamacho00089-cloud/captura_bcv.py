import requests
import json

def capturar():
    url = "https://pydolarvenezuela-api.vercel.app/api/v1/dollar?page=bcv"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=25)
        data = response.json()
        monitores = data.get('monitors', {})
        
        # Guardamos la lista de bancos
        resultado = []
        for clave, info in monitores.items():
            resultado.append({
                "banco": info.get('title'),
                "precio": info.get('price'),
                "fecha": info.get('last_update')
            })
        
        if resultado:
            with open("bancos.json", "w") as f:
                json.dump(resultado, f, indent=4)
            print("¡Logrado!")
    except:
        print("Error al capturar")

if __name__ == "__main__":
    capturar()
