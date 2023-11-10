# Pedro Martins de Andrade - RA: 4201075
# Thiago Dantas - RA: 4201051

from kivymd.uix.boxlayout import MDBoxLayout

class Analise (MDBoxLayout):

    def __init__(self,numero):
        self.numero = numero

    def formulaAnalise (self):
        numeros = []
        numerosPrimos = []
        
        for i in range(2, self.numero+1):
            numeros.append(i)
        
        for j in numeros:
            if j == 2:
                numerosPrimos.append(j)
            if j == 3:
                numerosPrimos.append(j)
            if j == 5:
                numerosPrimos.append(j)
            if j == 7:
                numerosPrimos.append(j)

            if j % 2 != 0:
                if j % 3 != 0:
                    if j % 5 != 0:
                        if j % 7 != 0:
                            numerosPrimos.append(j)
        resultado = str(numerosPrimos)
        return resultado
    
    
    