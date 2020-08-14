"""master launch sequence
Args:
    sys ([list]): [sistemas de lançamento]
    step ([list]): [com sequencia dos sistemas]

>>> syst = ["stage_1", "stage_2", "dragon", "stage_1", "stage_2", "dragon"]
>>> step = [1,10,11,2,12,111]
>>> sistemas = Sistemas()
>>> sistemas.verificar
syst = ["stage_1", "stage_2", "dragon", 
"stage_1", "stage_2", "dragon"]
>>> sistemas.listar()
>>> sistemas.verificar
"stage_1", "stage_2", "dragon"
>>>
>>> launch(sys, step)
true
>>> launch = Launcher()
>>> 

"""



class Sistemas:
    def __init__(self, verificar ):
        self.sistemas = []
        self.verificar = verificar