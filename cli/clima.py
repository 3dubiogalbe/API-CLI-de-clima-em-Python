import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Criação da lista de cidades para consulta.
lista_cidades = ['São Paulo', 'Campinas', 'Osasco', 'Sorocaba', 'Barueri']


#================================
# Acesso do usuário:

print("Bem-vindo ao sistema de clima!")
print("Selecione uma cidade abaixo:")
print("------------------------------")
print("Lista de cidades disponíveis:")

for indice, cidade in enumerate(lista_cidades):
    print(f"0{indice+1} - {cidade}")

cidade = ""

while cidade not in lista_cidades:

    cidade = input("Digite a cidade: ")

    if cidade in lista_cidades:
        print("Cidade válida! resultado abaixo:")

    else:
        print("Cidade inválida, digite novamente: ")


#================================
# Parte da API e retorno.

chave_api = os.getenv("CHAVE_API")
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"

resultado = requests.get(url) # Aqui recebemos o retorno da API totalmente, e dentro de "resultado" tem o conteúdo JSON que precisamos

if resultado.status_code == 200:
    print("Requisição atendida com sucesso!")

    dicionario = resultado.json() # Para tratarmos esses valores e transformarmos ele em um dicionario Python, utilizamos o método .json
    temperatura = dicionario["main"]["temp"]
    clima = dicionario["weather"][0]["description"]

    print(f"Temperatura em {cidade}: {temperatura} graus, e o clima atual: {clima}")
    print("Obrigado por utilizar o sistema de climas! até breve!")

else:
    print(f"Erro! >> código status: {resultado.status_code}")