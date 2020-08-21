# Arquivo com exemplos de manipulação de datas

from datetime import datetime
from datetime import time
from datetime import date


def manipula_data_hora():
    hoje = date.today()
    print("Hoje é: ", hoje)
    print("Partes da data: ", hoje.day, hoje.month, hoje.year)
    print("Número do dia da semana: ", hoje.weekday())
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    print("Nome abreviado do dia da semana: ", dias[hoje.weekday()])

    data = datetime.now()
    print("Data e hora: ", data)

    tempo = datetime.time(data)
    print("Hora atual: ", tempo)

  
manipula_data_hora()