import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def criar_zip_modo_1():
    shutil.make_archive("Arquivo_compactado", "zip", "/home/serlus/repositorios/Learning/estudos/linkedin")


# criar_zip_modo_1()

def criar_zip_modo_2():
    with ZipFile("arquivo_zip_modo2.zip", "w") as novo_zip:
        novo_zip.write("novo_arquivo.txt")

# criar_zip_modo_2()

def deleta_arquivo():
    os.remove("arquivo_zip_modo2.zip")

deleta_arquivo()