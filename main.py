from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
import operaciones

Window.size=(800,250)

class CalculadoraVenn(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

    def backspace(self):
        text=self.root.ids.operation.text
        n=len(text)
        self.root.ids.operation.text=text[0:n-2]
    
    def calculate(self):
        text=self.root.ids.operation.text
        text=text.strip()
        if len(text.replace(' ',''))==3:
            operaciones._2sets(text)
        elif len(text.replace(' ',''))==5:
            operaciones._3sets(text)
        else:
            print('Tas mal chavo')
        self.root.ids.resultado.source=''
        self.root.ids.resultado.source='graph.png'

if __name__=='__main__':
    CalculadoraVenn().run()
