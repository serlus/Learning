from datetime import datetime


def formata_data_hora():
    # %y/%Y - ano, 
    hoje = datetime.now()

    print(hoje.strftime("O ano é: %y"))

    print(hoje.strftime("Data e hora local: %c"))

formata_data_hora()