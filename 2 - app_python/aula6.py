#Um conjunto não tem duplicidade
conjunto1 = {1,2,3,4,5}
conjunto2 = {5,6,7,8}

#No caso de união e intersecção, a ordem não interfere no resultado
conjunto_uniao = conjunto1.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_inserseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_inserseccao))

#Na diferença,o resultado está sempre relacionado ao objeto que chama o método
conjunto_diferenca1 = conjunto1.difference(conjunto2)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

#Diferença simétrica: Oposto da intersecção
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica entre 1 e 2: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
isSubset_ab = conjunto_a.issubset(conjunto_b)
print('conjunto_a é um subconjunto de conjunto_b: {}'.format(isSubset_ab))
isSubset_ba = conjunto_b.issubset(conjunto_a)
print('conjunto_b é um subconjunto de conjunto_a: {}'.format(isSubset_ba))
isSuperset_ab = conjunto_a.issuperset(conjunto_b)
print('conjunto_a é um superconjunto de conjunto_b: {}'.format(isSuperset_ab))
isSuperset_ba = conjunto_b.issuperset(conjunto_a)
print('conjunto_b é um superconjunto de conjunto_a: {}'.format(isSuperset_ba))

lista_animais = ['gato','cachorro','gato','elefante','cachorro']
print('Lista de animais: {}'.format(lista_animais))
#Convertendo lista em conjunto
#Conversão de conjunto de volta para lista é uma maneira rápida e de baixo custo de retirar duplicados de uma lista
conjunto_animais = set(lista_animais)
print('Conjunto de animais: {}'.format(conjunto_animais))
lista_animais = list(conjunto_animais)
print('Conjunto convertido em lista: {}: '.format(lista_animais))


#Basta C ter apenas os mesmos elementos de D para ser um subconjunto
conjunto_c = {1,2,3}
conjunto_d = {1,2,3}
print('C é um subconjunto de D? {}'.format(conjunto_c.issubset(conjunto_d)))


# conjunto = {1,2,2,2,2,3,4,4,4}
# conjunto.add(5)
# conjunto.discard(2)
# print(type(conjunto))
# print(conjunto)

a = 10 / 2
b = 10 % 2
print(a, b)