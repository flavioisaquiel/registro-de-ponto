
from datetime import datetime
import PySimpleGUI as sg


class TelaPython:

    def __init__(self):

        # layout
        layout = [
            # Iniciando o ponto
            [sg.Text('nome', size=(5, 0))],
            [sg.Input('Digite seu nome', key='-nome-',
                      do_not_clear=False, size=(100, 0))],
            [sg.Input(datetime.now() .strftime(
                '%d/%m/%Y, às %H:%M:%S'), size=(20, 0), key='data_hora')],
            [sg.Button('Enviar', key='enviar'), sg.Button(
                'Finalizar', key='finalizar'), sg.Button('Sair', key='sair')],
            [sg.Output(size=(200, 100))],
        ]
        # janela
        self.janela = sg.Window('Controle de horas',
                                size=(400, 300)).layout(layout)

    def iniciar(self):

        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.read()

            name = self.values['-nome-']
            registro = self.values['data_hora']

            if self.button == 'sair':
                self.janela.exit()

            if name == '':
                print('Digite um nome')

            elif self.button == 'enviar':
                print(f'{name}, Entrou no dia : {registro}')

            elif self.button == 'finalizar':
                print(f'{name}, Finalizou : {registro}')


tela = TelaPython()
tela.iniciar()
