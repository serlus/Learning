from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta


def quantos_dias_faltam(ano, mes, dia):
    hoje = date.today()
    data_procurada = date(ano, mes, dia)

    qtos_dias = data_procurada - hoje

    mensagem_retorno = "Faltam " + str(qtos_dias).replace("days, 0:00:00", "") + " dias para a data " + data_procurada.strftime("%d/%m/%y")

    print(mensagem_retorno)

quantos_dias_faltam(2020, 10, 22)
