#Para entender melhor essa linha de raciocínio, vamos para mais um desafio: imagine que você foi designado para criar um sistema que recebe dimensões de pisos de uma casa e dimensões de azulejos que vão cobrir os pisos.
#Sua missão é mostrar a quantidade de azulejos necessária com base na área do piso e do azulejo escolhido. É evidente que os testes das funcionalidades devem estar em um arquivo à parte.
#Uma maneira de resolver o problema é criar as funcionalidades pensando em retângulos, já que azulejos e os pisos normalmente são quadriláteros.
#Logo, o arquivo de funcionalidades chamado de area.py ficará da seguinte forma:

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.a = lado_a
        self.b = lado_b

    def muda_valor(self, novo_a, novo_b):
        self.a = novo_a
        self.b = novo_b

    def retorna_lado(self):
        print(f'O retângulo possui dimensões {self.a}m x {self.b}m')

    def area(self):
        return self.a * self.b

#Continua no arquivo 'teste_area.py'
