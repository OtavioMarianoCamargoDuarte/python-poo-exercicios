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
        print(f"Produto: {self.nome} | Preço: R$ {self.preco:.2f}")


class Pedido:
    def __init__(self, numero):
        self.numero = numero
        self.produtos = []

    def adicionar_produto(self, produto):
        if produto not in self.produtos:
            self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            produto.mostrar_dados()

    def calcular_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.preco

        return total


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        if pedido not in self.pedidos:
            self.pedidos.append(pedido)

    def listar_pedidos(self):
        print(f"\nCliente: {self.nome}")
        print("=" * 40)

        for pedido in self.pedidos:
            print(f"\n{pedido.numero}")
            print("-" * len(pedido.numero))

            pedido.listar_produtos()

            total = pedido.calcular_total()

            print(f"Total: R$ {total:.2f}")


# Produtos
produto1 = Produto("Mouse", 50)
produto2 = Produto("Teclado", 120)
produto3 = Produto("Monitor", 800)
produto4 = Produto("Headset", 200)

# Pedido 1
pedido1 = Pedido("Pedido 1")
pedido1.adicionar_produto(produto1)
pedido1.adicionar_produto(produto2)

# Pedido 2
pedido2 = Pedido("Pedido 2")
pedido2.adicionar_produto(produto3)
pedido2.adicionar_produto(produto4)

# Cliente
cliente = Cliente("Otavio")

cliente.adicionar_pedido(pedido1)
cliente.adicionar_pedido(pedido2)

# Exibição
cliente.listar_pedidos()