lista = [12, 10, 7, 5]
animais = ['cachorro','gato','elefante','lobo','arara']
#Tupla x Lista
#Tupla = Imutável
#Lista = Mutável

tupla = ('1',10,12,14)
#print(tupla[3]) ERRO

tupla_animais = tuple(animais)
print('Tamanho da tupla: {}'.format(str(len(tupla_animais))))
print('Classe da tupla: {}'.format(type(tupla_animais)))
print('Elementos da tupla: {}'.format(str(tupla_animais)))

print('\n')

lista_numerica = list(tupla)
print('Tamanho da lista: {}'.format(str(len(lista_numerica))))
print('Classe da lista: {}'.format(type(lista_numerica)))
lista_numerica[0] = 100
print('Elementos da lista {}.'.format(str(lista_numerica)))

#print(animais[1])

# lista.sort();
# animais.sort();
#
# print(lista)
# print(animais)
#
# animais.reverse()
# print(animais)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

#print(min(animais))

# nova_lista = animais * 3
# print(nova_lista)

# print(animais)
# if 'lobo' in animais:
#     print('Existe um lobo na lista')
# else:
#     print('Não existe um lobo na lista. Será incluído:')
#     animais.append('lobo')
# print(animais)

# animais.pop()
# print(animais)

# animais.pop(0)
# print(animais)

# animais.remove('elefante')
# print(animais)