#Continuação...

#Supondo que o primeiro arquivo se chame: funcionalidades.py, o segundo arquivo (que pode se chamar: teste.py) vai importar as funcionalidades do seguinte modo:

from funcionalidades import *

tv = Televisor('Sony', 'Sony-123')
controle = ControleRemoto(tv)

controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print(tv.canal_atual)



#Veja que bastou importar tudo dentro de “funcionalidades”, ou seja, o arquivo .py se tornou, de certa forma, uma biblioteca em que você pode acessar comandos, deixando os testes mais fáceis de serem feitos e com menos riscos de prejudicar o arquivo base.
#Lembre-se que essa é uma maneira de manter as boas práticas de programação.