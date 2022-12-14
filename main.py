from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size=(800,250)

class CalculadoraVenn(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

    def backspace(self):
        text=self.root.ids.operation.text
        n=len(text)
        self.root.ids.operation.text=text[0:n-2]
    
    def calculate(self):
        pass

if __name__=='__main__':
    CalculadoraVenn().run()
