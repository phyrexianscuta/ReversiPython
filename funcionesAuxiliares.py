import copy

def Tablero(array):
    table ="       1   2   3   4   5   6   7   8\n"
    for i in range(8):
        table +='''     +---+---+---+---+---+---+---+---+
     |   |   |   |   |   |   |   |   |
   %s | %s | %s | %s | %s | %s | %s | %s | %s |
     |   |   |   |   |   |   |   |   |
'''%(i+1,array[0][i],array[1][i],array[2][i],array[3][i],array[4][i],array[5][i],array[6][i],array[7][i])
    table+="     +---+---+---+---+---+---+---+---+"
    return table

def symbolChoice():
    symbol = input("Do you want to be X or O?\n").lower()
    while(symbol != "x" and symbol !="o"):
        symbol = input("Please write X or the letter O\n").lower()
    if(symbol=="x"):
        return ["X","O"]
    else:
        return ["O","X"]

def tableFull(occupiedSpaces):
    if len(occupiedSpaces)==64:
        return True
    return False

def adjacentSpaces(table,occupiedSpaces):
    adjacent_Spaces = []
    for position in occupiedSpaces:
        for i in range(-1,2):
            for j in range(-1,2):
                if ( (0<=position[0]+i<= 7) and (0<=position[1]+j <=7 ) and ([position[0]+i, position[1]+ j] not in adjacent_Spaces) and table[position[0]+i][position[1]+j]==" "):
                    adjacent_Spaces.append([position[0]+i, position[1]+ j])
    return adjacent_Spaces

def noValidMoves(player,symbolPlayer,table,occupiedSpaces):
    adjacent_Spaces = adjacentSpaces(table,occupiedSpaces)
    for position in adjacent_Spaces:
        if(not doesntFlipAnyTile(player,symbolPlayer,position,table)):
            return False
    return True

def numberOfTiles(player,table):
    s= 0
    for i in range(8):
        for j in range(8):
            if(table[i][j]== player):
                s +=1
    return s

def incorrectMovement(player,symbolPlayer,move,table):
    import re
    if(not re.match('^\d \d$',move)):
        print("not in correct format\n")
        return True
    else:
        myre = re.compile(r"\d{1}")
        position = myre.findall(move)
        position[0] = int(position[0]) -1
        position[1] = int(position[1]) -1
        if( not (1<= position[0]+1 <=8) or not (1 <= position[1] +1<=8)):
            print("ERROR: numbers not between 1 and 8\n")
            return True
        elif(table[position[0]][position[1]] != " "):
            print("ERROR: the position is not empty\n")
            return True
        elif(doesntFlipAnyTile(player,symbolPlayer,position,table)):
            print("ERROR: that movement doesn't flip any tiles\n")
            return True
        else:
            return False

def doesntFlipAnyTile(player,symbolPlayer,position,table):
    if(player==symbolPlayer[0]):
        opponent = symbolPlayer[1]
    elif(player==symbolPlayer[1]):
        opponent = symbolPlayer[0]
    table_copy = copy.deepcopy(table)
    preMoveOccupiedSpaces = numberOfTiles(opponent,table_copy)
    makeMove(player,symbolPlayer,position,table_copy)
    afterMoveOccupiedSpaces = numberOfTiles(opponent,table_copy)
    if(preMoveOccupiedSpaces != afterMoveOccupiedSpaces):
        return False
    return True

def makeMove(player,symbolPlayer,position,table):
    from funcionesConvertirFichas import flipTiles
    table[position[0]][position[1]] = player
    flipTiles(player,symbolPlayer,position,table)

def finalCount(symbolPlayer,table):
    human_count = 0
    computer_count = 0
    for i in range(8):
        for j in range(8):
            if(table[i][j]==symbolPlayer[1]):
                human_count += 1
            elif(table[i][j]==symbolPlayer[0]):
                computer_count += 1
    if(human_count == computer_count):
        print("Empate!")
    elif(human_count<computer_count):
        print("Perdiste!")
    else:
        print("Ganaste!")