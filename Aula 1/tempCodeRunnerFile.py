'''
Exercício 09 - Cliente, Pedido e Produto

Agora teremos 3 classes.

Classe Produto

Atributos:

nome
preco

Método:

mostrar_dados()
Classe Pedido

Atributos:

numero
lista de produtos

Métodos:

adicionar_produto()
listar_produtos()
calcular_total()
Classe Cliente

Atributos:

nome
lista de pedidos

Métodos:

adicionar_pedido()
listar_pedidos()
Cenário

Crie:

Cliente
Otavio
Pedido 1

Produtos:

Mouse - R$ 50
Teclado - R$ 120
Pedido 2

Produtos:

Monitor - R$ 800
Headset - R$ 200
'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_dados(self):
        print(f'Produto: {self.nome} // Preço: R$ {self.preco:.2f}')


class Pedido:
    def __init__(self, numero):
        self.numero = numero
        self.lista_de_produtos = []

    def adicionar_produto(self, produto):
        if produto not in self.lista_de_produtos:
            self.lista_de_produtos.append(produto) 
        else:
            print('Já contem o produto na lista.')

    def listar_produtos(self):
        for produto in self.lista_de_produtos:
            produto.mostrar_dados()

    def calcular_total(self):
        valor_final = 0

        for produto in self.lista_de_produtos:
            valor_final += produto.preco

        return valor_final

produto1 = Produto('Mouse', 50)
produto2 = Produto('Teclado', 120)
produto3 = Produto('Monitor', 800)
produto4 = Produto('Headset', 200)

pedido1 = Pedido('Pedido 1')

pedido1.adicionar_produto(produto1)
pedido1.adicionar_produto(produto2)

pedido1.listar_produtos()

pedido1.calcular_total()
total = pedido1.calcular_total()

print(f'Total: R$ {total:.2f}')

pedido2 = Pedido('Pedido 2')

pedido2.adicionar_produto(produto3)
pedido2.adicionar_produto(produto4)

pedido2.listar_produtos()

pedido2.calcular_total()
total2 = pedido2.calcular_total()

print(f'Total: R$ {total2:.2f}')

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_pedidos = []

    def adicionar_pedidos(self, lista):
        if lista not in self.lista_de_pedidos:
            self.lista_de_pedidos.append(lista)
        else:
            print('Já contem o pedido na lista.')

    def listar_pedidos(self):
        pass

cliente1 = Cliente('Otavio')