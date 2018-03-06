
from funcionesConvertirFichas import *
from funcionesAuxiliares import *
from InteligenciaAI_ver2 import minimaxver2
import random

def initTable(table,occupiedSpaces):
    for i in range(8):
        table.append([])
        for j in range(8):
            table[i].append(" ")
    table[3][3] = "X"
    table[4][4] = "X"
    table[3][4] = "O"
    table[4][3] = "O"
    occupiedSpaces.append([3,3])
    occupiedSpaces.append([4,4])
    occupiedSpaces.append([3,4])
    occupiedSpaces.append([4,3])

corners = [[0,7],[7,0],[0,0],[7,7]]
region_celeste = []
region_azul = []
region_roja = [[1,0],[6,0],[0,1],[1,1],[6,1],[7,1],[0,6],[1,6],[6,6],[7,6],[1,7],[6,7]]
for i in range(0,2):
    for j in range(2,6):
        region_celeste.append([7*i,j])
        region_celeste.append([j,7*i])
        region_azul.append([5*i+1,j])
        region_azul.append([j,5*i+1])

region_verde = []
for i in range(2,6):
    for j in range(2,6):
        region_verde.append([i,j])

corners_ev = 10
region_celeste_ev = 5
region_verde_ev = 0
region_azul_ev = -5
region_roja_ev = -10

regiones = [corners,region_celeste,region_azul,region_roja,region_verde]
regiones_ev = [corners_ev,region_celeste_ev,region_azul_ev,region_roja_ev,region_verde_ev]

def playerStarts(symbolPlayer,table,playing,occupiedSpaces):
    print("You start the game using 'O' and the computer uses 'X'. Please press any button.")
    input()
    print(Tablero(table))
    player=symbolPlayer[1]
    computer = symbolPlayer[0]
    while(playing):
        if(playing and noValidMoves(player,symbolPlayer,table,occupiedSpaces) and noValidMoves(computer,symbolPlayer,table,occupiedSpaces)):
            playing = False
            finalCount(symbolPlayer,table)
        elif(playing and (not noValidMoves(player,symbolPlayer,table,occupiedSpaces))):
            humanMoves(symbolPlayer,table,occupiedSpaces)
            print("Your move:\n")
            print(Tablero(table))
        if(playing and noValidMoves(computer,symbolPlayer,table,occupiedSpaces) and noValidMoves(player,symbolPlayer,table,occupiedSpaces)):
            playing = False
            finalCount(symbolPlayer,table)
        elif(playing and (not noValidMoves(computer,symbolPlayer,table,occupiedSpaces))):
            computerMoves(symbolPlayer,table,occupiedSpaces)
            print("Computer moves:\n")
            print(Tablero(table))
            print('''-------------------------------------------------------------''')

def computerStarts(symbolPlayer,table,playing,occupiedSpaces):
    print("Computer moves first using 'O'. You are 'X'. Press any button.")
    input()
    print(Tablero(table))
    player = symbolPlayer[1]
    computer = symbolPlayer[0]
    while(playing):
        if(playing and noValidMoves(computer,symbolPlayer,table,occupiedSpaces) and noValidMoves(player,symbolPlayer,table,occupiedSpaces)):
            playing = False
            finalCount(symbolPlayer,table)
        elif(playing and (not noValidMoves(computer,symbolPlayer,table,occupiedSpaces))):
            print("Computer moves:\n")
            computerMoves(symbolPlayer,table,occupiedSpaces)
            print(Tablero(table))
        if(playing and noValidMoves(player,symbolPlayer,table,occupiedSpaces) and noValidMoves(computer,symbolPlayer,table,occupiedSpaces)):
            playing = False
            finalCount(symbolPlayer,table)
        elif(playing and (not noValidMoves(player,symbolPlayer,table,occupiedSpaces))):
            humanMoves(symbolPlayer,table,occupiedSpaces)
            print("Your move:\n")
            print(Tablero(table))
            print('''-------------------------------------------------------------''')

def humanMoves(symbolPlayer,table,occupiedSpaces):
    import re
    player = symbolPlayer[1]
    move = input("Please insert your move in 'n m' format:\nn m\n")
    while(incorrectMovement(player,symbolPlayer,move,table)):
        move = input("Please write your move as 'n m' with n and m numbers between 1 and 8.\nIt must be in an empty place of the board\nx x\n")
    myre = re.compile(r"\d{1}")
    position = myre.findall(move)
    makeMove(symbolPlayer[1],symbolPlayer,[int(position[0])-1,int(position[1])-1],table)
    occupiedSpaces.append([int(position[0])-1,int(position[1])-1])

def computerMoves(symbolPlayer,table,occupiedSpaces):
    bestMove = minimaxver2(table,symbolPlayer[0],symbolPlayer,occupiedSpaces,0,regiones,regiones_ev,-999,999).index
    makeMove(symbolPlayer[0],symbolPlayer,bestMove,table)
    occupiedSpaces.append(bestMove)

def Jugar():
    print("Welcome to Reversi!\nX is black, O is white.")
    table =[]
    occupiedSpaces =[]
    initTable(table,occupiedSpaces)
    playing = True
    if (random.randint(0,1)==0):
        symbolPlayer = ["X","O"]
        playerStarts(symbolPlayer,table,playing,occupiedSpaces)
    else:
        symbolPlayer = ["O","X"]
        computerStarts(symbolPlayer,table,playing,occupiedSpaces)
    jugar_de_nuevo = input("Do you want to play again? yes/no").lower()
    if(jugar_de_nuevo[0]=="y"):
        Jugar()
    else:
        print("Thanks for playing!")
        input()

Jugar()