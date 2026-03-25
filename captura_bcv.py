import requests
import json

def capturar():
    # Usamos una fuente más directa para el BCV
    url = "https://pydolarvenezuela-api.vercel.app/api/v1/dollar?page=bcv"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=20)
        data = response.json()
        
        # Esto agarra TODOS los bancos que vengan en la lista del BCV
        monitores = data.get('monitors', {})
        resultado = []
        
        for nombre, info in monitores.items():
            resultado.append({
                "nombre": info.get('title'),
                "precio": info.get('price'),
                "actualizado": info.get('last_update')
            })
        
        # Si logramos conseguir datos, los guardamos
        if resultado:
            with open("bancos.json", "w") as f:
                json.dump(resultado, f, indent=4)
            print("✅ ¡Datos guardados con éxito!")
        else:
            print("⚠️ No se consiguieron bancos en este intento")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    capturar()
