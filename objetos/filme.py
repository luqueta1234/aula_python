class Filme:
    titulo = "Sem nome"
    genero = "Drama"
    duracao = 120

filme1 = Filme()
filme1.titulo = "Inception"
filme1.duracao = 148

filme2 = Filme()
filme2.titulo = "Bladerunner 2049"
filme2.genero = "Ficção científica"
filme2.duracao = 150

print(f"\nNome do filme: {filme1.titulo} \nGênero: {filme1.genero}\nDuração: {filme1.duracao}\n")
print(f"Nome do filme: {filme2.titulo} \nGênero: {filme2.genero}\nDuração: {filme2.duracao}\n")