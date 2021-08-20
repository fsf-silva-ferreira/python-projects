#Arquivo aulaDois.py

#Lê dados digitados
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

#Realiza operações aritméticas
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#Armazena o resultados de todas as operações em resultado
resultado = ('Soma com format: {soma}. '
      '\nSubtração: {sub}. '
      '\nMultiplicação: {mult}.'
      '\nDivisão: {div}.'
      '\nResto: {resto}.'.
      format(
        soma=soma,
        sub=subtracao,
        mult=multiplicacao,
        div=int(divisao),
        resto=resto))

#Imprime o resultado
print(resultado)