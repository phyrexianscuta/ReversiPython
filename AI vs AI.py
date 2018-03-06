from funcionesAuxiliares import *
from InteligenciaAI_ver1 import *
from InteligenciaAI_ver2 import *
import time

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

def oldAIStarts(symbolPlayer,table,playing,occupiedSpaces,new_ai_finalcount,old_ai_finalcount,empate):
    ai_ver2 = symbolPlayer[0]
    ai_ver1 = symbolPlayer[1]
    while(playing):
        if(playing and noValidMoves(ai_ver2,symbolPlayer,table,occupiedSpaces) and noValidMoves(ai_ver1,symbolPlayer,table,occupiedSpaces)):
            playing = False
            if(numberOfTiles(ai_ver1,table)> numberOfTiles(ai_ver2,table)):
                ai_ver1_finalcount[0] +=1
            elif(numberOfTiles(ai_ver1,table)< numberOfTiles(ai_ver2,table)):
                ai_ver2_finalcount[0] +=1
            elif(numberOfTiles(ai_ver1,table)==numberOfTiles(ai_ver2,table)):
                empate[0] +=1
        elif(playing and (not noValidMoves(ai_ver1,symbolPlayer,table,occupiedSpaces))):
            AI_ver1(symbolPlayer,table,occupiedSpaces)
            print("Juega la version 1:\n", Tablero(table))
        if(playing and noValidMoves(ai_ver2,symbolPlayer,table,occupiedSpaces) and noValidMoves(ai_ver1,symbolPlayer,table,occupiedSpaces)):
            playing = False
            if(numberOfTiles(ai_ver1,table)> numberOfTiles(ai_ver2,table)):
                ai_ver1_finalcount[0] +=1
            elif(numberOfTiles(ai_ver1,table)< numberOfTiles(ai_ver2,table)):
                ai_ver2_finalcount[0] +=1
            elif(numberOfTiles(ai_ver1,table)==numberOfTiles(ai_ver2,table)):
                empate[0] +=1
        elif(playing and (not noValidMoves(ai_ver2,symbolPlayer,table,occupiedSpaces))):
            AI_ver2(symbolPlayer,table,occupiedSpaces)
            print("Juega la version 2:\n", Tablero(table))

def newAIStarts(symbolPlayer,table,playing,occupiedSpaces,ai_ver2_finalcount,ai_ver1_finalcount,empate):
    ai_ver2 = symbolPlayer[0]
    ai_ver1 = symbolPlayer[1]
    while(playing):
        if(playing and noValidMoves(ai_ver2,symbolPlayer,table,occupiedSpaces) and noValidMoves(ai_ver1,symbolPlayer,table,occupiedSpaces)):
            playing = False
            if(numberOfTiles(ai_ver1,table)> numberOfTiles(ai_ver2,table)):
                ai_ver1_finalcount[0] +=1
            elif(numberOfTiles(ai_ver1,table)< numberOfTiles(ai_ver2,table)):
                ai_ver2_finalcount[0] +=1
            elif(numberOfTiles(ai_ver1,table)==numberOfTiles(ai_ver2,table)):
                empate[0] +=1
        elif(playing and (not noValidMoves(ai_ver2,symbolPlayer,table,occupiedSpaces))):
            AI_ver2(symbolPlayer,table,occupiedSpaces)
            print("Juega la version 2:\n", Tablero(table))
        if(playing and noValidMoves(ai_ver2,symbolPlayer,table,occupiedSpaces) and noValidMoves(ai_ver1,symbolPlayer,table,occupiedSpaces)):
            playing = False
            if(numberOfTiles(ai_ver1,table)> numberOfTiles(ai_ver2,table)):
                ai_ver1_finalcount[0] +=1
            elif(numberOfTiles(ai_ver1,table)< numberOfTiles(ai_ver2,table)):
                ai_ver2_finalcount[0] +=1
            elif(numberOfTiles(ai_ver1,table)==numberOfTiles(ai_ver2,table)):
                empate[0] +=1
        elif(playing and (not noValidMoves(ai_ver1,symbolPlayer,table,occupiedSpaces))):
            AI_ver1(symbolPlayer,table,occupiedSpaces)
            print("Juega la version 1:\n", Tablero(table))

def AI_ver1(symbolPlayer,table,occupiedSpaces):
    depth = 0
    starti=time.time()
    bestMove = minimaxver1(table,symbolPlayer[1],symbolPlayer,occupiedSpaces,depth,regiones,regiones_ev).index
    endi=time.time()
    print(endi - starti)
    table[bestMove[0]][bestMove[1]] = symbolPlayer[1]
    occupiedSpaces.append(bestMove)
    makeMove(symbolPlayer[1],symbolPlayer,bestMove,table)

def AI_ver2(symbolPlayer,table,occupiedSpaces):
    depth = 0
    starti=time.time()
    bestMove = minimaxver2(table,symbolPlayer[0],symbolPlayer,occupiedSpaces,depth,regiones,regiones_ev,-999,999).index
    endi=time.time()
    print(endi - starti)
    table[bestMove[0]][bestMove[1]] = symbolPlayer[0]
    occupiedSpaces.append(bestMove)
    makeMove(symbolPlayer[0],symbolPlayer,bestMove,table)

ai_ver2_finalcount = [0]
ai_ver1_finalcount = [0]
empate = [0]

for l in range(1):
    table = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," ","X","X"," "," "],
[" "," ","O","X","X","O"," "," "],[" "," ","O","X","O"," "," "," "],["O","O","O","O"," "," "," "," "],
[" "," ","O"," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
    occupiedSpaces  = []
    for i in range(8):
        for j in range(8):
            if(table[i][j] !=" "):
                occupiedSpaces.append([i,j])
    print(Tablero(table))
    newAIStarts(["X","O"],table,True,occupiedSpaces,ai_ver2_finalcount,ai_ver1_finalcount,empate)
    print("ai_ver2:",ai_ver2_finalcount,"\nai_ver1:",ai_ver1_finalcount,"\nempate:",empate,"score ai_ver1-ai_ver2:\n",numberOfTiles("O",table),"-",numberOfTiles("X",table))