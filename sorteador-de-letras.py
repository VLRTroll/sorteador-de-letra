'''
Esta é uma mini interface gráfica de sorteio de letras
para uma adedonha. Com aparência limpa, esta aplcação
possui alguns mecanismos de configuração do sorteio.

1. Um botão seorteia a letra da rodada.
   A letra que é sorteada fica cinza, não podendo ser
sorteada novamente na rodada, a menos que o sorteio seja
reiniciado (item 4).
2. Caso os jogadores não desejem que uma letra seja
sorteada, bsata clicar em cima dela no mini alfabeto
para retirá-la do sorteio. Deixando-a vermelha.
   Do mesmo modo, para colocá-la novamente no sorteio
basta clicá-la novamente e esta retornará a ficar branca.
3. Se todas as letras forem sorteadas, uma mensagem de
aviso aparecerá avisando ao usuário do evento.
   E para reiniciar o sorteio basta apertar o segundo
botão com a escrita 'Reiniciar sorteio'.
'''

from tkinter import *
from random import *
import time

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfa = list(alfabeto)

#CORES DAS LETRAS DE VISUALIZAÇÃO DO ALFABETO
init_color = 'white'
select_color = 'red'
sorted_color = 'grey'

def clica(e):
    global alfa
    index = letrinhas.index(e.widget)

    if letrinhas[index]['foreground'] == sorted_color:
        return
    elif letrinhas[index]['foreground'] == init_color:
        letrinhas[index].configure(foreground = select_color)
        alfa.pop(alfa.index(alfabeto[index]))
    else:
        letrinhas[index].configure(foreground = init_color)
        alfa += alfabeto[index]
        texto.configure(text = '')

    if len(alfa) == 0:
        texto.configure(text = 'Todas as letras foram sorteadas!')
        letra['text'] = ''

def reload():
    global alfa
    alfa = list(alfabeto)

    texto.configure(text = '')
    letra['text'] = ''

    for i in range(0,len(letrinhas)):
        letrinhas[i].configure(foreground = init_color)
    
def sorteio():
    '''for i in range(0,3):
        letra.configure(text = i+1)
        time.sleep(0.5)'''
    global alfa

    if len(alfa) == 0:
        letra.configure(text = '')
        texto.configure(text = 'Todas as letras foram sorteadas!')
        return
    
    letter = randint(0,len(alfa)-1)
    letra.configure(text = alfa[letter])
    letrinhas[alfabeto.index(alfa[letter])].configure(foreground = sorted_color)
    alfa.pop(letter)

#============================JANELA============================#
janela = Tk()
janela.title('Sorteio da Adedonha')
janela.iconbitmap('a.ico')
#janela.geometry('200x200')
#print(dir(janela))

janela.maxsize(width = 380, height = 200)
janela.minsize(width = 380, height = 200)
#----------------------------X-X-X-X---------------------------#

#============================FUNDO=============================#
fHeight = 200
fWidth = 380

fundo = Frame(janela, width = fWidth, height = fHeight)
fundo.configure(background = '#123456')
fundo.pack()
#fundo.pack(expand = YES, fill = 'both')
#----------------------------X-X-X-X---------------------------#

#========================LETRA SORTEADA========================#
dist = 25
fHeight2 = fHeight - 2*dist
fWidth2 = 110

fundo_letra = Frame(fundo, width = fWidth2, height = fHeight2)
fundo_letra.configure(background = 'white', relief = 'raised', border = 10)
fundo_letra.place(x = dist, y = dist)

letra = Label(fundo_letra, text = '', foreground = 'green')
letra.configure(font = "Consolas 65 bold", background = 'white')
letra.configure(width = 1, height = 1)
letra.place(x = 16, y = 10)
#----------------------------X-X-X-X---------------------------#

#=======================BOTÕES DE SORTEIO======================#
distX = 2*dist + fWidth2

sorteio = Button(fundo, text = "Sortear Letra", width = 18, command = sorteio)
sorteio.configure(font = "Arial 12 bold")
sorteio.place(x = distX, y = dist)

reinicio = Button(fundo, text = "Reiniciar Sorteio", width = 18, command = reload)
reinicio.configure(font = "Arial 12 bold")
reinicio.place(x = distX, y = 3*dist)
#----------------------------X-X-X-X---------------------------#

#=========================TEXTO DE AVISO=======================#
texto = Label(fundo, text = "")
texto.configure(font = "Arial 10 bold", background = '#123456', foreground = 'red')
texto.place(x = 102.5, y = fHeight - dist)

#tam = ['195', '22+25+175']
'''tam = texto.winfo_geometry().split('x')
tam = int(tam[0])
print(tam)'''
#----------------------------X-X-X-X---------------------------#

#======================LETRAS SELECIONAVEIS====================#
letrinhas = []
distX2 = 15

for i in range(0,len(alfabeto)//2):
    letrinhas += [Label(fundo, text = alfabeto[i], font = "Consolas 12 bold")]
    letrinhas[i].configure(foreground = init_color, background = '#123456')
    letrinhas[i].bind("<Button-1>", clica)
    letrinhas[i].place(x = distX + i*distX2, y = 5*dist+4)

aux = len(alfabeto)//2
for i in range(0,len(alfabeto)-aux):
    letrinhas += [Label(fundo, text = alfabeto[i+aux], font = "Consolas 12 bold")]
    letrinhas[i+aux].configure(foreground = init_color, background = '#123456')
    letrinhas[i+aux].bind("<Button-1>", clica)
    letrinhas[i+aux].place(x = distX + i*distX2, y = 5*dist + 29)
#----------------------------X-X-X-X---------------------------#
input()

