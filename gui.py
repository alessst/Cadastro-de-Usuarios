import PySimpleGUI as sg
from salva_usuario import SalvaDados


def cria_layout():
    layout = [  [sg.Text('Digite o Nome:', size=(15,1)), sg.InputText(key="nome", size=(50))],
                [sg.Text('Digite a Idade:', size=(15,1)), sg.InputText(key="idade", size=(5))],
                [sg.Text('Digite o Endereço:', size=(15,1)), sg.InputText(key="endereco", size=(50))],
                [sg.Text('Digite a CPF:', size=(15,1)), sg.InputText(key="cpf", size=(12))],
                [sg.Text('Digite a Email:', size=(15,1)), sg.InputText(key="email",size=(50))],
                [sg.Button('Salvar'), sg.Button('Cancelar'), sg.Button('Novo Cadastro')], 
                [sg.Text('', key='dados')]]

    return sg.Window('Cadastros de Usuario', layout)

janela = cria_layout()


while True:
    evento, valores = janela.read()

    nome = valores['nome']
    idade = valores['idade']
    endereco = valores['endereco']
    cpf = valores['cpf']
    email = valores['email']
    button_salvar = 'Salvar'
    button_cancelar = 'Cancelar'
    button_novo = 'Novo Cadastro'
    
    if evento == sg.WIN_CLOSED or evento == button_cancelar: 
        break
    if evento == button_salvar:
        save = SalvaDados(nome, idade, endereco, cpf, email)
        save.salvar()
        janela['dados'].update(f'Usuario ({nome}) está salva no Banco de dados: \nNome: {nome} \nIdade: {idade}\nEndereço: {endereco} \nCPF: {cpf} \nEmail: {email}')
    if evento == button_novo:
        janela.close()
        janela = cria_layout()
       
        

janela.close()