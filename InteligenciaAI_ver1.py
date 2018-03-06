from funcionesConvertirFichas import *
from funcionesAuxiliares import *
import copy
import random

def winningPositions(player,symbolPlayer,newBoard,occupiedSpaces):
    if(noValidMoves(symbolPlayer[0],symbolPlayer,newBoard,occupiedSpaces) and noValidMoves(symbolPlayer[1],symbolPlayer,newBoard,occupiedSpaces)):
        numberComputer = numberOfTiles(symbolPlayer[1],newBoard)
        numberHuman = numberOfTiles(symbolPlayer[0],newBoard)
        if(player == symbolPlayer[0] and (numberHuman > numberComputer)):
            return True
        elif(player == symbolPlayer[1] and (numberComputer > numberHuman)):
            return True
    return False

def availableSpots(newBoard,player,symbolPlayer,occupiedSpaces):
    adjacent_Spots = adjacentSpaces(newBoard,occupiedSpaces)
    to_remove = []
    for position in adjacent_Spots:
        if doesntFlipAnyTile(player,symbolPlayer,position,newBoard):
            to_remove.append(position)
    for x in to_remove:
        adjacent_Spots.remove(x)
    return adjacent_Spots

def draw(symbolPlayer,newBoard,occupiedSpaces):
    if(noValidMoves(symbolPlayer[0],symbolPlayer,newBoard,occupiedSpaces) and noValidMoves(symbolPlayer[1],symbolPlayer,newBoard,occupiedSpaces)):
        numberComputer = numberOfTiles(symbolPlayer[1],newBoard)
        numberHuman = numberOfTiles(symbolPlayer[0],newBoard)
        if(numberHuman == numberComputer):
            return True
    return False

def evaluatingFunction(newBoard,symbolPlayer):
    other_player = numberOfTiles(symbolPlayer[0],newBoard)
    myself = numberOfTiles(symbolPlayer[1],newBoard)
    return (myself- other_player)

def evalPosition(move,regiones,regiones_ev):
    position = move.index
    if(position in regiones[4]):
        return regiones_ev[4]
    elif(position in regiones[2]):
        return regiones_ev[2]
    elif(position in regiones[1]):
        return regiones_ev[1]
    elif(position in regiones[3]):
        return regiones_ev[3]
    elif(position in regiones[0]):
        return regiones_ev[0]

def minimaxver1(table,player,symbolPlayer,occupiedSpaces,depth,regiones,regiones_ev):
    depth +=1
    class MOVE:
        pass
    availSpots = availableSpots(table,player,symbolPlayer,occupiedSpaces)
    if(winningPositions(symbolPlayer[0],symbolPlayer,table,occupiedSpaces)):
        x=MOVE()
        x.score = depth-100
        return x
    elif(winningPositions(symbolPlayer[1],symbolPlayer,table,occupiedSpaces)):
        x=MOVE()
        x.score = +100-depth
        return x
    elif(draw(symbolPlayer,table,occupiedSpaces)):
        x=MOVE()
        x.score = 0
        return x
    elif(depth ==4 or len(availSpots)==0):
        x =MOVE()
        ev = evaluatingFunction(table,symbolPlayer)
        x.score = ev
        return x
    moves = []
    for k in range(len(availSpots)):
        move = MOVE()
        move.index = availSpots[k]
        newBoard = copy.deepcopy(table)
        newBoard[availSpots[k][0]][availSpots[k][1]] = player
        occupiedSpaces.append(availSpots[k])
        makeMove(player,symbolPlayer,availSpots[k],newBoard)
        if(player == symbolPlayer[1]):
            result = minimaxver1(newBoard,symbolPlayer[0],symbolPlayer,occupiedSpaces,depth,regiones,regiones_ev)
            move.score = result.score
            move.score += evalPosition(move,regiones,regiones_ev)
        else:
            result = minimaxver1(newBoard,symbolPlayer[1],symbolPlayer,occupiedSpaces,depth,regiones,regiones_ev)
            move.score = result.score
            move.score += evalPosition(move,regiones,regiones_ev)
        occupiedSpaces.remove([availSpots[k][0],availSpots[k][1]])
        moves.append(move)
    if(player==symbolPlayer[1]):
        bestScore = max([moves[l].score for l in range(len(moves))])
    else:
        bestScore = min([moves[l].score for l in range(len(moves))])
    indexes_bestScore =[i for i,j in enumerate(moves) if j.score== bestScore]
    sss=random.choice(indexes_bestScore)
    return moves[sss]