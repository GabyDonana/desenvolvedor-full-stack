# exercício 101 ----------------------------------------------------------------------------------------- #

'''

def saudacao():
    print("Bem-vindo ao programa!")

saudacao()

'''

# exercício 102 ----------------------------------------------------------------------------------------- #

'''

def saudacao(nome):
    print("Oii", nome, "seja bem-vindo ao programa!")

saudacao("Gaby,")

'''

# exercício 103 ----------------------------------------------------------------------------------------- #

'''

numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite um numero: "))

def somar(numero_1, numero_2):
    return numero_1 + numero_2

resultado = somar(numero_1, numero_2)

print("O resultado é:", resultado)

'''

# exercício 104 ----------------------------------------------------------------------------------------- #

'''

numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite um numero: "))

def maior(numero_1, numero_2):
    if numero_1 > numero_2:
        return numero_1
    else:
        return numero_2

resultado = maior(numero_1, numero_2)

print("O maior número informado é:", resultado)

'''

# exercício 105 ----------------------------------------------------------------------------------------- #

'''

numero = int(input("Digite um número inteiro: "))

def funcao(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

print(f"O número é: {funcao(numero)}")

'''

# exercício 106 ----------------------------------------------------------------------------------------- #

'''

numero_1 = int(input("Digite a primeira nota: "))
numero_2 = int(input("Digite a segunda nota: "))
numero_3 = int(input("Digite a terceira nota: "))

def media():
    resultado = (numero_1 + numero_2 + numero_3) / 3
    return resultado

print("A média das notas será:", media())

'''

# exercício 107 ----------------------------------------------------------------------------------------- #

'''

largura = int(input("Digite a lagura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

def area():
    resultado = (largura * altura)
    return resultado

print("A área do retâmgulo é:", area())

'''

# exercício 108 ----------------------------------------------------------------------------------------- #

'''

celsius = float(input("Digite a temperatura em Celsius: "))

def converter():
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

print("A temperatura em Fahrenheit é:", converter())

'''

# exercício 109 ----------------------------------------------------------------------------------------- #

'''

numero = int(input("Digite um número inteiro que não seja negativo: "))

def fatorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado

print("O fatorial desse número é:", fatorial(numero))

'''

# exercício 110 ----------------------------------------------------------------------------------------- #

'''

def primo(numerozinho):
    if numerozinho < 2:
        return False
    
    for i in range(2, numerozinho):
        if numerozinho % i == 0:
            return False
        
    return True

numerozinho = int(input("Digite um número: "))

if primo(numerozinho):
    print("Esse número é primo!")
else:
    print("Esse número não é primo!")
    
'''

# exercício 111 ----------------------------------------------------------------------------------------- #

'''

frase = input("Digite uma palavra ou uma fase: ")

def vogal(frase):
    quantidade = 0

    for letra in frase.lower():
        if letra in "aeiou":
            quantidade += 1

    return quantidade

resultado = vogal(frase)

print("Quantidade de vogais:", resultado)

'''

# exercício 112 ----------------------------------------------------------------------------------------- #

'''

lista_numeros = [7, 17, 22]

def maiorzao(lista_numeros):
    maior = lista_numeros[0]

    for numero in lista_numeros:
        if numero > maior:
            maior = numero

    return maior

print(maiorzao(lista_numeros))

'''

# exercício 113 ----------------------------------------------------------------------------------------- #

'''

quantidade = int(input("Informe a quantidade de números: "))
lista = []

def calcular_media(lista):
    for contador in range(quantidade):
        numero_digitado = float(input("Digite um número: "))
        lista.append(numero_digitado)

    if len(lista) == 0:
        return "A lista está vazia!"

    soma = 0
    for numero in lista:
        soma += numero

    media_aritmetica = soma / len(lista)
    return media_aritmetica

resultado_media = calcular_media(lista)
print(resultado_media)

'''

# exercício 114 ----------------------------------------------------------------------------------------- #

'''

lista_de_numeros = []

for i in range(4):
    numero = int(input("Digite um número: "))
    lista_de_numeros.append(numero)

def nova_lista(lista_de_numeros):
    numeros_positivos = []

    for numero in lista_de_numeros:
        if numero > 0:
            numeros_positivos.append(numero)

    return numeros_positivos

resultado = nova_lista(lista_de_numeros)
print(resultado)

'''

# exercício 115 ----------------------------------------------------------------------------------------- #

'''

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

def somar(numero_1, numero_2):
    return numero_1 + numero_2

def subtrair(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicar(numero_1, numero_2):
    return numero_1 * numero_2

def dividir(numero_1, numero_2):
    if numero_2 == 0:
        return numero_1 / numero_2

while True:
    print("1 - Somar | 2 - Subtrair | 3 - Multiplicar | 4 - Dividir | 0 - Sair")
    numero = (input("Escolha qual operção será realizada: "))

    if numero == "0":
        break
    elif numero == "1":
        print(somar(numero_1, numero_2))
    elif numero == "2":
        print(subtrair(numero_1, numero_2))
    elif numero == "3":
        print(multiplicar(numero_1, numero_2))
    elif numero == "4":
        print(dividir(numero_1, numero_2))
    else:
        print("Nao existe essa opção.")
        
'''