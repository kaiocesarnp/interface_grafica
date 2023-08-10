#O Kivy tem o conceito de um relógio que você pode usar para agendar chamadas de função para algum tempo no futuro.
#Ele também tem a função Properties, que funciona com o EventDispatcher.
#As propriedades o ajudam a fazer a verificação de validação. Elas também permitem que você dispare eventos sempre que um widget mudar de tamanho ou posição.

#Adicionar um evento de botão ao código visto anteriormente. Veja como fazer isso no código abaixo:

from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        button = Button(text = 'Fala Galera!',
                size_hint = (.5, .5),
                pos_hint = {'cente_x': .5, 'center_y': .5})

        button.bind(on_press = self.on_press_button)

        return button

    def on_press_button(self, instance):
        print('Você apertou o botão!')

if __name__ == '__main__':
    app = MainApp()
    app.run()
