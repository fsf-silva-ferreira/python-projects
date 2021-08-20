from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
#É possível retornar mais de uma função de um módulo
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5,10)
    print(calculadora.soma())

    list_palavras = ['cachorro','gato','elefante']
    total_letras = contador_letras(list_palavras)
    print('Total de letras por palavra: {}'.format(total_letras))

    print(teste())
