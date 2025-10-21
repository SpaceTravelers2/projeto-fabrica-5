import requests


API_CEP = "https://cep.awesomeapi.com.br/json/"
GOOGLE = "https://www.google.com/search"


def buscar_cep(cep_usuario):
    endereco_com_cep = f"{API_CEP}{cep_usuario}"


    resposta = requests.get(endereco_com_cep)


    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        return None


def descobrir_cep(endereco_usuario):
   #Futuramente melhorar essa função para retornar o CEP correto
   resposta = requests.get(GOOGLE, params={"q": endereco_usuario})
   return resposta.url