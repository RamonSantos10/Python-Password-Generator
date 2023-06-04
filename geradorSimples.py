from random import *


def geradorDeSenhaSimples(qCaracteres):
    qCaracteres = int(qCaracteres)

    lista_letrasMai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lista_letrasMin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'u', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lista_especiais = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '_', '{', '|', '}']
    listasCaracteres = [lista_letrasMai, lista_letrasMin, lista_numeros, lista_especiais]

    
    senhaSeparada = []
    senhaUnida = ''
    newCaracter = ''
    

    for caracterSenha in range(1, qCaracteres+1):
        listaEscolhida = choice(listasCaracteres)
        newCaracter = choice(listaEscolhida)
        senhaSeparada.append(newCaracter)

    for caracter in senhaSeparada:
        senhaUnida += caracter

    return senhaUnida