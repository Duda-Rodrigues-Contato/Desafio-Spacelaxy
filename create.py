import json

arquivo_create = 'desafio-spacelaxy/create.json'

criar_dados = []

with open("create.json", "r", encoding="utf-8") as arquivo_create:
    dados = json.load(arquivo_create)


def add_info():

    nome = str(input("Me diga o nome:"))
    dados["nome"].append(nome)
    idade = int(input("Me diga sua idade:"))
    dados["idade"].append(idade)
    planeta = str(input("Digite seu planeta: "))
    dados["planeta"].append(planeta)
    lingua = str(input("Digite seu idioma: "))
    dados["lingua"].append(lingua)
    pontuacao_risco = int(input("Me diga sua pontuacao de risco: "))
    dados["pontuacao-de-risco"].append(pontuacao_risco)
    nivel_risco = int(input("Me diga seu nivel de risco: "))
    dados["nivel-de-risco"].append(nivel_risco)
    comportamento = int(input("Digite o comportamento mais frequente: "))
    dados["comportamento"].append(comportamento)
    alien = str(input("Alien ou n? "))
    dados["alien"].append(alien)

    with open("create.json", "w", encoding="utf-8") as arquivo_create:
        json.dump(criar_dados, arquivo_create, indent=4)

add_info()