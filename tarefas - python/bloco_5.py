# exercício 71 ------------------------------------------------------------------------------------------ #

'''

palavra_frase = input("Digite uma palavra ou frase: ")

print("A palavra ou frase digitada foi:", palavra_frase)

'''

# exercício 72 ------------------------------------------------------------------------------------------ #

'''

frase = input("Digite uma frase: ")

print(frase.upper())
print(frase.lower())

'''

# exercício 73 ------------------------------------------------------------------------------------------ #

'''

palavra = input("Digite uma palavra: ")

print(palavra[0])
print(palavra[len(palavra) - 1])

'''

# exercício 74 ------------------------------------------------------------------------------------------ #

'''

frase = input("Digite uma frase: ")

a = frase.lower()

print("A quantidade de a é ", a.count('a'))

'''

# exercício 75 ------------------------------------------------------------------------------------------ #

'''

palavra1 = input("Digite uma palavra: ")
palavra1 = palavra1.lower()

palavra2 = palavra1[::-1] 

if palavra1 == palavra2:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
    
'''

# exercício 76 ------------------------------------------------------------------------------------------ #

'''

palavra_frase = input("Uma palavra ou frase: ")

fatiamneto = palavra_frase[::-1] 

print(fatiamneto)

'''

# exercício 77 ------------------------------------------------------------------------------------------ #

'''

frase = input("Digite uma frase: ")

separa_frase = frase.split()

for frase_sepada in separa_frase:

    print(frase_sepada)
    
'''

# exercício 78 ------------------------------------------------------------------------------------------ #

'''

frase = input("Digite uma frase: ")

espaços = len(frase.split())

print(espaços)

'''

# exercício 79 ------------------------------------------------------------------------------------------ #

'''

frase = input("Digite uma frase: ")
palavra_substituida = input("Digite uma palavra a ser substituida: ")
palavra_nova = input("Digite a nova palavra: ")

print(frase.replace(palavra_substituida, palavra_nova))

'''

# exercício 80 ------------------------------------------------------------------------------------------ #

'''

email = input("Digite um e-mail: ")

if "@" in email and "." in email.split("@")[-1]:
    print("E-mail válido")
else:
    print("E-mail inválido")
    
'''