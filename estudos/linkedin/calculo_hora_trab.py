from datetime import datetime
from datetime import timedelta


def dia_de_trampo():

    inicio_expediente = datetime(2020, 9, 14, 9, 0, 0)
    ent_almoco = datetime(2020, 9, 14, 12, 00, 00)
    saida_almoco = timedelta(hours=1)
    expediente = timedelta(hours=8)
    
    
    print("Inicio do expediente: ", inicio_expediente)
    print("Entrada no almoço: ", ent_almoco)
    print("saida do almoço: ", ent_almoco + saida_almoco )
    print("Fim do expediente: ", inicio_expediente + expediente + saida_almoco)

dia_de_trampo()