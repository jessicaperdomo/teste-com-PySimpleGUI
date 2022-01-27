import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        # Layout

        layout = [
            [sg.Text('Nome'), sg.Input(key='nome')],
            [sg.Text('Sexo')],
            [sg.Checkbox('Feminino', key='fem'), sg.Checkbox(
                'Masculino', key='mas'), sg.Checkbox('Outro/Não desejo especificar', key='out')],
            [sg.Text('Idade'), sg.Input(key='idade')],
            [sg.Text('Endereço'), sg.Input(key='endereco')],
            [sg.Text('Celular'), sg.Input(key='cel')],
            [sg.Text('E-mail'), sg.Input(key='email')],
            [sg.Button('Enviar Dados')],
        ]
        # Janela
        janela = sg.Window("Formulário de Cadastro").layout(layout)
        # Extrair dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values['nome']
        fem = self.values['fem']
        mas = self.values['mas']
        outros = self.values['out']
        idade = self.values['idade']
        end = self.values['endereco']
        celular = self.values['cel']
        email = self.values['email']
        print(f'nome: {nome}')
        print(f'fem: {fem}')
        print(f'mas: {mas}')
        print(f'outros: {outros}')
        print(f'idade: {idade}')
        print(f'end: {end}')
        print(f'celular: {celular}')
        print(f'email: {email}')


tela = TelaPython()
tela.Iniciar()
