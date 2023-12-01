class Livro:
    def __init__(self, titulo, autor, paginas, isbn):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn

    def mostrar_titulo(self):
        return f'O título do livro é {self.titulo}'

    def mostrar_autor(self):
        return f'O autor do livro é {self.autor}'

    def mostrar_paginas(self):
        return f'O livro tem {self.paginas} páginas'

    def mostrar_isbn(self):
        return f'O ISBN do livro é {self.isbn}'

livro1 = Livro('Fundação', 'Isaac Asimov', 250, 9783161484100)

print(livro1.mostrar_titulo())
print(livro1.mostrar_autor())
print(livro1.mostrar_paginas())
print(livro1.mostrar_isbn())