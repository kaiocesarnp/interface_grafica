#Em seguida, é possível fazer um teste simples, com um looping que manterá a janela do executável .py aberta para você testar indefinidamente, observe:

from area import Retangulo
import math

while True:
    piso_a = float(input("Digite um lado do piso: "))
    piso_b = float(input("Digite o outro lado do piso: "))
    piso = Retangulo(piso_a, piso_b)

    az_a = float(input("Digite o lado do azulejo: "))
    az_b = float(input("Digite o outro lado do azulejo: "))
    azulejo = Retangulo(az_a, az_b)

    area_piso = piso.area()
    area_az = azulejo.area()

    qntd_az = area_piso / area_az

    if area_piso% area_az == 0:
        print(f'A quantidade exata de azulejos para preencher o piso é de {qntd_az}')

    else:
        print(f'A quantidade mínima de azulejos para preencher o piso é de {math.ceil(qntd_az)}')

    break;

#Nesse caso, foi abordado o conceito de calcular a quantidade exata de pisos, ou até mesmo a quantidade mínima, caso o valor seja um número que possua casas decimais (a função math.ceil( ) arredonda o número para cima).
