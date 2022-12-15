from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
import operaciones
from kivy.uix.image import Image

Window.size=(800,250)

class CalculadoraVenn(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

    def delete(self):
        self.root.ids.operation.text=''
        self.root.ids.resultado.clear_widgets()

    def calculate(self):
        text=self.root.ids.operation.text
        text=text.strip()
        if len(text.replace(' ',''))==3:
            operaciones._2sets(text)
        elif len(text.replace(' ',''))==5:
            operaciones._3sets(text)
        else:
            print('Tas mal chavo')
        self.root.ids.resultado.source='graph.png'

if __name__=='__main__':
    CalculadoraVenn().run()
