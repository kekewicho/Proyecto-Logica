from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
import operaciones
import os
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

Window.size=(800,350)

class CalculadoraVenn(MDApp):
    dialog=None
    def build(self):
        for i in os.listdir('img/'):
            os.remove(os.path.join('img/', i))
        return Builder.load_file('main.kv')
    
    def show_message(self,message):
        def close_dialog(obj):
            self.dialog.dismiss()

        if not self.dialog:
            self.dialog = MDDialog(
                title="¡Error!",
                text=message,
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_press = close_dialog
                    )
                ]
            )
        self.dialog.open()


    def validaciones(self,text):
        operation=self.root.ids.operation.text
        if len(operation)==0:
            self.root.ids.operation.text=self.root.ids.operation.text+' '+text
        else:
            if text in ('A','B','C') and operation[-1] not in ('Δ','n','u','-'):
                self.show_message('No has ingresado ningún operador')
            elif text in ('Δ','n','u','-') and operation[-1] not in ('A','B','C'):
                self.show_message('No olvides agregar un conjunto para realizar operaciones')
            else:
                self.root.ids.operation.text=self.root.ids.operation.text+' '+text


    def delete(self):
        self.root.ids.operation.text=''

    def calculate(self):
        text=self.root.ids.operation.text
        txt=self.root.ids.operation.text
        if len(text.replace(' ','')) in (3,5):
            text=text.strip()
            if len(text.replace(' ',''))==3:
                if 'C' in text:
                    self.show_message('El conjunto "C" es solo usado para operaciones de 3 conjuntos')
                else:
                    operaciones._2sets(text)
            elif len(text.replace(' ',''))==5:
                operaciones._3sets(text)
            else:
                print('Tas mal chavo')
            self.root.ids.resultado.source='img/'+txt.replace(' ','')+'.png'
        else:
            self.show_message('La operación tiene menos valores de los esperados')

if __name__=='__main__':
    CalculadoraVenn().run()
