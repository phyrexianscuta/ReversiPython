from funcionesConvertirFichas import *
from funcionesAuxiliares import *
import copy
from random import shuffle

def winningPositions(player,symbolPlayer,newBoard,occupiedSpaces):
    if(noValidMoves(symbolPlayer[0],symbolPlayer,newBoard,occupiedSpaces) and noValidMoves(symbolPlayer[1],symbolPlayer,newBoard,occupiedSpaces)):
        number_other_ai = numberOfTiles(symbolPlayer[1],newBoard)
        number_ai_ver2 = numberOfTiles(symbolPlayer[0],newBoard)
        if(player == symbolPlayer[0] and (number_ai_ver2 > number_other_ai)):
            return True
        elif(player == symbolPlayer[1] and (number_other_ai > number_ai_ver2)):
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
        number_other_ai = numberOfTiles(symbolPlayer[1],newBoard)
        number_ai_ver2 = numberOfTiles(symbolPlayer[0],newBoard)
        if(number_other_ai == number_ai_ver2):
            return True
    return False

def evaluatingFunction(player,symbolPlayer,table,occupiedSpaces):
    opposing_ai = numberOfTiles(symbolPlayer[1],table)
    ai_ver2 = numberOfTiles(symbolPlayer[0],table)
    eval_mobility = evalMobility(player,symbolPlayer,table,occupiedSpaces)
    tile_difference = ai_ver2 - opposing_ai
    return (tile_difference)

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

def evalMobility(player,symbolPlayer,table,occupiedSpaces):
    count_available_moves_aiver2 = 0
    count_available_moves_opp_ai = 0
    adjacent_spaces = adjacentSpaces(table,occupiedSpaces)
    for position in adjacent_spaces:
        if (not doesntFlipAnyTile(symbolPlayer[0],symbolPlayer,position,table)):
            count_available_moves_aiver2 +=1
        if(not doesntFlipAnyTile(symbolPlayer[1],symbolPlayer,position,table)):
            count_available_moves_opp_ai +=1
    return (count_available_moves_aiver2 - count_available_moves_opp_ai)

def minimaxver2(table,player,symbolPlayer,occupiedSpaces,depth,regiones,regiones_ev,alpha,beta):
	depth +=1
	class MOVE:
		pass
	availSpots = availableSpots(table,player,symbolPlayer,occupiedSpaces)
	shuffle(availSpots)
	if(winningPositions(symbolPlayer[1],symbolPlayer,table,occupiedSpaces)):
		x=MOVE()
		x.score = depth-100
		return x
	elif(winningPositions(symbolPlayer[0],symbolPlayer,table,occupiedSpaces)):
		x=MOVE()
		x.score = +100-depth
		return x
	elif(draw(symbolPlayer,table,occupiedSpaces)):
		x=MOVE()
		x.score = 0
		return x
	elif(depth ==4 or len(availSpots)==0):
		x =MOVE()
		ev = evaluatingFunction(player,symbolPlayer,table,occupiedSpaces)
		x.score = ev
		return x
	bestMove = MOVE()
	if(player == symbolPlayer[1]):
		bestMove.score = +999
		for k in range(len(availSpots)):
			move = MOVE()
			move.index = availSpots[k]
			newBoard = copy.deepcopy(table)
			newBoard[availSpots[k][0]][availSpots[k][1]] = player
			occupiedSpaces.append(availSpots[k])
			makeMove(player,symbolPlayer,availSpots[k],newBoard)
			result = minimaxver2(newBoard,symbolPlayer[0],symbolPlayer,occupiedSpaces,depth,regiones,regiones_ev,alpha,beta)
			move.score = result.score
			move.score += evalPosition(move,regiones,regiones_ev)
			occupiedSpaces.remove(availSpots[k])
			if(move.score <= bestMove.score):
				bestMove.score = move.score
				bestMove.index = move.index
			beta = min(beta, bestMove.score)
			if(bestMove.score <= alpha):
				break
		return bestMove
	else:
		bestMove.score = -999
		for k in range(len(availSpots)):
			move = MOVE()
			move.index = availSpots[k]
			newBoard = copy.deepcopy(table)
			newBoard[availSpots[k][0]][availSpots[k][1]] = player
			occupiedSpaces.append(availSpots[k])
			makeMove(player,symbolPlayer,availSpots[k],newBoard)
			result = minimaxver2(newBoard,symbolPlayer[1],symbolPlayer,occupiedSpaces,depth,regiones,regiones_ev,alpha,beta)
			move.score = result.score
			move.score += evalPosition(move,regiones,regiones_ev)
			occupiedSpaces.remove(availSpots[k])
			if(move.score >= bestMove.score):
				bestMove.score = move.score
				bestMove.index = move.index
			alpha = max(alpha,bestMove.score)
			if(beta <= bestMove.score):
				break
		return bestMove