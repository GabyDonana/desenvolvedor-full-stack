# exercício 16 ------------------------------------------------------------------------------------------ #

'''

lado = float(input("Digite o valor do lado do quadrado: "))

lado = lado * lado

print ("A área do quadrado é:", lado)

''' 

# exercício 17 ------------------------------------------------------------------------------------------ #

'''

largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = largura * altura

print("A área do retângulo é:", area)

'''

# exercício 18 ------------------------------------------------------------------------------------------ #

'''

base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

area = (base * altura) / 2

print("A área do triângulo é:", area)

'''

# exercício 19 ------------------------------------------------------------------------------------------ #

'''

raio = float(input("Digite o valor do raio do círculo: "))

area = 3.14 * (raio ** 2)

print("A área do círculo é:", area)

'''

# exercício 20 ------------------------------------------------------------------------------------------ #

'''

altura = float(input("Digite a altura do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))

perimetro = (altura * 2) + (largura * 2)

print("O perímetro do retângulo é:", perimetro)

'''

# exercício 21 ------------------------------------------------------------------------------------------ #

'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: ")) 
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("A média das notas é:", media)

'''

# exercício 22 ------------------------------------------------------------------------------------------ #

'''

valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

salario = valor_hora * horas_trabalhadas

print("O salário do funcionário é:", salario)

'''

# exercício 23 ------------------------------------------------------------------------------------------ #

'''

salario = float(input("Digite o salário do funcionário: "))
aumento = salario * 10 / 100

novo_salario = salario + aumento

print("Salário original:", salario)
print("Valor do aumento:", aumento)
print("Novo salário:", novo_salario)

'''

# exercício 24 ------------------------------------------------------------------------------------------ #

'''

preco = float(input("Digite o preço do produto: "))
desconto = preco * 5 / 100

preco_final = preco - desconto

print("Valor do desconto:", desconto)
print("Preço final:", preco_final)

'''

# exercício 25 ------------------------------------------------------------------------------------------ #

'''

valor = float(input("Digite o valor do produto: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

valor_parcela = valor / parcelas

print("Valor de cada parcela:", valor_parcela)

'''

# exercício 26 ------------------------------------------------------------------------------------------ #

'''

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print("Seu Índice de Massa Corporal (IMC) é: ", f"{imc:.2f}")

'''

# exercício 27 ------------------------------------------------------------------------------------------ #

'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 * 2 + nota2 * 3) / 5

print("A média ponderada das notas é:", media)

'''

# exercício 28 ------------------------------------------------------------------------------------------ #

'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

quociente = numero1 // numero2
resto = numero1 % numero2

print("O quociente da divisão é:", quociente)
print("O resto da divisão é:", resto)

'''

# exercício 29 ------------------------------------------------------------------------------------------ #

'''

numero = int(input("Digite um número: "))

antecessor = numero - 1
sucessor = numero + 1

print("o antecessor é:", antecessor)
print("o sucessor é:", sucessor)

'''

# exercício 30 ------------------------------------------------------------------------------------------ #

'''

base = int(input("Digite o valor da base para a potenciação: "))
expoente = int(input("Digite o valor do expoente para a potenciação: "))

resultado = base ** expoente

print("O resultado da potenciação é:", resultado)

'''