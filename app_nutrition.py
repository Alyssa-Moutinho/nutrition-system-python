import os

fatores_atividade_fisica = {'sedentário': 1.12, 'leve': 1.2, 'moderado': 1.3, 'intenso': 1.55}

pacientes = []

def exibir_menu():
    print('\033[34mSISTEMA DE NUTRIÇÃO\033[m')
    print('-=-' * 12)
    print('\n[1] Cadastrar paciente\n')
    print('[2] Consultar IMC e classificação\n')
    print('[3] Consultar calorias\n')
    print('[4] Listar pacientes\n')
    print('[5] Sair do programa\n')
    print('-=-' * 12)

def cadastrar_pacientes(): 
    print('\033[34mCadastro do paciente\033[m')
    print('-=-' * 12)
    while True: 
        nome = input('Digite o nome: ').strip().lower()
        if nome: 
            break
        print('\033[31mInválido, digite novamente!\033[m')
    while True: 
        try:
            idade = int(input('Digite a idade: '))
            if idade > 0: 
                break
            else: 
                print('Idade deve ser maior que 0.')
        except ValueError: 
            print('Digite um número inteiro válido.')

    while True:
        genero = input('Digite o gênero: (F) ou (M): ').strip().lower()
        if genero in ['f','m']:
            break
        print('Digite apenas F ou M')

    while True: 
        try:
            altura = float(input('Digite a altura em metros: ').strip().replace(',', '.'))
            if altura > 0: 
                break
            else: 
                print('Altura deve ser maior que 0.')
        except ValueError: 
            print('Digite uma altura válida')
    while True: 
        try:        
            peso = float(input('Digite o peso em kg: ').strip().replace(',', '.'))
            if peso > 0: 
                break
            else: 
                print('Peso deve ser maior que 0.')
        except ValueError: 
            print('Digite um peso válido.')

    while True: 
        print('\033[34m\nNíveis de atividade física:\033[m')
        print('Sedentário | Leve | Moderado | Intenso')
        print('-' * 40)
        nivel_atividade_fisica = input('Digite o seu nível: ').strip().lower()
        if nivel_atividade_fisica in fatores_atividade_fisica:
            break
        else: 
            print('\033[31mOpção inválida.\033[m] Digite exatamente como informado: ')

    paciente = {'nome': nome, 'idade': idade, 'genero': genero, 'altura': altura, 'peso': peso, 'atividade': nivel_atividade_fisica}
    pacientes.append(paciente) 
    print('\033[32m\nPaciente cadastrado com sucesso!\033[m')

def calcular_imc(): 
    print('\033[34m\nConsulta do IMC\033[m')
    print('-=-' * 12)
    nome = input('Digite o nome do paciente: ').strip().lower()
    for paciente in pacientes: 
        if paciente['nome'] == nome: 
            peso = paciente['peso']
            altura = paciente['altura']
            imc = peso / (altura ** 2)
            print(f'\nO IMC do(a) {nome.capitalize()} é {imc:.1f} kg/m²')
            print(f'\nClassificação do IMC do(a) {nome.capitalize()}: ', end = '')
            if imc < 18.5: 
                print('Baixo peso\n')
            elif 18.5 <= imc < 25: 
                print('Peso normal\n')
            elif 25 <= imc < 30: 
                print('Sobrepeso\n')
            elif 30 <= imc < 35: 
                print('Obesidade grau I\n')
            elif 35 <= imc < 40: 
                print('Obesidade grau II\n')
            elif imc >= 40: 
                print('Obesidade grau III\n')
            return
    print('\033[31m\nPaciente não encontrado.\033[m Faça o cadastro')

def calcular_calorias(): 
    print('\033[34mCalorias diárias\033[m')
    print('-=-' * 12)
    nome = input('Digite o nome do paciente: ').strip().lower()
    
    for paciente in pacientes:
        if paciente['nome'] == nome and paciente['genero'] == 'f':
            idade = paciente['idade']
            peso = paciente['peso']
            altura_cm = paciente['altura'] * 100
            nivel_atividade = paciente['atividade']
            fator_atividade = fatores_atividade_fisica[nivel_atividade]
            gasto_energetico_mulheres = 655 + (9.6 * peso) + (1.8 * altura_cm) - (4.7 * idade)
            calorias_totais_mulheres = gasto_energetico_mulheres * fator_atividade

            print(f'\nO gasto energético diário da {nome.capitalize()} é {gasto_energetico_mulheres}kcal')
            print(f'\nAs calorias diárias totais da {nome.capitalize()} com o fator de atividade de {fator_atividade} considerado um nível {nivel_atividade} é de {calorias_totais_mulheres:.1f}kcal\n')
            return
        
        elif paciente['nome'] == nome and paciente['genero'] == 'm':
            idade = paciente['idade']
            peso = paciente['peso']
            altura_cm = paciente['altura'] * 100
            nivel_atividade = paciente['atividade']
            fator_atividade = fatores_atividade_fisica[nivel_atividade]
            gasto_energetico_homens = 66 + (13.7 * peso) + (5 * altura_cm) - (6.8 * idade)
            calorias_totais_homens = gasto_energetico_homens * fator_atividade

            print(f'\nO gasto energético diário do {nome.capitalize()} é {gasto_energetico_homens}kcal')
            print(f'\nAs calorias diárias totais do {nome.capitalize()} com o fator de atividade de {fator_atividade} considerado um nível {nivel_atividade} é de {calorias_totais_homens:.1f}kcal\n')
            return
     
    print('\033[31mPaciente não encontrado.\033[m Faça o cadastro')
        
            
def listar_pacientes(): 
    print('\033[34mLista dos pacientes\033[m')
    print('-=-' * 12)
    for paciente in pacientes: 
        nome_paciente = paciente['nome']
        idade_paciente = paciente['idade']
        altura_paciente = paciente['altura']
        peso_paciente = paciente['peso']
        atividade_paciente = paciente['atividade']
        if paciente['genero'] == 'f': 
            genero_paciente = 'feminino'
        elif paciente['genero'] == 'm': 
            genero_paciente = 'masculino'
        print(f'{nome_paciente.title()} | {idade_paciente} anos | {genero_paciente.ljust(5)} | {altura_paciente}m | {peso_paciente}kg | Atividade: {atividade_paciente}\n')


def main():
    while True: 
        os.system('cls')
        exibir_menu()

        try:
            opcao = int(input('\nEscolha sua opção: '))
        except ValueError: 
            print('\033[31mErro.\033[m Digite uma opção válida.')
            input('Pressione enter para voltar ao menu.')
            continue

        match opcao: 
            case 1: 
                os.system('cls')
                cadastrar_pacientes()
                input('Pressione enter para voltar ao menu.')
            case 2: 
                os.system('cls')
                calcular_imc()
                input('Pressione enter para voltar ao menu.')
            case 3: 
                os.system('cls')
                calcular_calorias()
                input('Pressione enter para voltar ao menu.')
            case 4: 
                os.system('cls')
                listar_pacientes()
                input('Pressione enter para voltar ao menu.')
            case 5: 
                os.system('cls')
                print('\033[33m\nSaindo do programa...\033[m')
                break
            case _: 
                print('\033[31mOpção inválida\033[m')
                input('Pressione enter para voltar ao menu.')
main()
               
    
    
