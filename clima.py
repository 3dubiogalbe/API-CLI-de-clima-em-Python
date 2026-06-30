import requests
import os
from dotenv import load_dotenv

load_dotenv()


cidade = "São Paulo"
chave_api = os.getenv("CHAVE_API")
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"

resultado = requests.get(url) # Aqui recebemos o retorno da API totalmente, e dentro de "resultado" tem o conteúdo JSON que precisamos

dicionario = resultado.json() # Para tratarmos esses valores e transformarmos ele em um dicionario Python, utilizamos o método .json
temperatura = dicionario["main"]["temp"]
clima = dicionario["weather"][0]["description"]

print(resultado)
print(f"Temperatura em São Paulo: {temperatura} graus, e o clima atual: {clima}")