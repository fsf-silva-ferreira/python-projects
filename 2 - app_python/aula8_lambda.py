# Lambda é uma função anônima
# Eficiente para funções com uma única linha
# Não é utilizado para soluções complexas
contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print(soma(5, 10))
print(subtracao(10, 5))

#Dicionário de funções lâmbda
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

#Imprimindo a classe 'dict'
print(type(calculadora))

#Chamadas do dicionário
soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']

#Imprimindo valores das funções do dicionário
print('A soma é {}'.format(soma(10, 5)))
print('A diferença ou o resto é {}'.format(subtracao(10, 5)))
print('O produto é {}'.format(multiplicacao(10, 5)))
print('O quociente é {}'.format(divisao(10, 5)))

