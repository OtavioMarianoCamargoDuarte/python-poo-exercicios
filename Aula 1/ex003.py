'''
Exercício 03 - Duas Pessoas

Agora vamos começar a trabalhar com mais de um objeto.

Enunciado

Crie uma classe chamada Pessoa.

Requisitos:

A classe deve armazenar o nome da pessoa.
Crie um método chamado mostrar_nome.
Crie dois objetos:
p1 com o nome "Otavio"
p2 com o nome "Maria"
Mostre o nome de cada pessoa utilizando o método mostrar_nome.
Resultado esperado

Deve aparecer algo semelhante a:

Otavio
Maria
'''

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def mostrar_nome(self):
        print(self.nome)

p1 = Pessoa('Otavio')
p2 = Pessoa('Maria')

p1.mostrar_nome()
p2.mostrar_nome()