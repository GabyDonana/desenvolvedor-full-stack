# exercício 31 ------------------------------------------------------------------------------------------ #

'''

numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
    
'''

# exercício 32 ------------------------------------------------------------------------------------------ #

'''

numero = int(input("Digite sua idade: "))

if numero >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
    
'''

# exercício 33 ------------------------------------------------------------------------------------------ #

'''

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
    
'''

# exercício 34 ------------------------------------------------------------------------------------------ #

'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro número é maior.")
else:
    print("O segundo número é maior.")
    
'''

# exercício 35 ------------------------------------------------------------------------------------------ #

'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O primeiro número é o maior.")
elif numero2 > numero1 and numero2 > numero3:
    print("O segundo número é o maior.")
else:
    print("O terceiro número é o maior.")
    
'''

# exercício 36 ------------------------------------------------------------------------------------------ #

'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 < numero2 and numero1 < numero3:
    print("O primeiro número é o menor.")
elif numero2 < numero1 and numero2 < numero3:
    print("O segundo número é o menor.")
else:
    print("O terceiro número é o menor.")
    
'''

# exercício 37 ------------------------------------------------------------------------------------------ #

'''

media = float(input("Digite a média do aluno: "))

if media >= 6:
    print("aprovado.")
elif media < 6:
    print("reprovado.")
    
'''

# exercício 38 ------------------------------------------------------------------------------------------ #

'''

media = float(input("Digite a média do aluno: "))

if media >= 7:
    print("Aprovado.")
elif media >=5:
    print("Recuperação.")
else:
    print("Reprovado.")
    
'''

# exercício 39 ------------------------------------------------------------------------------------------ #

'''

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Criança.")
elif idade >= 13 and idade <= 17:
    print("Adolescente.")
elif idade >= 18 and idade <= 59:
    print("Adulto.")
elif idade >= 60:
    print("Idoso.")
    
'''

# exercício 40 ------------------------------------------------------------------------------------------ #

'''

senha_correta = 1706

senha = int(input("Digite a senha: "))

if senha == senha_correta:
    print("Acesso permitido.")
else:
    print("Acesso negado.")
    
'''

# exercício 41 ------------------------------------------------------------------------------------------ #

'''

usuario = "gaby"
senha = 1706

usuario_digitado = input("Digite o usuário: ")
senha_digitada = int(input("Digite a senha: "))

if usuario_digitado == usuario and senha_digitada == senha:
    print("Acesso permitido.")
else:
    print("Acesso negado.")
    
'''

# exercício 42 ------------------------------------------------------------------------------------------ #

'''numero = int(input("Digite um número: "))

if numero % 5 == 0:
    print("O número é multiplo de 5.")
else:
    print("O número não é multiplo de 5.")'''

# exercício 43 ------------------------------------------------------------------------------------------ #

'''numero = int(input("Digite um número: "))

if numero % 5 == 0 and numero % 3 == 0:
    print("É divisível por 3 e por 5.")
else:
    print("Não é divisível por 3 e por 5.")'''

# exercício 44 ------------------------------------------------------------------------------------------ #

'''ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")'''

# exercício 45 ------------------------------------------------------------------------------------------ #

'''valor = float(input("Digite o valor da compra: "))

if valor <= 200:
    desconto = valor * 0.10
    valor_final = valor - desconto
    
    print("O valor final da compra é: R$", valor_final)'''

# exercício 46 ------------------------------------------------------------------------------------------ #

'''valor = float(input("Digite o valor da compra: "))

if valor <= 150:
    total = valor
else:
    total = valor + 20 

    print("O valor total da compra é: R$", total)'''

# exercício 47 ------------------------------------------------------------------------------------------ #

'''numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
    print("O resultado da soma é:", resultado)

elif operacao == "-":
    resultado = numero1 - numero2
    print("O resultado da subtração é:", resultado)

elif operacao == "*":
    resultado = numero1 * numero2
    print("O resultado da multiplicação é:", resultado)

elif operacao == "/":
    if numero2 == 0:
        print("Não é possível dividir por zero.")

    else:
        resultado = numero1 / numero2
        print("O resultado da divisão é:", resultado)'''

# exercício 48 ------------------------------------------------------------------------------------------ #

'''lado1 = int(input("Digite um número "))
lado2 = int(input("Digite outro número "))
lado3 = int(input("Digite mais um número "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os números podem formar um triângulo.")
else: 
    print("Os números não podem formar um triângulo.")'''

# exercício 49 ------------------------------------------------------------------------------------------ #

'''lado1 = int(input("Digite um número inteiro "))
lado2 = int(input("Digite outro número inteiro "))
lado3 = int(input("Digite mais um número inteiro "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os números não podem formar um triângulo.")'''

# exercício 50 ------------------------------------------------------------------------------------------ #

'''salario = float(input("Digite seu salário mensal: R$ "))

if salario <= 2000.00:
    imposto = 0.0

elif salario <= 4000.00:
    imposto = 0.10

else:
    imposto = 0.20

valor_imposto = salario * imposto
salario_restante = salario - valor_imposto

print(f"Imposto aplicado: {imposto * 100:.0f}%")
print(f"Valor do imposto: R$ {valor_imposto:.2f}")
print(f"Salário restante: R$ {salario_restante:.2f}")'''