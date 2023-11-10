# Pedro Martins de Andrade - RA: 4201075
# Thiago Dantas - RA: 4201051

from kivymd.app import MDApp
from widgets2 import CalcPrimos
from kivy.lang import Builder


class CalculadoraSalarioMain(MDApp):
    def build (self):
        kv = Builder.load_file("widgets2.kv")
        self.theme_cls.primary_palette = "DeepOrange"
        return CalcPrimos()
    
    
CalculadoraSalarioMain().run()
