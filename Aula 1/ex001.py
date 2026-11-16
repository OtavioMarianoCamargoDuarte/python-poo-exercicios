'''
Exercício 01 - Primeira Classe

Crie uma classe chamada Pessoa.

Requisitos
A classe deve possuir um atributo para armazenar o nome da pessoa.
Ao criar o objeto, o nome deve ser informado pelo construtor (__init__).
Crie um objeto chamado p1.
O nome da pessoa deve ser "Otavio".
Ao final, exiba o nome armazenado no objeto.
Resultado esperado

Algo deve ser exibido na tela mostrando o nome da pessoa.
'''

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def mostrar_nome(self):
        print(f'Meu nome é {self.nome}')

p1 = Pessoa('Otavio')

p1.mostrar_nome()
