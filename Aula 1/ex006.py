'''
Exercício 06 - Evitando alunos duplicados

Altere a classe Turma para que:

um mesmo aluno não possa ser adicionado duas vezes;
se tentar adicionar um aluno que já está na lista, exiba:

Aluno já está cadastrado.

Exemplo

t.adicionar_aluno(a1)
t.adicionar_aluno(a1)

Resultado:

Aluno já está cadastrado.
'''

class Pessoa:

    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            print(f'Aluno adicionado a {self.nome_turma} com sucesso.')
        else:
            print(f'Aluno já cadastrado na {self.nome_turma}')

    def mostrar_alunos(self):
        print(f'==== {self.nome_turma} ====')
        for aluno in self.alunos:
            print(f'{aluno.nome}')  



t = Turma('1ªA')

a1 = Pessoa('Otavio')
t.adicionar_aluno(a1)
t.adicionar_aluno(a1)

t.mostrar_alunos()