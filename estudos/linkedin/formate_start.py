from datetime import datetime


def formata_data_hora():
    # %y/%Y - ano, %a/%A -Dia da semana, %d/%d - dia do mês, %b/%B - mês
    hoje = datetime.now()

    print(hoje.strftime("O ano é: %y"))
# %c - data e hora local, %x - data local, %X - hora local
    print(hoje.strftime("Data e hora local: %c"))

### Time Formatting ###
# %I/%H - 12/24 hpras, %M - min, %S - seg, %p - AM/PM
    print(hoje.strftime("A hora atual é: %I:%M:%S %p"))
    print(hoje.strftime("ou de outra forma: %H:%M:%S"))
    
formata_data_hora()