# exercício 124 ----------------------------------------------------------------------------------------- #

'''

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

personagem = (nome, idade)

print(personagem)

'''

# exercício 125 ----------------------------------------------------------------------------------------- #

'''

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

pessoa_1 = Pessoa("Gaby", 16)
pessoa_2 = Pessoa("Davi", 17)

print(pessoa_1.nome, pessoa_1.idade)
print(pessoa_2.nome, pessoa_2.idade)

'''

# exercício 126 ----------------------------------------------------------------------------------------- #

'''

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Oii, meu nome é {self.nome} e tenho {self.idade} anos.")


pessoa_1 = Pessoa("Gaby", 16)
pessoa_2 = Pessoa("Davi", 17)

pessoa_1.apresentar()
pessoa_2.apresentar()

'''

# exercício 127 ----------------------------------------------------------------------------------------- #

'''

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto_1 = Produto("Creme de Pentear", 45.99)
produto_2 = Produto("Reparador de Pontas", 25.99)
produto_3 = Produto("Gelatina Capilar", 35.00)

print("Nome:", produto_1.nome, "- Preço:", produto_1.preco)
print("Nome:", produto_2.nome, "- Preço:", produto_2.preco)
print("Nome:", produto_3.nome, "- Preço:", produto_3.preco)

'''

# exercício 128 ----------------------------------------------------------------------------------------- #

'''

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar(self):
        print(f"Produto: {self.nome} - Preço: R$ {self.preco:.2f}")

    def aplicar_desconto(self, percentual):
        self.preco = self.preco - (self.preco * percentual / 100)

produto_1 = Produto("Creme de Pentear", 45.99)
produto_2 = Produto("Reparador de Pontas", 25.99)
produto_3 = Produto("Gelatina Capilar", 35.00)

desconto = float(input("Digite o percentual de desconto: "))

produto_1.aplicar_desconto(desconto)
produto_2.aplicar_desconto(desconto)
produto_3.aplicar_desconto(desconto)

produto_1.mostrar()
produto_2.mostrar()
produto_3.mostrar()

'''
        
# exercício 129 ----------------------------------------------------------------------------------------- #

'''

class Conta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo 

    def depositar_valor(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado. Saldo:", self.saldo)
        else:
            print("Valor de depósito inválido.")

    def sacar_valor(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor 
            print("Saque realizado. Saldo:", self.saldo)
        else:
            print("Valor inválido ou saldo insuficiente.")

conta = Conta_Bancaria("Gaby", 170.00)

while True:
    print("1 Depositar - 2 Sacar - 0 Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        conta.depositar_valor(valor)

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        conta.sacar_valor(valor)
        
    elif opcao == "0":
        break

    else:
        print("Opção inválida.")

print("Títular:", conta.titular)
print("Saldo final:", conta.saldo)

'''

# exercício 130 ----------------------------------------------------------------------------------------- #

'''
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

Gaby = Aluno('Gaby', [7, 8, 9])
Davi = Aluno('Davi', [6, 7, 8])

print(Gaby.calcular_media())
print(Davi.calcular_media())

'''

# exercício 131 ----------------------------------------------------------------------------------------- #

'''

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 6:
            return "Aprovado"
        else:
            return "Reprovado"


aluno_1 = Aluno("Gaby", [7, 8, 9])
aluno_2 = Aluno("Davi", [6, 7, 8])

print(aluno_1.calcular_media())
print(aluno_2.calcular_media())

print(aluno_1.verificar_situacao())
print(aluno_2.verificar_situacao())

'''

# exercício 132 ----------------------------------------------------------------------------------------- #

'''

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_perimetro(self):
        soma = self.altura + self.largura
        perimetro = soma * 2
        print(perimetro)

    def calcular_area(self):
        area = self.altura * self.largura
        print(area)


retangulo = Retangulo(20, 10)

retangulo.calcular_area()
retangulo.calcular_perimetro()

'''

# exercício 133 ----------------------------------------------------------------------------------------- #

'''

class Carro:
    def __init__(self, modelo, velocidade_atual, velocidade_maxima):
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual
        self.velocidade_maxima = velocidade_maxima

    def acelerar(self, valor):
        if self.velocidade_atual >= 0 and valor > 0 and self.velocidade_atual + valor <= self.velocidade_maxima:
            self.velocidade_atual += valor
            print("Acelerou", valor, "\nVelocidade atual:", self.velocidade_atual)
        else:
            print("Ação inválida!")

    def frear(self, valor):
        if self.velocidade_atual > 0 and valor > 0 and self.velocidade_atual - valor >= 0:
            self.velocidade_atual -= valor
            print("Freou", valor, "\nVelocidade atual:", self.velocidade_atual)
        else:
            print("Ação inválida!")


carro = Carro("Honda Civic G10", 20, 480)

while True:
    print("1 Acelerar -  2 Frear - 0 Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        valor = int(input("Quanto você quer acelerar? "))
        carro.acelerar(valor)

    elif opcao == "2":
        valor = int(input("Quanto você quer frear? "))
        carro.frear(valor)

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")

print("Modelo:", carro.modelo)
print("Velocidade final:", carro.velocidade_atual)

'''

# exercício 134 ----------------------------------------------------------------------------------------- #

'''

class Livro:
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor 
        self.disponivel = disponivel

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar(self, livro):
        livro.disponivel = True
        self.livros.append(livro)
        print(livro, "Livro adionado com sucesso.")

    def listar(self):
        for livro in self.livros:
            print(livro.titulo)
        
    def emprestar(self, emprestimo):
        if emprestimo in self.livros:
            posicao = self.livros.index(emprestimo)
            self.livros[posicao].disponivel = False
            print(emprestimo.titulo, "Livro emprestado com sucesso.")
        else:
            print("Livro não está cadastrado.")

    def devolver(self, devolvido):
        if devolvido in self.livros:
            posicao = self.livros.index(devolvido)
            self.livros[posicao].disponivel = True
        else:
            print("Esse livro não está cadastrado.")

Coraline = Livro("Coraline e o Mundo Secreto", "Neil Gaiman", True)
Harry_Potter = Livro("Prisioneiro de Azkaban", "J. K. Rowling", True)
Casa_Monstro = Livro("A Casa Monstro", "Gil Kenan", True)

La_biblio = Biblioteca()

La_biblio.adicionar(Coraline)
La_biblio.listar()
La_biblio.emprestar(Coraline)
La_biblio.devolver(Coraline)

'''

# exercício 135 ----------------------------------------------------------------------------------------- #