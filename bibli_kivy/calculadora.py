#Usar o Kivy para construir uma calculadora que suporte as seguintes operações:
#Adição, Subtração, Multiplicação, Divisão
#Para essa aplicação, precisará de uma série de botões em algum tipo de layout. E também precisará de uma caixa na parte superior do aplicativo para exibir as equações e seus resultados.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"] #criamos uma lista deoperators e alguns valores úteis, last_was_operatore last_button
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation = "vertical") #criamos um layoutmain_layout de nível superior e adicionamosum widget TextInput somente leitura a ele
        self.solution = TextInput(
            multiline = False, readonly = True, halign = "right", font_size = 55)
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"], #criamos uma lista aninhada de listas contendo a maioria dosnossos buttons para a calculadora
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
            ]
        for row in buttons:         #nós iniciamos um forloop sobre aqueles buttons.Para cada listaaninhada, fizemos o seguinte:
            h_layout = BoxLayout()  # criamos um BoxLayout com orientação horizontal;
            for label in row:       #iniciamos outro loop sobre os itens da lista aninhada
                button = Button(
                    text = label,   #criamos os botõespara a linha, os vinculamos a um manipuladorde eventos e adicionamos os botões à horizontalBoxLayout da linha 23
                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                    )
                button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
                main_layout.add_widget(h_layout)    #adiciona esse layout ao arquivomain_layout

        equals_button = Button(
            text = "=", pos_hint = {"center_x": 0.5, "center_y": 0.5}
            )
        equals_button.bind(on_press = self.on_solution) # cria o botão igual (=),associa-o a um manipulador de eventos e adiciona-oa main_layout
        main_layout.add_widget(equals_button)

        retur main_layout

#A próxima etapa é criar o manipulador de eventos on_button_press()

    def on_button_press(self, instance):    #recebe o argumento instance para que você possaacessar qual widget chamou a função
        current = self.solution.text        #extraem e armazenam ovalor do solution e do botão text
        button_text = instance.text

        if button_text == "C":      #verificam qual botão foi pressionado. Se ousuário pressionou C, você limpará o arquivo solution. Caso contrário,vá para a declaração else
            #Limpar o widget de solução  
            self.solution.text = ""

        else:
            if current and
        


















