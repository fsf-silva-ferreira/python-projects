

try:
    lista = [1, 10]
    arquivo = open('test.txt', 'r')
    divisao = 10 / 1
    # Acessando uma posição inexistente da lista
    numero = lista[1]
    #x = a
#Colocar sempre os filhos no topo da cadeira de exceções
except ZeroDivisionError:
    # Erro de divisão por 0 tratado
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
#Encadeamento de exceções
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
#BaseException é a mãe de todas as exceções
#Gravando a mensagem de erro em "ex"
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
#Entrar no else significa que não houve nenhum erro
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando o arquivo')