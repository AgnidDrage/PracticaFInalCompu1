from tema_musical import TemaMusical, EmptyError
from lista_musical import ListaMusical

tema1 = TemaMusical('1', 'Tema 1', 120, 'Interprete 1')
tema2 = TemaMusical('2', 'Tema 2', 240, 'Interprete 2')
tema3 = TemaMusical('3', 'Tema 3', 360, 'Interprete 3')
tema4 = TemaMusical('4', 'Tema 4', 480, 'Interprete 4')

lista = ListaMusical()

lista.add(tema1)
print(lista)

lista.update(tema2, tema2.codigo)
#lista.update(tema4, tema4.codigo)



print(lista)
