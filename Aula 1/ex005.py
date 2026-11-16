'''
Enunciado:

Crie uma classe chamada Turma.

Requisitos:

A turma deve possuir uma lista chamada alunos.
Crie um método chamado adicionar_aluno.
Esse método deve receber um objeto do tipo Pessoa e adicioná-lo na lista.
Crie três objetos Pessoa.
Crie uma turma.
Adicione os três alunos na turma.
Utilize um for para mostrar o nome de todos os alunos da turma.
'''

class Pessoa:

    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def mostrar_alunos(self):
        print(f'==== {self.nome_turma} ====')
        for aluno in self.alunos:
            print(f'{aluno.nome}')  



t = Turma('1ªA')

a1 = Pessoa('Otavio')
t.adicionar_aluno(a1)

a2 = Pessoa('Maria')
t.adicionar_aluno(a2)

a3 = Pessoa('Jonas')
t.adicionar_aluno(a3)

t.mostrar_alunos()

