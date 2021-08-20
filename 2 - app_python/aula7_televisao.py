class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:  # Ou if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

print('Arquivo chamado: {}'.format(__name__))

#Com o if abaixo, o bloco só é executado se for chamado de dentro do próprio arquivo
#se for chamado pelo prompt como um módulo, não faz nada
if __name__ == '__main__':
    televisao = Televisao()

    print('Televisão ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão ligada: {}'.format(televisao.ligada))

    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisão ligada: {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))
