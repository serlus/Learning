from os import path
import time

    """descobrir mais sobre o q path pode fazer 
    """
def dados_arquivos():
    arquivo_existe = path.exists("novo_arquivo.txt")
    eh_diretorio = path.isdir("novo_arquivo.txt")
    path_arquivo = path.realpath("novo_arquivo.txt")
    path_relativo = path.relpath("novo_arquivo.txt")
    data_criacao = time.ctime(path.getctime("novo_arquivo.txt"))
    data_modifacao = time.ctime(path.getmtime("novo_arquivo.txt"))

    print(arquivo_existe)
    print(eh_diretorio)
    print(path_arquivo)
    print(path_relativo)
    print(data_criacao)
    print(data_modifacao)

dados_arquivos()