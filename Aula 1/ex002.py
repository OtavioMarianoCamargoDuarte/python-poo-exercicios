'''
Exercício 02 - Alterando um atributo

Agora vamos subir um degrau bem pequeno.

Enunciado

Crie uma classe chamada Pessoa.

Requisitos
A classe deve armazenar o nome da pessoa.
Crie um método chamado trocar_nome.
Esse método deve receber um novo nome e substituir o nome atual.
Crie um objeto chamado p1 com o nome "Otavio".
Utilize o método para trocar o nome para "Carlos".
Exiba o nome após a alteração.
Resultado esperado

Ao final da execução, deve ser exibido:

Carlos
'''

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def trocar_nome(self, novo_nome):
        self.nome = novo_nome

    def mostrar_nome(self):
        print(f'Nome: {self.nome}')

p1 = Pessoa('Otavio')

p1.trocar_nome('Carlos')

p1.mostrar_nome()

