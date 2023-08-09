#Testando com imagem:

#O Kivy tem alguns widgets relacionados a imagens diferentes, para escolher. Você pode usar Image para carregar imagens locais do seu disco rígido ou AsyncImage para carregar uma imagem de uma URL.
#Para este exemplo, vamos testar trazendo uma imagem via URL, escreva:

from kivy.app import App
from kivy.uix.image import Image, AsyncImage #Nesse código, você importa AsyncImage do kivy.uix.image

class MainApp(App):
    def build(self):
        img = AsyncImage(source = 'https://www.lance.com.br/galerias/wp-content/uploads/2022/02/memes-palmeiras-mundial-chelsea-31-593x474.jpg',
            size_hint = (1, .5),
            pos_hint = {'center_x': .5, 'center_y': .5})

        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()

