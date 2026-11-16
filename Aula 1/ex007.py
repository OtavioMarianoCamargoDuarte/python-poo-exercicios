class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_dados(self):
        print(f"Título: {self.titulo} | Autor: {self.autor}")


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print("=" * len(self.nome))
        print(self.nome)
        print("=" * len(self.nome))

        for livro in self.livros:
            livro.mostrar_dados()


# Criação da biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# Criação dos livros
livro1 = Livro("Harry Potter", "J. K. Rowling")
livro2 = Livro("O Hobbit", "J. R. R. Tolkien")
livro3 = Livro("Dom Casmurro", "Machado de Assis")

# Adicionando livros na biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Exibindo os livros cadastrados
biblioteca.listar_livros()