from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size=(800,250)

class CalculadoraVenn(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

if __name__=='__main__':
    CalculadoraVenn().run()
