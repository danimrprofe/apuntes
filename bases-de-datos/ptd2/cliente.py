import requests

# Hacer una solicitud GET a la API Flask
response = requests.get('http://127.0.0.1:5000/api/hello')

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("Respuesta de la API:", response.text)
else:
    print("Error en la solicitud:", response.status_code)