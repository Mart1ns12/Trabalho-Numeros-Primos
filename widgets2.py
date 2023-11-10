
# Pedro Martins de Andrade - RA: 4201075
# Thiago Dantas - RA: 4201051

from kivymd.uix.screen import Screen
from primo import Analise

class CalcPrimos (Screen):

        def analisar (self):
            
            try:    
                primo = int(self.ids.input.text)
                if primo > 1:
                    analise = Analise(primo)
                    resultado = analise.formulaAnalise()
                    self.ids.saida.text = resultado
                    return
                else:
                    self.ids.input.error = "Insira um numero maior que 1"
                    return
            
            except ValueError:
                self.ids.input_field.error = "Insira um valor"

    