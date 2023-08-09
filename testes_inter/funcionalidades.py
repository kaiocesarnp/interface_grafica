#Encapsulando códigos e criando bibliotecas

#A Programação Orientada a Objetos nos permite criar as classes e suas características para que, dentro de um arquivo Python, possamos guardar funcionalidades que podem ser reaproveitadas para diferentes projetos e finalidades.
#Ou seja, é possível criar funcionalidades dentro de um arquivo .py, que mais tarde pode ser importado em outros arquivos.

#Criar uma classe chamada Televisor, cujos os atributos são:
#Fabricante
#Modelo
#Canal atual
#Lista de canais
#Volume

#Para isso, é preciso criar métodos para aumentar/diminuir volume, trocar e sintonizar um novo canal, adicionando um novo canal à lista (somente se esse canal não estiver nessa lista). No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV.

#

#Criar uma classe ControleRemoto, cujo atributo é televisão (isto é, recebe um objeto da classe Televisor). Neste caso, você deve criar métodos para aumentar/diminuir volume, trocar e sintonizar um novo canal, que adiciona um novo canal à lista de canais (somente se esse canal não estiver nessa lista).

class Televisor:
    def __init__(self, fab, modelo):
        self.fabricante = fab
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 20

    def aumentaVolume(self, valor):
        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100

    def diminuiVolume(self, valor):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def trocaCanal(self, canal):
        if canal in self.lista_de_canais:
            self.canal_atual = canal

    def sintonizaCanal(self, canal):
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)

class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv

    def aumentaVolume(self):
        self.tv.aumentaVolume(90)

    def diminuiVolume(self):
        self.tv.diminuiVolume(90)

    def trocaCanal(self, canal):
        self.tv.trocaCanal(canal)

    def sintonizaCanal(self, canal):
        self.tv.sintonizaCanal(canal)

#Dado esse problema, imagine agora que, além de criar essa funcionalidade, o projeto precisa ser feito de tal maneira que os testes dessas funcionalidades sejam feitos em um arquivo .py à parte do arquivo das funcionalidades.
#Como fazer para testar essas funcionalidades em um arquivo à parte?
#A resposta é bem simples: basta criar dois arquivos .py na mesma pasta de trabalho: o primeiro vai conter o código acima, e o segundo vai importar as classes criadas.
#Supondo que o primeiro arquivo se chame: funcionalidades.py, o segundo arquivo (que pode se chamar: teste.py) vai importar as funcionalidades do seguinte modo:












