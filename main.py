import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='selecione uma pasta')

ListaDeArquivos = os.listdir(caminho)

locais = {
    'imagens': ['.png','.jpg'],
    'planilhas': ['.xlsx'],
    'pdfs': ['.pdf'],
    'csv': ['.csv'],
}

for arquivo in ListaDeArquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho/{arquivo}}', f'{caminho}/{pasta}/{arquivo}')    