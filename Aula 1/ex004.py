'''
Exercício 04 - Cadastro de Pessoas

Agora vamos dar um passo importante, mas pequeno.

Enunciado

Crie uma classe chamada Pessoa.

Requisitos
A classe deve armazenar o nome da pessoa.
Crie três objetos:
p1 → "Otavio"
p2 → "Maria"
p3 → "João"
Crie uma lista chamada pessoas.
Adicione os três objetos dentro da lista.
Ao final, utilize um for para exibir o nome de todas as pessoas da lista.

Otavio
Maria
João
'''

class Pessoa:

    def __init__(self, nome):
        self.nome = nome

pessoas = []
p1 = Pessoa('Otavio')
p2 = Pessoa('Maria')
p3 = Pessoa('João')

pessoas.append(p1)
pessoas.append(p2)
pessoas.append(p3)

for pessoa in pessoas:
    print(f'Nome: {pessoa.nome}')