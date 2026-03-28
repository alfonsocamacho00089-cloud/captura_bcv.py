import requests
from bs4 import BeautifulSoup
import json
import urllib3
import os

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
        tabla = soup.find('table')
        
        if tabla:
            filas = tabla.find_all('tr')
            for fila in filas:
                celdas = fila.find_all('td')
                # Ajustamos para agarrar la columna 1 (Banco) y la columna 3 (Precio)
                if len(celdas) >= 4:
                    nombre_banco = celdas[1].get_text(strip=True) # Cambiado a [1]
                    precio = celdas[3].get_text(strip=True).replace('.', '').replace(',', '.') # Cambiado a [3]
                    
                    if nombre_banco and "Fecha" not in nombre_banco:
                        resultado.append({
                            "banco": nombre_banco,
                            "precio": precio
                        })
    
        if resultado:
            with open("bancos.json", "w") as f:
                json.dump(resultado, f, indent=4)
            print("✅ ¡Tabla capturada con nombres correctos!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    capturar()
