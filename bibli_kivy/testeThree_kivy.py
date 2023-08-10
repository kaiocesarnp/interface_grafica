#Cada estrutura de GUI que você usa, tem seu próprio método de organização de widgets.
#Com Kivy, você usará layouts.
#Existem vários tipos diferentes de layouts que se pode usar.
#Aqui estão alguns dos mais comuns: BoxLayout, FloatLayout, GridLayout

#Layout com diferentes cores:

import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout #importa BoxLayout e kivy.uix.boxlayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding = 10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text = f"Este é o botão #{i+1}",
                  background_color = random.choice(colors)  #define background_color para uma cor aleatória.
                         )

            layout.add_widget(btn) #adiciona o botão ao seu layout comlayout.add_widget(btn)
        return layout

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()
