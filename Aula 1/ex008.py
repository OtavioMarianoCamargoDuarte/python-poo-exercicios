'''
Exercício 08 - Sistema de Pedidos

Agora vamos aumentar um nível.

Classe Produto

Cada produto deve possuir:

nome
preço

Além disso, deve ter um método para mostrar seus dados.

Classe Pedido

Cada pedido deve possuir:

número do pedido
uma lista de produtos

Além disso, deve possuir métodos para:

adicionar produto
listar produtos
calcular valor total do pedido

Crie os seguintes produtos:

Mouse - R$ 50
Teclado - R$ 120
Monitor - R$ 800

Crie um pedido:

Pedido 1

Adicione os três produtos.

Depois:

Liste todos os produtos.
Mostre o valor total do pedido.

Exemplo de saída:

Pedido 1

Mouse - R$ 50
Teclado - R$ 120
Monitor - R$ 800

Total: R$ 970
'''

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_dados(self):
        print(f'Produto: {self.nome} // Preço: R$ {self.preco:.2f}')


class Pedido:
    def __init__(self, num_pedido):
        self.num_pedido = num_pedido
        self.lista_produtos = []

    def adicionar_produto_ao_pedido(self, produto):
        self.lista_produtos.append(produto)

    def listar_produtos(self):
        print(f"\n{self.num_pedido}")
        print("-" * len(self.num_pedido))

        for produto in self.lista_produtos:
            produto.mostrar_dados()

    def calcular_valor_pedido(self):
        valor_final = 0

        for produto in self.lista_produtos:
            valor_final += produto.preco

        return valor_final

# Criação do pedido
pedido1 = Pedido('Pedido 1')

# Criação do produto
produto1 = Produto('Mouse', 50)
produto2 = Produto('Teclado', 120)
produto3 = Produto('Monitor', 800)

# Adicionando produtos no pedido
pedido1.adicionar_produto_ao_pedido(produto1)
pedido1.adicionar_produto_ao_pedido(produto2)
pedido1.adicionar_produto_ao_pedido(produto3)

# Listando produtos
pedido1.listar_produtos()

# Calculando valor final
pedido1.calcular_valor_pedido()

total = pedido1.calcular_valor_pedido()

print(f"\nTotal: R$ {total:.2f}")


