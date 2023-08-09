#Que tal mais um exemplo?
#Foi solicitado à você uma classe Funcionário, cujos atributos são: nome e e-mail. Deve-se guardar as horas trabalhadas em um dicionário, cujas chaves são o mês em questão e, em outro dicionário, guardar o salário por hora relativo ao mês em questão.
#Além disso, precisamos de um método que retorna o salário mensal do funcionário. A proposta é que sejam separados em dois arquivos:
#um chamado funcionario.py, em que será criada a classe com suas funcionalidades.
#um segundo chamado teste_funcionario.py, em que você deve aplicar testes e verificar a legitimidade do código anterior.
#Para resolver essa questão, é necessário criar uma pasta no computador contendo os dois arquivos, sendo que o conteúdo do primeiro arquivo será conforme apresentado no código a seguir:

class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario_hora = {}

    def cadastro_hora(self, mes, horas):
        if (mes not in self.horas):
            self.horas[mes] = horas

    def cadastro_salario_hora(self, mes, valor):
        if (mes not in self.salario_hora):
            self.salario_hora[mes] = valor

    def calcula_salario(self, mes):
        if (mes not in self.horas) or (mes not in self.salario_hora):
            print('Mês Inexistente!')
        else:
            return self.horas[mes] * self.salario_hora[mes]

    def __repr__(self):
        return f'Funcionário: {self.nome}, \nEmail: {self.email}, \nHoras/Mês: {self.horas}, \nSalario-hora: {self.salario_hora}'

#É possível notar que os dicionários contendo as informações de horas e salário devem ser inicialmente vazios e criados dentro do método construtor da classe.

#Continua no arquivo 'teste_funcionario.py'
