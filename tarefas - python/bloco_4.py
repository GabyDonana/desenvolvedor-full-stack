# exercício 51 ------------------------------------------------------------------------------------------ #

'''

for numero in range(1, 11):
    print(numero)
    
'''

# exercício 52 ------------------------------------------------------------------------------------------ #

'''

for numero in range(10, -1, -1):
    print(numero)

print("Fimm")

'''

# exercício 53 ------------------------------------------------------------------------------------------ #

'''

for numero in range(0, 101, 2):
    print(numero)
    
'''

# exercício 54 ------------------------------------------------------------------------------------------ #

'''

for numero in range(1, 101, 2):
    print(numero)
    
'''

# exercício 55 ------------------------------------------------------------------------------------------ #

'''

numero = int(input("Digite um número: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
'''

# exercício 56 ------------------------------------------------------------------------------------------ #

'''

numero = int(input("Digite um número inteiro: "))

soma = 0

for contador in range(1, numero + 1):
    soma += contador

print("Soma:", soma)

'''

# exercício 57 ------------------------------------------------------------------------------------------ #

'''

numero = int(input("Digite um número inteiro: "))

fatorial = 1

for contador in range(1, numero + 1):
    fatorial *= contador            

print("Fatorial:", fatorial)

'''

# exercício 58 ------------------------------------------------------------------------------------------ #

'''

pares = 0

for contador in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        pares += 1

print("Quantidade de números pares:", pares)

'''

# exercício 59 ------------------------------------------------------------------------------------------ #

'''

soma = 0

for contador in range(10):
    numero = float(input(f"Digite o {contador + 1}º número: "))

    if numero > 0:
        soma += numero

print("Soma dos números positivos:", soma)

'''

# exercício 60 ------------------------------------------------------------------------------------------ #

'''

numero1 = float(input("Digite o 1º número: "))

for numero2 in range(2, 6):
    numero3 = float(input(f"Digite o {numero2}º número: "))

    if numero3 > numero1:
        numero1 = numero3

print("O maior número é ", numero1)

'''

# exercício 61 ------------------------------------------------------------------------------------------ #

'''

numero1 = float(input("Digite o 1º número: "))

for numero2 in range(2, 6):
    numero3 = float(input(f"Digite o {numero2}º número: "))

    if numero3 < numero1:
        numero1 = numero3

print("O menor número é ", numero1)

'''

# exercício 62 ------------------------------------------------------------------------------------------ #

'''

notas = 0

for notass in range(5):
    notasss = float(input(f"Digite a nota {notass + 1}: "))

    notas += notasss
    notassss = notas / 5

print("A media das notas é ", notassss)

'''

# exercício 63 ------------------------------------------------------------------------------------------ #

'''

senha = 1706

login = int(input("Digite a senha: "))

while login != senha:
    login = int(input("Acesso negado. Digite a senha novamente: "))

print("Acesso permitido")

'''
    
# exercício 64 ------------------------------------------------------------------------------------------ #

'''

numero = int(input("Digite um número inteiro positivo: "))

while numero <= 0:
    numero = int(input("Número negativo. Digite um número inteiro positivo: "))

print("Número positivo:", numero)

'''

# exercício 65 ------------------------------------------------------------------------------------------ #

'''

while True:
    print("1 - Dizer olá")
    print("2 - Mostrar uma mensagem")
    print("0 - Sair")

    menu = int(input("Escolha uma opção: "))
    if menu == 1:
        print("Olá")
    elif menu == 2:
        print("Mensagem")
    elif menu == 3:
        print("Saiu ")
        break
    else:
        print("Tente novamente")
        
'''

# exercício 66 ------------------------------------------------------------------------------------------ #

'''

soma = 0 

while True:
    numero = float(input("Digite o número (ou 0 para sair): "))

    if numero == 0:
        break
    soma += numero

print("A soma dos numeros digitados é ", soma)

'''

# exercício 67 ------------------------------------------------------------------------------------------ #

'''

notas1 = 0 
notas2 = 0

while True:
    notas3 = float(input("Digite notas de 0 à 10 (ou -1 para sair): "))

    if notas3 == -1:
        break
    if notas3 <0 or notas3 >10:
        print("Insira uma nota valida")

    notas1 += notas3
    notas2 += 1

print ("A media das notas é ", notas1/notas2)

'''

# exercício 68 ------------------------------------------------------------------------------------------ #

'''

numero_secreto = 22

while True:
    palpite = int(input("Fale um palpite "))

    if palpite == numero_secreto:
        print("Você acertou, mas você é Bolsonaro?")
        break
    elif palpite < numero_secreto:
        print("O numero é maior")
    else:
        print("O numero é menor")
        
'''

# exercício 69 ------------------------------------------------------------------------------------------ #

'''

numero = int(input("Digite um número inteiro maior que 1: "))

divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print("É primo!")
else:
    print("Não é primo!")
    
'''

# exercício 70 ------------------------------------------------------------------------------------------ #

'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

for numero in range(numero1, numero2 + 1):
    if numero > 1:
        divisores = 0

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores += 1

        if divisores == 2:
            print(numero)
            
'''