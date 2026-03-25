import requests
from bs4 import BeautifulSoup
import json
import urllib3

# Esto es para que no se queje por el certificado de seguridad del BCV
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def capturar():
    url = "https://www.bcv.org.ve/tasas-informativas-sistema-bancario"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, verify=False, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        resultado = []
        # Buscamos la tabla que contiene los bancos
        tabla = soup.find('table')
        
        if tabla:
            filas = tabla.find_all('tr')
            for fila in filas:
                celdas = fila.find_all('td')
                if len(celdas) >= 3:
                    # Limpiamos el texto de los bancos y los precios
                    nombre_banco = celdas[0].get_text(strip=True)
                    precio = celdas[2].get_text(strip=True).replace('.', '').replace(',', '.')
                    
                    if nombre_banco and "Institución" not in nombre_banco:
                        resultado.append({
                            "banco": nombre_banco,
                            "precio": precio
                        })
        
        if resultado:
            with open("bancos.json", "w") as f:
                json.dump(resultado, f, indent=4)
            print("✅ ¡Tabla capturada con éxito!")
        else:
            print("❌ No se encontró la tabla. El BCV cambió el diseño o bloqueó el acceso.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    capturar()
