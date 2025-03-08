class Livro:
    def __init__(self, titulo):
        self._titulo = titulo

    def exibirLivro(self):
        print(f"\nTítulo do livro: {self._titulo}\n")

livro1 = Livro("Título qualquer")

livro1.exibirLivro()