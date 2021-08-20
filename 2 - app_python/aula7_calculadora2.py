#Função: Retorna valor
#Método: Não retorna valor
class Calculadora:
    #O método ini não é obrigatório
    # def __init__(self):
    #     #o init não pode ficar vazio, por coloca-se o pass
    #     pass

    def soma(self,valor_a,valor_b):
        return valor_a + valor_b

    def subtracao(self,valor_a,valor_b):
        return valor_a - valor_a

    def multiplicacao(self,valor_a,valor_b):
        return valor_a * valor_b

    def divisao(self,valor_a,valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.valor_a)
print(calculadora.valor_b)

print(calculadora.soma(10,2))
print(calculadora.subtracao(5,3))
print(calculadora.divisao(100,2))
print(calculadora.multiplicacao(10,5))

# print(soma(1,2))
# print(soma(3,25))
# print(subtracao(10,2))
# print(multiplicacao(10,2))
# print(divisao(10,2))
