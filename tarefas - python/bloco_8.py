# exercício 116 ----------------------------------------------------------------------------------------- #

'''

nome = input("Digite seu nome: ")

with open("nomes.txt", "w") as arquivo:
    arquivo.write(nome)
    
'''

# exercício 117 ----------------------------------------------------------------------------------------- #

'''

with open("nomes.txt", "a") as arquivo:
    while True:
        nome = input("Digite um nome ou 'sair': ")

        if nome == "sair":
            break
        arquivo.write(f"{nome}\n")

with open("nomes.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
'''

# exercício 118 ----------------------------------------------------------------------------------------- #

'''

with open("nomes.txt", "r") as arquivo:
    exibir = arquivo.read()

    print(exibir)

'''
    
# exercício 119 ----------------------------------------------------------------------------------------- #

'''

with open("nomes.txt", "r") as arquivo:
    for linha in arquivo:

        print(linha.strip())

'''

# exercício 120 ----------------------------------------------------------------------------------------- #

'''

with open("nomes.txt", "r") as arquivo:
    linha = 0

    for linhas in arquivo:
        linha += 1

print(linha)

'''

# exercício 121 ----------------------------------------------------------------------------------------- #

'''

try:
    numero = int(input("Digite um número inteiro: "))
    print("Número inteiro:", numero)

except ValueError:
    print("Babilônico, eu disse um número inteiro!")

'''

# exercício 122 ----------------------------------------------------------------------------------------- #

'''

try:
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))

    divisao = numero_1 / numero_2
    print("Resultado:", divisao)

except ValueError:
    print("Digite apenas números inteiros.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

'''

# exercício 123 ----------------------------------------------------------------------------------------- #

'''
import calculos

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

print(calculos.somar_numerozinhos(numero_1, numero_2))
print(calculos.subtrair_numerozinhos(numero_1, numero_2))

'''