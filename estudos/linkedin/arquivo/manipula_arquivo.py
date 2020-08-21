import os
from os import path
import shutil


def copia_arquivo():
    if path.exists("novo_arquivo.txt"):
        path_atual = path.realpath("novo_arquivo.txt")
        novo_path = path_atual + ".bkp"
        shutil.copy(path_atual, novo_path)

        shutil.copystat(path_atual, novo_path)

copia_arquivo()

def renomear_arquivo():
    if path.exists("novo_arquivo.txt.bkp"):
        os.rename("novo_arquivo.txt.bkp", "Arquivo_alterado.txt")

renomear_arquivo()