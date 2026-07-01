from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Criação da lista de cidades para consulta.
lista_cidades = ['São Paulo', 'Campinas', 'Osasco', 'Sorocaba', 'Barueri']

app = Flask(__name__) # — cria a aplicação Flask em si. É tipo "ligar o servidor". O __name__ é uma variável especial do Python que diz pro Flask em qual arquivo ele está rodando.

@app.route("/") #  — isso é um decorator. Ele "etiqueta" a função logo abaixo dizendo: "quando alguém acessar o endereço /, execute essa função". É assim que o Flask sabe qual função chamar pra cada rota.
def index():
    return render_template("index.html")


@app.route("/resultado")

def resultado_final():
    cidade = request.args.get("cidade")

    if cidade in lista_cidades:
        
        chave_api = os.getenv("CHAVE_API")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"

        resultado = requests.get(url) # Aqui recebemos o retorno da API totalmente, e dentro de "resultado" tem o conteúdo JSON que precisamos
    
        if resultado.status_code == 200:

            dicionario = resultado.json() # Para tratarmos esses valores e transformarmos ele em um dicionario Python, utilizamos o método .json
            temperatura = dicionario["main"]["temp"]
            clima = dicionario["weather"][0]["description"]

            return render_template("resultado.html", 
                                temperatura=temperatura,
                                clima=clima,
                                cidade=cidade
                               )

        else:
            return render_template("resultado.html",
                                retorno_erro = resultado.status_code
                                )
    else:
        return render_template("resultado.html", 
                                cidade=cidade
                               )

# ESSA PARTE DO CÓDIGO TEM QUE SER SEMPRE NO FINAL!!!!!!!!!!!!

if __name__ == "__main__": #— Garante que o servidor só sobe quando você roda o arquivo diretamente (não quando ele é importado por outro arquivo). 
                            
    app.run(debug=True) # O debug=True faz o servidor reiniciar automaticamente toda vez que você salva o código


    