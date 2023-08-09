from kivy.app import App
from kivy.uix.label import Label

#Perceba que todo aplicativo Kivy precisa da subclasseApp e da função build().

class MainApp(App):
    def build(self):

#Neste caso, crie um widget do tipo label e passe comoparâmetro: text, size_hint, e pos_hint (estes dois últimosargumentos não são obrigatórios).

        label = Label(text = 'O Parmera não tem Mundial!',
##O comando size_hint informa ao Kivy as proporções aserem usadas ao criar o widget.
#Para isso são necessários dois números:O primeiro número (x): refere-se à largura do controle.O segundo número (y): refere-se à altura do controle.
            size_hint = (.100, .99),
            pos_hint = {'center_x': .5, 'cente_y': .5})

        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()
