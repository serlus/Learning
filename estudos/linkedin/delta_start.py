from datetime import datetime
from datetime import date
# from datetime import time
from datetime import timedelta
from time import time


def delta_tempo():
    # é uma das formas de manipulação de datas do python 
    delta = timedelta(days=86, hours=8532, minutes=7645)
    print(delta)

    hoje = datetime.now()
    print("Data no futuro: ", hoje + delta)
    print("Data no passado: ", hoje - delta)

    ent_almoco = datetime(2020, 9, 14, 12, 00, 00)
    saida_almoco = timedelta(hours=1)
    
    print("Entrada no almoço: ", ent_almoco)
    print("saida do almoço: ", ent_almoco + saida_almoco )
delta_tempo()