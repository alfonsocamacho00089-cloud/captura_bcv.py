import requests
import json

def capturar():
    # Usamos la API que suele tener acceso a las tasas informativas
    url = "https://pydolarvenezuela-api.vercel.app/api/v1/dollar?page=bcv"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    try:
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200:
            monitores = response.json().get('monitors', {})
            
            # Filtramos los bancos que te interesan (los de tus fotos)
            bancos_pro = ["Mercantil", "Provincial", "BNC", "Banco de Venezuela"]
            data_final = []
            
            for clave, info in monitores.items():
                if any(b in info['title'] for b in bancos_pro):
                    data_final.append({
                        "banco": info['title'],
                        "precio": info['price'],
                        "fecha": info.get('last_update', 'Reciente')
                    })
            
            # Guardamos el resultado en el archivo que leerá tu App
            with open("bancos.json", "w") as f:
                json.dump(data_final, f, indent=4)
            print("✅ Datos actualizados con éxito en bancos.json")
        else:
            print(f"❌ Error en API: {response.status_code}")
    except Exception as e:
        print(f"❌ Fallo total: {e}")

if __name__ == "__main__":
    capturar()
