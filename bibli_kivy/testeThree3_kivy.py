#O Kivy também fornece uma linguagem de design chamada KV, que você pode usar com seus aplicativos Kivy. A linguagem KV permite separar o design da interface e a lógica do aplicativo.
#Isso segue o princípio da separação de interesses e faz parte do padrão de arquitetura Model-View-Controller.
#Você pode atualizar o exemplo anterior para usar a linguagem KV. Confira!

from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('Você apertou o botão!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()


#Esse código pode parecer um pouco estranho à primeira vista, pois cria um Button sem definir nenhum de seus atributos ou vinculá-lo a nenhum evento.
#O que está acontecendo aqui é que o Kivy procurará automaticamente um arquivo que tenha o mesmo nome da classe em letras minúsculas.
#Nesse caso, o nome da classe é ButtonApp, então Kivy procurará um arquivo chamado button.kv. Se esse arquivo existir e estiver formatado corretamente, o Kivy o usará para carregar a interface do usuário.

#Vá em frente, crie esse arquivo e digite o código nele.
























