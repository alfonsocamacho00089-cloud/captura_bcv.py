import requests
import json

def capturar():
    # Esta fuente nos da todos los bancos de una vez
    url = "https://ve.dolarapi.com/v1/dolares"
    
    try:
        response = requests.get(url, timeout=25)
        data = response.json()
        
        # Filtramos para que solo guarde los bancos y el oficial
        resultado = []
        for item in data:
            # Aquí puedes agregar o quitar bancos según lo que necesites
            resultado.append({
                "banco": item.get('nombre'),
                "precio": item.get('promedio'),
                "fecha": item.get('fechaActualizacion')
            })
        
        if resultado:
            with open("bancos.json", "w") as f:
                json.dump(resultado, f, indent=4)
            print("✅ ¡Todos los bancos guardados!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    capturar()
