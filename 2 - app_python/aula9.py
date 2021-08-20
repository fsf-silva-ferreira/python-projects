#Recomendado colocar o import no topo do arquivo
#Assim, ele pode ser utilizado por qualquer método ou função
import shutil


def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto + '\n')
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto + '\n')
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    # O método read não tem parâmetro
    # O nome do arquivo já foi passado como parâmetro do método open
    texto = arquivo.read()
    print('Conteúdo do arquivo:\n{}'.format(texto))
    return texto


def media_notas(nome_arquivo):
    lista_media = []
    print('1 - Ler arquivo de notas')
    aluno_nota = ler_arquivo(nome_arquivo)
    aluno_nota = aluno_nota.split('\n')
    print('2 - Aluno e notas em cada posição da lista: {} '.format(aluno_nota))
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #Função lambda para calcular a média de cada aluno
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arquivo(origem, destino):
    #Se o destino tiver apenas o diretório, copia com o mesmo nome do arquivo de origem
    shutil.copy(origem, destino)


def move_arquivo(origem, destino):
    #Se o destino tiver apenas o diretório, copia com o mesmo nome do arquivo de origem
    shutil.move(origem, destino)


if __name__ == '__main__':
    # diretorio = 'C:/python-projects/app_python/test.txt'
    # escrever_arquivo(diretorio, 'Primeira linha. \n')
    # atualizar_arquivo(diretorio, 'Segunda linha. \nTerceira linha. \n')
    # ler_arquivo(diretorio)

    # escrever_arquivo('notas.txt', 'Primeira linha. \n')
    # aluno = 'Cesar,7,9,3,8'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('notas.txt')

    nome_arquivo_notas = 'notas.txt'
    medias_origem = 'medias.txt'
    medias_destino = 'C:/python-projects/app_python/dir_copia/medias_copia.txt'
    dir_move = 'C:/python-projects/app_python/dir_move/medias_move.txt'

    lista_media = media_notas(nome_arquivo_notas)
    print('3 - Lista com nomes dos alunos e médias: {}'.format(lista_media))
    #Grava em arquivo nome do aluno e média
    for media in lista_media:
        atualizar_arquivo(medias_origem, str(media))
    print('4 - Ler arquivo de médias')
    ler_arquivo(medias_origem)
    copia_arquivo(medias_origem, medias_destino)
    move_arquivo(medias_origem, dir_move)

    teste = 'oiuoiu7uujejejej'.split('\n')
    print(teste)
