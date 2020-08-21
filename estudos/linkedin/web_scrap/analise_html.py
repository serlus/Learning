from html.parser import HTMLParser


class MeuParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Tag de abertura encontrada!")
        if attrs.__len__() > 0:
            for a in attrs:
                print(" Valores encontrados: ", a[0], " = ", a[1])

    def handle_endtag(self,tag):
        print("Tag de fechamento encontrada")

    def handle_comment(self, data):
        print("Comentário encontrada")

    def handle_data(self, data):
        print("valores encontrados")
        if data.isspace():
            print("O valor encontrado é um espaço")
        else:
            print("O valor encontrado é: ", data)

def minha_classe():
    meu_parser1 = MeuParser()
    arquivo = open("/home/serlus/repositorios/Learning/estudos/linkedin/calendario.html", "r")
    dados = arquivo.read()
    meu_parser1.feed(dados)

minha_classe()