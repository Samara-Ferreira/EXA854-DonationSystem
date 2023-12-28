"""
    Autor(a): Samara dos Santos Ferreira
    Componente Curricular: MI - Algoritmos e Programação I
    Concluído em: 09/04/2022
    Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de colega ou de outro autor, tais como 
    provindos de livros e apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código de outra autoria que não a minha 
    está destacado com uma citação do autor e a fonte do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""

# ------------------ IMPORTAÇÕES ------------------ #
# Função system utilizada para limpar o terminal a cada utilização do programa
from os import system # Fonte: https://github.com/python/cpython/blob/3.11/Lib/os.py

system("cls")


# ------------------ FUNÇÕES COMPLEMENTARES ------------------ #

# Procedimento para imprimir o Livro de Registros
def imprimeLivroRegistros():
    print("\n\n", "-=" * 20, f"\n{f'LIVRO DE REGISTROS':^40}\n", "-=" * 20, "\n")

    i = 0   # Percorrer os doadores
    j = 0   # Percorrer os dados de cada doador

    for chave in livroRegistro.keys():
        i += 1

        print(f"{f'        NOME DO DOADOR {i}: {chave}':40}\n", "--" * 20)
        print(f"{f'|  Contato: {livroRegistro[chave][i]}':40} |")
        j += 1

        # Separa os tipos de doadores pelo índice
        if (livroRegistro[chave][i] == 1):
            print(f"{f'|  Tipo: Pessoa Física':40} |")
        else:
            print(f"{f'|  Tipo: Pessoa Jurídica':40} |")
        j += 1

        # Separa os tipos de doadores pelo índice
        if (livroRegistro[chave][j] == 1):
            print(f"{f'|  Horário da Doação: Manhã':40} |")
        else:
            print(f"{f'|  Horário da Doação: Tarde':40} |")
        j += 1

        # Separa os dias de doação pelo índice
        if (livroRegistro[chave][i] == 1):
            print(f"{f'|  Dia da Doação: Comercial':40} |\n")
        else:
            print(f"{f'|  Dia da Doação: Fim de Semana':40} |\n")
        
        # Reseta a variável para mostrar os dados do outro doador (caso tenha)
        j = 0
  
# Procedimento para imprimir o relatório final/parcial
def imprimeRelatorio(frase, itensCesta):
    print("\n", "-=" * 20, f"\n{f'RELATÓRIO {frase}':^40}\n", "-=" * 20, "\n")
    
    print(f"{'        TOTAL DE CADA ITEM RECEBIDO':40}\n", "--" * 20)
    for chave in alimentosDoados.keys():
        if (chave == "Açúcar" or chave == "Café" or chave == "Feijão" or chave == "Sal" or chave == "Arroz" or chave == "Farinha de Trigo"):
            un = "kg"
        elif (chave == "Extrato de Tomate" or chave == "Macarrão"):
            un = "un"
        elif (chave == "Bolacha"):
            un = "pct"
        elif (chave == "Óleo"):
            un = "L"
        elif (chave == "Extras"):
            un = ""
        print(f"{f'|  {chave} = {alimentosDoados[chave]} {un}':40} |")

    print(f"\n{'   TOTAL DE ITENS RECEBIDOS POR PESSOA':40}\n", "--" * 20)
    fisicas = doacoesPessoa["Físicas"]
    juridicas = doacoesPessoa["Jurídicas"]
    print(f"{f'|  Físicas: {fisicas} doação(es) ':40} |")
    print(f"{f'|  Jurídicas: {juridicas} doação(es) ':40} |")

    print(f"\n{'   TOTAIS DAS CESTAS BÁSICAS FORMADAS':40}\n", "--" * 20)
    formadas = cestas["Formadas"]
    comExtra = cestas["Com Extra"]
    semExtra = cestas["Sem Extra"]

    print(f"{f'|  Total de Cestas: {formadas} ':40} |")
    print(f"{f'|  Com Extra: {comExtra} cestas ':40} |")
    print(f"{f'|  Sem Extra: {semExtra} cestas ':40} |")


    print(f"\n{'    TOTAL DOS ITENS QUE SOBRARAM':40}\n", "--" * 20)

    cont = 0   # Contar quantos itens sobraram 

    for chave in itensCesta.keys():
        if (itensCesta[chave] > 0):
            if (chave == "Açúcar" or chave == "Café" or chave == "Feijão" or chave == "Sal" or chave == "Arroz" or chave == "Farinha de Trigo"):
                un = "kg"
            elif (chave == "Extrato de Tomate" or chave == "Macarrão"):
                un = "un"
            elif (chave == "Bolacha"):
                un = "pct"
            elif (chave == "Óleo"):
                un = "L"
            elif (chave == "Extras"):
                un = ""
            print(f"{f'|  {chave} = {itensCesta[chave]} {un}':40} |")
            cont += 1
    
    # Caso não tenha itens sobrando, é impresso na tela essa mensagem
    if (cont == 0):
        print(f"{f'|  0 itens':40} |")

# Função que forma as cestas báiscas
def formaCestas():
    # Cópia do dicionário principal, que contém a quantidade de cada alimento doado
    itensCesta = dict(alimentosDoados)

    totalCestas = 0
    contadora = 0
    continuar = 1

    while (continuar == 1):
        for chave in itensCesta.keys():
            if (itensCesta[chave] > 0 and chave != "Extras"):
                contadora += 1

            # Quando um item obrigatório for igual a zero, o programa deve finalizar e a cesta não será formada
            else:
                continuar = 2
                break
        
        if (continuar != 2 and contadora == 10):
            # Desconta a quantidade de alimentos que formaram a cesta
            itensCesta["Açúcar"] -= 1
            itensCesta["Bolacha"] -= 1
            itensCesta["Óleo"] -= 1
            itensCesta["Farinha de Trigo"] -= 1
            itensCesta["Sal"] -= 1
            itensCesta["Arroz"] -= 4
            itensCesta["Feijão"] -= 4
            itensCesta["Café"] -= 2
            itensCesta["Extrato de Tomate"] -= 2
            itensCesta["Macarrão"] -= 3

            totalCestas += 1
            contadora = 0

    quantCestas = totalCestas
    # Adiciona 1 item extra em cada cesta
    while (itensCesta["Extras"] > 0 and quantCestas > 0):
        itensCesta["Extras"] -= 1
        quantCestas -= 1

    cestas["Formadas"] = totalCestas
    cestas["Com Extra"] = totalCestas - quantCestas
    cestas["Sem Extra"] = quantCestas

    return itensCesta

# Função que verifica se as entradas inseridas pelo usuário são corretas
def validaInformacoes(tipo, frase, loop, max):
    # Caso a variável seja do tipo int
    if (tipo == 'int'):
        valida = 's'
        while (type(valida) is not int):
            try: 
                valida = int(input("%s" % frase))
            except:
                print("\n\tOpção Inválida!")
            else:
                if (loop != 'false'):
                    if (valida < 1 or valida > max):
                        print("\n\tDigite uma opção entre %s (incluindo eles)!" % loop)
                        valida = 's'

    # Caso a variável seja do tipo str
    else:
        valida = 1
        while (type(valida) is not str):
            try:
                valida = str(input("%s" % frase))        
            except:
                print("\n\tOpção Inválida!")

    return valida        


# ------------------ FUNÇÃO PRINCIPAL ------------------ #

print(" -------> SEJA BEM-VINDO(A) AO DISPENSÁRIO SANTANA!")

# Dicionário que guarda os nomes dos alimentos, junto com o seu respectivo índice
nomesAlimentos = {1: "Açúcar", 2: "Arroz", 3: "Café", 4: "Extrato de Tomate", 5: "Macarrão", 6: "Bolacha", 7: "Óleo", 8: "Farinha de Trigo", 9: 
"Feijão", 10: "Sal", 11: "Extras"}

# Dicionário que guarda a quantidade de cada alimento
alimentosDoados = {"Açúcar": 0, "Arroz": 0, "Café": 0, "Extrato de Tomate": 0, "Macarrão": 0, "Bolacha": 0, "Óleo": 0, "Farinha de Trigo": 0, 
"Feijão": 0, "Sal": 0, "Extras": 0}


# Dicionário que guarda o nome e o contato do doador 
livroRegistro = {}

# Dicionário que guarda a quantidade de itens doados por pessoas físicas e jurídicas
doacoesPessoa = {"Físicas": 0, "Jurídicas": 0}

# Dicionário que guarda a quantidade de cestas formadas, com itens extras e sem itens extras
cestas = {"Formadas": 0, "Com Extra": 0, "Sem Extra": 0}


# Opção para inicializar ou não o sistema
continuar = validaInformacoes('int', '\n  Deseja incializar o sistema? \n[1] Sim \t[2] Não \n\t>> ', '1 e 2', 2)
if (continuar == 2):
    continuar = 3

# Caso o sistema seja iniciado
while (continuar == 1  or continuar == 2):
    # Nome do doador e sua respectiva validação
    nomeDoador = validaInformacoes('str', '\n  Digite o nome do doador: ', 'false', 0)

    # Contato do doador (número de telefone) e a sua respectiva validação 
    contatoDoador = validaInformacoes('int', '\n  Digite o contato do doador: ', 'false', 0)

    # Tipo de doador (pessoa física ou jurídica) e sua respectiva validação
    tipoDoador = validaInformacoes('int', '\n  Digite o tipo de doador: \n[1] Física \t[2] Jurídica \n\t>> ', '1 e 2', 2)

    # Horário de doação (turno matutino ou vespertino) e sua respectiva validação 
    horarioDoacao = validaInformacoes('int', '\n  Digite o horário da doação: \n[1] Manhã \t[2] Tarde \n\t>> ', '1 e 2', 2)

    # Dia de doação (comercial ou fim de semana) e sua respectiva validação
    diaDoacao = validaInformacoes('int', '\n  Digite o dia da doação: \n[1] Comercial \t[2] Fim de Semana \n\t>> ', '1 e 2', 2)
            
    livroRegistro.update({nomeDoador:[contatoDoador, tipoDoador, horarioDoacao, diaDoacao]})

    # --- Cadastro de Alimentos --- #
    continuarAli = 1
    while (continuarAli == 1):
        # Armazena a quantidade de doações de pessoas físicas e jurídicas
        if (tipoDoador == 1):
            doacoesPessoa["Físicas"] += 1
        else:
            doacoesPessoa["Jurídicas"] += 1

        tipoItem = validaInformacoes('int', '\n  Digite o tipo de alimento: \n[1] Açúcar \t[2] Arroz \n[3] Café \t[4] Extrato de Tomate \n[5] Macarrão \t[6] Bolacha \n[7] Óleo \t[8] Farinha de Trigo \n[9] Feijão \t[10] Sal \n[11] Extras \n\t>> ', '1 e 11', 11)

        # Pega o nome do item a partir do índice 
        nome = nomesAlimentos[tipoItem]

        quantItem = validaInformacoes('int', '\n  Digite a quantidade de %s: ' % nome, 'false', 0)

        # Atualiza a quantidade daquele alimento no dicionário
        alimentosDoados[nome] += quantItem

        # Condição para continuar ou não o cadastro dos itens
        continuarAli = validaInformacoes('int', '\n  Deseja cadastrar um alimento? \n[1] Sim \t[2] Não \n\t>> ', '1 e 2', 2)


    # Condição para saber se o sistema continuará rodando 
    continuar = validaInformacoes('int', '\n  O que deseja fazer agora? \n[1] Cadastrar outro doador \n[2] Visualizar o relatório parcial \n[3] Visualizar o relatório final \n\t>> ', '1 e 3', 3)

    if (continuar == 2):
        itensCesta = formaCestas()
        imprimeRelatorio('PARCIAL', itensCesta)
    
    elif (continuar == 3):
        itensCesta = formaCestas()
        imprimeRelatorio('FINAL', itensCesta)
        imprimeLivroRegistros() 

print("\n SISTEMA FINALIZADO! <------- ")
