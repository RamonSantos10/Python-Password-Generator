from random import *


def geradorDeSenhaPersonalizado():
    qCaracteres = int(input('Diigite a quantidade de caracteres da senha: '))

    lista_letrasMai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lista_letrasMin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'u', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lista_especiais = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '_', '{', '|', '}']
    listasCaracteres = []

    
    senhaSeparada = []
    senhaUnida = ''
    newCaracter = ''

    preferences = str(input('Definir preferências da senha: \n 1 - Letras Maiúsculas \n 2 - Letras Minúsculas \n 3 - Números \n 4 - Caracteres Especiais \n Digite as preferências da senha: '))

    if '1' in preferences:
        listasCaracteres.append(lista_letrasMai)
    if '2' in preferences:
        listasCaracteres.append(lista_letrasMin)
    if '3' in preferences:
        listasCaracteres.append(lista_numeros)
    if '4' in preferences:
        listasCaracteres.append(lista_especiais)


    for caracterSenha in range(1, qCaracteres+1):
        listaEscolhida = choice(listasCaracteres)
        newCaracter = choice(listaEscolhida)
        senhaSeparada.append(newCaracter)

    for caracter in senhaSeparada:
        senhaUnida += caracter

    return senhaUnida