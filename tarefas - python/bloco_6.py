# exercício 81 ------------------------------------------------------------------------------------------ #

'''

lista_nomes = ["Vitoria", "Nicole", "Antonio", "Gaby", "Geovanna"]

for nome in lista_nomes:
    print(nome)
    
'''

# exercício 82 ------------------------------------------------------------------------------------------ #

'''
lista_nomes = []

for i in range(5):
    nomes = input("Digite um nome: ")
    lista_nomes.append(nomes)
    print(lista_nomes)
    
'''

# exercício 83 ------------------------------------------------------------------------------------------ #

'''

soma = 0
notas = [1, 2, 3, 4, 5, 6, 7]

for i in range (len(notas)):
    soma = soma + notas[i]

print(soma)

'''

# exercício 84 ------------------------------------------------------------------------------------------ #

'''

numeros = [-7, -4, -22, 100, -8]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print(maior)

'''

# exercício 85 ------------------------------------------------------------------------------------------ #

'''

numeros = [-7, -4, -22, 100, -8]
menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero

print(menor)

'''

# exercício 86 ------------------------------------------------------------------------------------------ #

'''

soma = []
lista = []

for i in range(5):
    nota = int(input("Digite a nota: "))
    lista.append(nota)
    media = sum(lista) / 5

print(media)

'''

# exercício 87 ------------------------------------------------------------------------------------------ #

'''

lista = [17, 22, 67, 4]
par = []

for i in lista:
    if i % 2 == 0:
        par.append(i)

print(par)

'''

# exercício 88 ------------------------------------------------------------------------------------------ #

'''

lista = ["Gaby", "Nicole", "Antonio"]
nome = input("Digite um nome: ")

if nome in lista:
    lista.remove(nome)
    print("Nome removido")
    print("Lista atualizada:", lista)
else:
    print("Esse nome não pertece a lista.")
    
'''

# exercício 89 ------------------------------------------------------------------------------------------ #

'''

lista = []

for i in range(5):
    produto = input("Digite o produto: ")
    lista.append(produto)

buscar_produto = input("Digite para buscar o produto: ")
if (buscar_produto in lista):
    print("Produto encontrado.")
else:
    print("Produto não encontrado.")
    
'''

# exercício 90 ------------------------------------------------------------------------------------------ #

'''

lista = []

for numeros in range(6):
    numero = input("Digite 6 números: ")
    lista.append(numero)

lista.sort()
print("Ordem crescente:" ,lista)

lista.sort(reverse=True)
print("Ordem decrescente:" ,lista)

'''

# exercício 91 ------------------------------------------------------------------------------------------ #

'''

lista = []

for numeros in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

setlista = set(lista)
print(setlista)

'''

# exercício 92 ------------------------------------------------------------------------------------------ #

'''

conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {2, 4, 6, 8, 10}

em_comum = conjunto_1 & conjunto_2
print(em_comum)

'''

# exercício 93 ------------------------------------------------------------------------------------------ #

'''

tupla_coordenadas = (5, 10)

print("X = ", tupla_coordenadas[0])
print("Y = ", tupla_coordenadas[1])

'''

# exercício 94 ------------------------------------------------------------------------------------------ #

'''

dicionário = {
    "Nome": "Gaby",
    "Idade": 16,
    "Cidade": "Uberlândia"
}

print("Meu nome é", dicionário["Nome"], "tenho", dicionário["Idade"], "anos e moro em", dicionário["Cidade"])

'''

# exercício 95 ------------------------------------------------------------------------------------------ #

'''

lista = []

aluno = input("Digite o nome do aluno: ")
for i in range(2):
    nota_aluno = int(input("Digite a nota do aluno: "))
    lista.append(nota_aluno)

dicionário = {
    "Nome": aluno,
    "Notas": nota_aluno
}

dicionário ["Média"] = (lista[0] + lista[1]) / 2
print(dicionário)

'''

# exercício 96 ------------------------------------------------------------------------------------------ #

'''

lista = []

dicionario_1 = {
    "Nome: " "maça",
    "Preço: " "7,99"
}

lista.append(dicionario_1)

dicionario_2 = {
    "Nome: " "melância",
    "Preço: " "6,99"
}

lista.append(dicionario_2)

dicionario_3 = {
    "Nome: " "melão",
    "Preço: " "9,99"
}

lista.append(dicionario_3)

print(lista)

'''

# exercício 97 ------------------------------------------------------------------------------------------ #

'''

maior_preco = 0
produto_caro = ""

lista = [
    {"Nome": "maçã", "Preço": 7.99},
    {"Nome": "melância", "Preço": 6.99},
    {"Nome": "melão", "Preço": 9.99}
]

for i in lista:
    if i["Preço"] > maior_preco:
        maior_preco = i["Preço"]
        produto_caro = i["Nome"]

print("Produto mais caro:", produto_caro)
print("Preço:", maior_preco)

'''

# exercício 98 ------------------------------------------------------------------------------------------ #

'''

agenda = {
    "Gaby": 34991022100,
    "Nicole": 34998674522,
    "Antonio": 34967226722
}

telefone = input("Digite o nome para saber o número de telefone: ")

if telefone in agenda:
    print("Telefone:", agenda[telefone])
else:
    print("Nome não encontrado na agenda.")
    
'''

# exercício 99 ------------------------------------------------------------------------------------------ #

'''

contagem = {}

frase = input("Digite uma frase: ")
frase_minuscula = frase.lower()
palavras = frase_minuscula.split()
palavras_unicas = set(palavras)

for palavra in palavras_unicas:
    contagem[palavra] = palavras.count(palavra)

print(contagem)

'''

# exercício 100 ----------------------------------------------------------------------------------------- #

'''

estoque = {
    "maçã": 22,
    "melância": 17,
    "melão": 7
}

produto = input("Digite o nome do produto: ").lower()
quantidade_retirar = int(input("Digite a quantidade a retirar: "))

if produto not in estoque:
    print("Esse produto não está cadastrado.")
elif quantidade_retirar <= 0:
    print("A quantidade deve ser positiva.")
elif quantidade_retirar > estoque[produto]:
    print("Não há quantidade suficiente para retirar.")
else:
    estoque[produto] -= quantidade_retirar
    print("Item retirado com sucesso!")
    print("Quantidade restante:", estoque[produto])

print("Estoque atualizado:", estoque)

'''