    """foi feita apenas uma conexão com uma página
    mas pode ser feito mais coisas.
    """
import urllib.request


def conecta_internet():
    obj_url = urllib.request.urlopen("http://www.google.com")

    if obj_url.getcode() == 200:
        dados = obj_url.read()
        print(dados)

conecta_internet()