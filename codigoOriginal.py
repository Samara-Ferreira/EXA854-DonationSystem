"""
Autor: Samara dos Santos Ferreira
Componente Curricular: MI - Algoritmos I
Concluído em: 09/04/2022
Declaro que este código foi elaborado por mim de forma individual e não contém
nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""

# Declaração das variáveis

    # Variáveis dos alimentos que não precisam de uma quantidade específica para formarem um item
quant_acucar = quant_bolacha = quant_farinha = quant_oleo = quant_sal = quant_extras = 0
    # Variáveis dos alimentos que precisam de uma quantidade específica para formarem um item
quant_arroz_item = quant_cafe_item = quant_extrato_item = quant_feijao_item = quant_macarrao_item = 0
    # Variáveis utilizadas para guardarem a quantidade total de cada alimento
        # São utilizadas na saída do programa, imprimindo o total e o restante de cada alimento doado
quant_acucar_total = quant_arroz_total = quant_bolacha_total = quant_cafe_total = quant_extrato_total = 0
quant_farinha_total = quant_feijao_total = quant_macarrao_total = quant_oleo_total = quant_sal_total = quant_extras_total = 0
    # Varíaveis utilizadas para guardar o total de itens doados por pessoas físicas e jurídicas
fisicas = juridicas = 0
    # Listas utilizadas para guardar a quantidade, o tipo e a unidade de medida do item extra, respectivamente
quant_itens_extras = []
tipos_extras = []
unidades_extras = []


# Gerenciamento de doações
 
print('-='*62, f'\n{"DISPENSÁRIO SANTANA":^124}\n', '-='*62)

    # Variável condicional do while
        #  Utilizada para que o sistema só pare o cadastramento mediante solicitação do funcionário

continuacao = 's'
continuar = 1
while continuar == 1:

    # Registro do nome do doador e a sua respectiva validação
        # Validação: impede a entrada de dados incorretos, tais como números, simbologias, espaços em branco, etc.
    nome = input('\n> Digite o nome do doador: ').strip().title()
    nome_teste = nome.replace(" ", "")
    while nome_teste.isalpha() == False:
        print('\n\tNOME DO DOADOR INVÁLIDO!\n\t- Por favor, digite novamente:\n')
        nome = input('> Digite o nome do doador: ').strip().title()
        nome_teste = nome.replace(" ", "")

    # Registro do tipo de doador e a sua respectiva validação
        # Validação: impede a entrada de dados incorretos, tais como letras, espaços, númros maiores do que 2 e números menores do que um
    print(f'\n{"-"*46}', f'{" TIPOS DE DOADORES "}', f'{"-"*46}\n')
    print(f'{f"| [1] Pessoa Física ":28} | {f"[2] Pessoa Jurídica":28} |\n'.center(111))
    tipo_doador = input('> Digite o tipo de doador: ').strip()
    while tipo_doador != '1' and tipo_doador != '2':
        print('\n\tTIPO DE DOADOR INVÁLIDO!\n\t- Por favor, digite novamente:\n')
        tipo_doador = input('> Digite o tipo de doador: ').strip()

    # Segundo while: utilizado para caso um doador desejar doar mais de um donativo
    while continuacao == 's':

        # Menu para escolha do tipo de donativo
        print(f'\n{"-"*46}', f'{" ALIMENTOS DA CESTA BÁSICA "}', f'{"-"*46}\n')
        print(f'{f"| [1] Açúcar":28} | {f"[4] Café":28} | {f"[7] Feijão":28} | {f"[10] Sal":28} |')
        print(f'{f"| [2] Arroz":28} | {f"[5] Extrato de Tomate":28} | {f"[8] Macarrão":28} | {f"[11] Extra":28} |')
        print(f'{f"| [3] Bolacha":28} | {f"[6] Farinha de Trigo":28} | {f"[9] Óleo":28} | {f" ":28} |\n')

        # Entrada e validação do tipo de item
            # While: utilizado para que não ocorra a entrada de dados incorretos, tais como letras, números maioresdo do que 11 e menores do que 1
        var = 'v'
        while var == 'v':
            try:
                tipo_item = int(input('> Digite o tipo de item: '))

                while tipo_item < 1 or tipo_item > 11:
                    print('\n\tTIPO DE ITEM INVÁLIDO!\n\t- Por favor, digite novamente:\n')
                    tipo_item = int(input('> Digite o número do item: '))

            except:
                print('\n\tTIPO DE ITEM INVÁLIDO!\n\t- Por favor, digite novamente:\n')
            else:
                var = 'f'

        # Menu para escolha da unidade de medida do donativo
        print(f'\n{"-"*46}', f'{" UNIDADES DE MEDIDA "}', f'{"-"*46}\n')
        print(f'{"| [1] Litros (L)":28} | {"[3] Quilograma (kg)":28} | {"[5] Pacote (pct)":28} |')
        print(f'{"| [2] Mililitros [mL]":28} | {"[4] Gramas (g)":28} | {"[6] Unidade (un)":28} |\n')

        # Entrada e validação da unidade do item
            # While: utilizado para que não ocorra a entrada de dados incorretos, tais como letras, números maiores do do que 6 e menores do que 1
        var = 'v'
        while var == 'v':
            try:
                unidade = int(input('> Digite a unidade de medida do item: '))

                while unidade < 1 or unidade > 6:
                    print('\n\tUNIDADE DE MEDIDA INVÁLIDA!\n\t- Por favor, digite uma opção válida [1 - 6]:\n')
                    unidade = int(input('> Digite a unidade de medida do item: '))

                # Novo while: verifica se o funcionario digitou uma unidade válida para determinado item
                while (tipo_item == 1 or tipo_item == 2 or tipo_item == 4 or tipo_item == 6 or tipo_item == 7 or tipo_item == 10) and (unidade != 3 and unidade != 4):
                    print('\n\tUNIDADE DE MEDIDA INVÁLIDA!\n\t- As opções válidas para esse item são quilogramas [kg] e gramas [g].\n')
                    unidade = int(input('> Digite a unidade de medida do item: '))

                # Novo while: verifica se o funcionario digitou uma unidade válida para determinado item
                while (tipo_item == 5 or tipo_item == 8) and unidade != 6:
                    print('\n\tUNIDADE DE MEDIDA INVÁLIDA!\n\t- A opção válida para esse item é unidade [un].\n')
                    unidade = int(input('> Digite a unidade de medida do item: '))

                # Novo while: verifica se o funcionario digitou uma unidade válida para determinado item
                while tipo_item == 3 and unidade != 5:
                    print('\n\tUNIDADE DE MEDIDA INVÁLIDA!\n\t- A opção válida para esse item é pacote [pct].\n')
                    unidade = int(input('> Digite a unidade de medida do item: '))

                # Novo while: verifica se o funcionario digitou uma unidade válida para determinado item
                while tipo_item == 9 and (unidade != 1 and unidade != 2):
                    print('\n\tUNIDADE DE MEDIDA INVÁLIDA!\n\t- As opções válidas para esse item são litros [L] e mililitros [mL].\n')
                    unidade = int(input('> Digite a unidade de medida do item: '))

            except:
                print('\n\tUNIDADE DE MEDIDA INVÁLIDA!\n\t- Por favor, digite novamente:\n')
            else:
                var = 'f'

        # Entrada e validação da quantidade do item
            # While: utilizado para que não ocorra a entrada de dados incorretos, tais como letras e números menores do que 0
        var = 'v'
        while var == 'v':
            try:
                quantidade = float(input('> Digite a quantidade do item: '))

                # Novo while: impede a entrada de quantidades menores do que zero
                while quantidade < 0:
                    print('\n\tQUANTIDADE INVÁLIDA!\n\t- Por favor, digite novamente:\n')
                    quantidade = float(input('> Digite a quantidade do item: '))

            except:
                print('\n\tQUANTIDADE INVÁLIDA!\n\t- Por favor, digite novamente:\n')
            else:
                var = 'falso'

            # Conversões de medidas
                # Transforma as gramas e mililitros em quilogramas e em litros, respectivamente
        if unidade == 2:
            quantidade /= 1000
        elif unidade == 4:
            quantidade /= 1000

        # Atribuição da quantidade dos itens as suas respectivas variáveis, de acordo com o 'Menu de Alimentos'
        if tipo_item == 1:
            # Variável utilizada para a montagem das cestas básicas, que sofrerá um decréscimo de acordo com a quantidade de cestas formadas
            quant_acucar += quantidade
            # Essa variável não será modificada; será utilizada na saída do programa para imprimir a quantidade total de acúcar e o que sobrou
            quant_acucar_total += quantidade
            if tipo_doador == '1':
                if quantidade == 0:
                    fisicas += 0  # Caso a quantidade seja igual a zero, o sistema não contabilizará isso como uma doação
                else:
                    fisicas += quant_acucar // 1
            else:
                if quantidade == 0:
                    juridicas += 0
                else:
                    juridicas += quant_acucar // 1

        elif tipo_item == 2:
            quant_arroz_total += quantidade
            if quant_arroz_total >= 4:  # Variável utilizada na montagem das cestas básicas, que sofrerá um decréscimo de acordo com a quantidade de cestas formadas
                # Para formar um item de arroz, deve-se ter um total de 4kg
                quant_arroz_item += quant_arroz_total // 4
                if tipo_doador == '1':
                    if quantidade == 0:
                        fisicas += 0
                    else:
                        fisicas += quant_arroz_item
                else:
                    if quantidade == 0:
                        juridicas += 0
                    else:
                        juridicas += quant_arroz_item

        elif tipo_item == 3:
            quant_bolacha += quantidade
            quant_bolacha_total += quantidade
            if tipo_doador == '1':
                if quantidade == 0:
                    fisicas += 0
                else:
                    fisicas += quant_bolacha // 1
            else:
                if quantidade == 0:
                    juridicas += 0
                else:
                    juridicas += quant_bolacha // 1

        elif tipo_item == 4:
            quant_cafe_total += quantidade
            if quant_cafe_total >= 2:
                quant_cafe_item += quant_cafe_total // 2
                if tipo_doador == '1':
                    if quantidade == 0:
                        fisicas += 0
                    else:
                        fisicas += quant_cafe_item
                else:
                    if quantidade == 0:
                        juridicas += 0
                    else:
                        juridicas += quant_cafe_item

        elif tipo_item == 5:
            quant_extrato_total += quantidade
            if quant_extrato_total >= 2:
                quant_extrato_item += quant_extrato_total // 2
                if tipo_doador == '1':
                    if quantidade == 0:
                        fisicas += 0
                    else:
                        fisicas += quant_extrato_item
                else:
                    if quantidade == 0:
                        juridicas += 0
                    else:
                        juridicas += quant_extrato_item

        elif tipo_item == 6:
            quant_farinha += quantidade
            quant_farinha_total += quantidade
            if tipo_doador == '1':
                if quantidade == 0:
                    fisicas += 0
                else:
                    fisicas += quant_farinha // 1
            else:
                if quantidade == 0:
                    juridicas += 0
                else:
                    juridicas += quant_farinha // 1

        elif tipo_item == 7:
            quant_feijao_total += quantidade
            if quant_feijao_total >= 4:
                quant_feijao_item += quant_feijao_total // 4
                if tipo_doador == '1':
                    if quantidade == 0:
                        fisicas += 0
                    else:
                        fisicas += quant_feijao_item
                else:
                    if quantidade == 0:
                        juridicas += 0
                    else:
                        juridicas += quant_feijao_item

        elif tipo_item == 8:
            quant_macarrao_total += quantidade
            if quant_macarrao_total >= 3:
                quant_macarrao_item += quant_macarrao_total // 3
                if tipo_doador == '1':
                    if quantidade == 0:
                        fisicas += 0
                    else:
                        fisicas += quant_macarrao_item
                else:
                    if quantidade == 0:
                        juridicas += 0
                    else:
                        juridicas += quant_macarrao_item

        elif tipo_item == 9:
            quant_oleo += quantidade
            quant_oleo_total += quantidade
            if tipo_doador == '1':
                if quantidade == 0:
                    fisicas += 0
                else:
                    fisicas += quant_oleo // 1
            else:
                if quantidade == 0:
                    juridicas += 0
                else:
                    juridicas += quant_oleo // 1

        elif tipo_item == 10:
            quant_sal += quantidade
            quant_sal_total += quantidade
            if tipo_doador == '1':
                if quantidade == 0:
                    fisicas += 0
                else:
                    fisicas += quant_sal // 1
            else:
                if quantidade == 0:
                    juridicas += 0
                else:
                    juridicas += quant_sal // 1

        # Atribuição dos itens extras
        elif tipo_item == 11:
            quant_extras += 1
            quant_extras_total += quantidade
            if tipo_doador == '1':
                fisicas += quantidade
            else:
                juridicas += quantidade

            # Entrada e validação do nome do item extra
            nome_item_extra = input('> Digite o nome do item extra: ').strip().title()
            nome_item_extra_f = nome_item_extra.replace(" ", "")
            while nome_item_extra_f.isalpha() == False:
                print('\n\tNOME INVÁLIDO!\n\t- Por favor, digite novamente:\n')
                nome_item_extra = input('Digite o nome do item extra: ').strip().title()
                nome_item_extra_f = nome_item_extra.replace(" ", "")

            # Montagem das listas
                # Tipos dos itens extras
            tipos_extras.append(nome_item_extra)
                # Quantidades dos itens extras
            quant_itens_extras.append(quantidade)
                # Unidades de medidas dos itens extras
            if unidade == 1:
                unidades_extras.append('L')
            elif unidade == 2:
                unidades_extras.append('L')
            elif unidade == 3:
                unidades_extras.append('kg')
            elif unidade == 4:
                unidades_extras.append('kg')
            elif unidade == 5:
                unidades_extras.append('pct')
            elif unidade == 6:
                unidades_extras.append('un')


    # Condicionais do while
        continuacao = input(f'\n\t>> Há mais donativos doados por {nome}? ').strip().lower()[0]

    print('\n\t>> O Dispensário Santana agradece pela doação! ')

    # Menu de opções: escolha entre continuar o cadastro ou visualizar o relatório    
    print('\n', '-'*20, ' MENU DE OPÇÕES ')

    print(f'\n{f"| [1] Continuar as doações":28} | {f"[3] Finalizar o expediente":28} \n| {f"[2] Visualizar o relatório":28}') 

    valida_continuar = 'v'
    while valida_continuar == 'v':
        try:
            continuar = int(input('\n\t>> Escolha uma das opções acima [1 - 3]: '))
           
            while continuar < 1 or continuar > 3:
                print('\n\tOPÇÃO INVÁLIDA!\n\t- Por favor, digite uma opção entre 1 e 3:')
                continuar = int(input('\n\t>> Escolha uma das opções acima [1 - 3]: '))
        except:
            print('\n\tINVÁLIDO!\n\t- Por favor, digite novamente:')
        else:
            valida_continuar = 'f'

    if continuar == 1:
        continuar = 1
        continuacao = 's'
    else:
        continuar = 2


# Organização e montagem das cestas básicas

    # Declaração das variáveis
cestas = cestas_com_extras = cestas_sem_extras = 0
total_extras = quant_extras_total

# Montagem das cestas
while quant_acucar > 0 and quant_arroz_item > 0 and quant_bolacha > 0 and quant_cafe_item > 0 and quant_extrato_item > 0 and quant_farinha > 0 and quant_feijao_item > 0 and quant_macarrao_item > 0 and quant_oleo > 0 and quant_sal > 0:
    cestas += 1
    # Verficação se tem item extras ou não
    if total_extras > 0:
        cestas_com_extras += 1
        total_extras -= 1
    else:
        cestas_sem_extras += 1

    quant_acucar -= 1
    quant_arroz_item -= 1
    quant_bolacha -= 1
    quant_cafe_item -= 1
    quant_extrato_item -= 1
    quant_farinha -= 1
    quant_feijao_item -= 1
    quant_macarrao_item -= 1
    quant_oleo -= 1
    quant_sal -= 1

cestas_total = cestas


# Relatório final

print('\n', '-='*62, f'\n{"RELATÓRIO DE DOAÇÕES":^124}\n', '-='*62, '\n')

# Total de cada item recebido

    # Caso as cestas NÃO tenham itens extras
if quant_extras == 0:
    print('-'*45, ' TOTAL DE CADA ITEM RECEBIDO ', '\n')
    print(f'{f"| Açúcar: {quant_acucar_total:.1f} kg":28} | {f"Café: {quant_cafe_total:.1f} kg":28} | {f"Feijão: {quant_feijao_total:.1f} kg":28} | {f"Sal: {quant_sal_total:.1f} kg":28} |')
    print(f'{f"| Arroz: {quant_arroz_total:.1f} kg":28} | {f"Extrato de Tomate: {quant_extrato_total:.1f} un":28} | {f"Macarrão: {quant_macarrao_total:.1f} un":28} | {f" ":28} |')
    print(f'{f"| Bolacha: {quant_bolacha_total:.1f} pct":28} | {f"Farinha de Trigo: {quant_farinha_total:.1f} kg":28} | {f"Óleo: {quant_oleo_total:.1f} L":28} | {f" ":28} |')

    # Caso as cestas tenham 1 item extra
elif 0 < quant_extras <= 1:
    print('-'*45, ' TOTAL DE CADA ITEM RECEBIDO ', '\n')
    print(f'{f"| Açúcar: {quant_acucar_total:.1f} kg":28} | {f"Café: {quant_cafe_total:.1f} kg":28} | {f"Feijão: {quant_feijao_total:.1f} kg":28} | {f"Sal: {quant_sal_total:.1f} kg":28} |')
    print(f'{f"| Arroz: {quant_arroz_total:.1f} kg":28} | {f"Extrato de Tomate: {quant_extrato_total:.1f} un":28} | {f"Macarrão: {quant_macarrao_total:.1f} un":28} | {f"{tipos_extras[0]}: {quant_itens_extras[0]} {unidades_extras[0]}":28} |')
    print(f'{f"| Bolacha: {quant_bolacha_total:.1f} pct":28} | {f"Farinha de Trigo: {quant_farinha_total:.1f} kg":28} | {f"Óleo: {quant_oleo_total:.1f} L":28} | {f" ":28} |')

    # Caso as cestas tenham 2 itens extras
elif 1 < quant_extras <= 2:
    print('-'*45, ' TOTAL DE CADA ITEM RECEBIDO ', '\n')
    print(f'{f"| Açúcar: {quant_acucar_total:.1f} kg":28} | {f"Café: {quant_cafe_total:.1f} kg":28} | {f"Feijão: {quant_feijao_total:.1f} kg":28} | {f"Sal: {quant_sal_total:.1f} kg":28} |')
    print(f'{f"| Arroz: {quant_arroz_total:.1f} kg":28} | {f"Extrato de Tomate: {quant_extrato_total:.1f} un":28} | {f"Macarrão: {quant_macarrao_total:.1f} un":28} | {f"{tipos_extras[0]}: {quant_itens_extras[0]} {unidades_extras[0]}":28} |')
    print(f'{f"| Bolacha: {quant_bolacha_total:.1f} pct":28} | {f"Farinha de Trigo: {quant_farinha_total:.1f} kg":28} | {f"Óleo: {quant_oleo_total:.1f} L":28} | {f"{tipos_extras[1]}: {quant_itens_extras[1]} {unidades_extras[1]}":28} |')

    # Caso as cestas tenham mais de 2 itens extras
else:
    print('-'*45, ' TOTAL DE CADA ITEM RECEBIDO ', '\n')
    print(f'{f"| Açúcar: {quant_acucar_total:.1f} kg":28} | {f"Café: {quant_cafe_total:.1f} kg":28} | {f"Feijão: {quant_feijao_total:.1f} kg":28} | {f"Sal: {quant_sal_total:.1f} kg":28} |')
    print(f'{f"| Arroz: {quant_arroz_total:.1f} kg":28} | {f"Extrato de Tomate: {quant_extrato_total:.1f} un":28} | {f"Macarrão: {quant_macarrao_total:.1f} un":28} | {f"{tipos_extras[0]}: {quant_itens_extras[0]} {unidades_extras[0]}":28} |')
    print(f'{f"| Bolacha: {quant_bolacha_total:.1f} pct":28} | {f"Farinha de Trigo: {quant_farinha_total:.1f} kg":28} | {f"Óleo: {quant_oleo_total:.1f} L":28} | {f"{tipos_extras[1]}: {quant_itens_extras[1]} {unidades_extras[1]}":28} |')
    for i in range(2, len(tipos_extras)):
        print(f'{f"| {tipos_extras[i]}: {quant_itens_extras[i]} {unidades_extras[i]}":28}', end=' | ')


# Total de itens doados por pessoas físicas e jurídicas
print('\n', '-'*45, ' DOAÇÕES POR PESSOAS FÍSICAS E JURÍDICAS ', '\n')
print(f' Total de itens por pessoas FÍSICAS: {int(fisicas)} itens')
print(f' Total de itens por pessoas JURÍDICAS: {int(juridicas)} itens')


# Total de cestas básicas formadas
print('\n', '-'*45, ' CESTAS BÁSICAS ', '\n')

print(f' Total de cestas básicas formadas: {cestas_total} cestas')

# Total de cestas básicas que receberão um item extra
print(f' Total de cestas básicas que receberam um item extra: {cestas_com_extras} cestas')

# Total de cestas básicas que não receberam um item extra
print(f' Total de cestas básicas que NÃO receberam um item extra: {cestas_sem_extras} cestas')


# Itens restantes
print('\n', '-'*45, ' ITENS RESTANTES ', '\n')

    # Subtrai a quantidade de itens extras
while cestas_com_extras > 0:
    quant_extras_total -= 1
    cestas_com_extras -= 1

    # Caso as cestas não tenham itens extras
if quant_extras == 0:
    print(f'{f"| Açúcar: {quant_acucar_total - cestas:.1f} kg":28} | {f"Café: {quant_cafe_total - (cestas * 2):.1f} kg":28} | {f"Feijão: {quant_feijao_total - (cestas * 4):.1f} kg":28} | {f"Sal: {quant_sal_total - cestas:.1f} kg":28} |')
    print(f'{f"| Arroz: {quant_arroz_total - (cestas * 4):.1f} kg":28} | {f"Extrato de Tomate: {quant_extrato_total - (cestas * 2):.1f} un":28} | {f"Macarrão: {quant_macarrao_total - (cestas * 3):.1f} un":28} | {f" ":28} |')
    print(f'{f"| Bolacha: {quant_bolacha_total - cestas:.1f} pct":28} | {f"Farinha de Trigo: {quant_farinha_total - cestas:.1f} kg":28} | {f"Óleo: {quant_oleo_total - cestas:.1f} L":28} | {f" ":28} |')

    # Caso as cestas tenham 1 item extra
elif quant_extras > 0 :
    print(f'{f"| Açúcar: {quant_acucar_total - cestas:.1f} kg":28} | {f"Café: {quant_cafe_total - (cestas * 2):.1f} kg":28} | {f"Feijão: {quant_feijao_total - (cestas * 4):.1f} kg":28} | {f"Sal: {quant_sal_total - cestas:.1f} kg":28} |')
    print(f'{f"| Arroz: {quant_arroz_total - (cestas * 4):.1f} kg":28} | {f"Extrato de Tomate: {quant_extrato_total - (cestas * 2):.1f} un":28} | {f"Macarrão: {quant_macarrao_total - (cestas * 3):.1f} un":28} | {f"Extras: {quant_extras_total} un":28} |')
    print(f'{f"| Bolacha: {quant_bolacha_total - cestas:.1f} pct":28} | {f"Farinha de Trigo: {quant_farinha_total - cestas:.1f} kg":28} | {f"Óleo: {quant_oleo_total - cestas:.1f} L":28} | {f" ":28} |')
