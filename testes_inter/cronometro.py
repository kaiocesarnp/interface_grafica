#Criando uma pequena aplicação em Python

#Imagine que você foi designado para uma tarefa onde precise criar um arquivo chamado cronometro.py que, ao ser clicado duas vezes, abre uma janela do executável Python e mostra um cronômetro que vai contabilizando segundos, minutos e horas.

import time
import os

class Cronometro:
    def __init__ (self, segundos = 0, minutos = 0, horas = 0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas

    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

    def incrementos(self):
        self.segundos += 1 #contador de segundos
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1

        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1

    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.incrementos()
            if self.minutos == 1: #quando atingir 1 minuto, o loop para
                print("Tempo esgotado!")
                break
            time.sleep(1)

cronometro1 = Cronometro()
cronometro1.start()


#Após ver todos esses conceitos, é importante que você entenda como a orientação a objetos tem relação com o desenvolvimento de aplicações.
