a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Você digitou o valor errado. Primeiro Bimestre: '))

b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Você digitou o valor errado. Segundo Bimestre: '))

c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('Você digitou o valor errado. Terceiro Bimestre: '))
    
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('Você digitou o valor errado. Quarto Bimestre: '))

media = (a + b + c + d) / 4

print('Média: {}'.format(media))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada')

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')


# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# #Verifica o maior valor
# if a > b and a > c:
#     print('O maior número é {}.'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}.'.format(b))
# else:
#     print('O maior número é {}.'.format(c))
#
# print('Final do programa')