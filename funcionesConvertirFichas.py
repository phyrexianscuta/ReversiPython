def checkUpCol(player,symbolPlayer,position,table):
    UpCol=[]
    if(player==symbolPlayer[0]):
        opponent = symbolPlayer[1]
    elif(player==symbolPlayer[1]):
        opponent = symbolPlayer[0]
    for i in range(position[1]-1,-1,-1):
        UpCol.append(table[position[0]][i])
    listaUnida = "".join(UpCol)
    index_space = listaUnida.find(" ")
    index_player = listaUnida.find(player)
    if(player in UpCol and (index_space ==-1 or index_player < index_space)):
        checking = True
        i = position[1]
        while(checking and i>=0):
            if(table[position[0]][i-1]==opponent):
                table[position[0]][i-1] = player
                i-=1
            else:
                checking =False

def checkDownCol(player,symbolPlayer,position,table):
    DownCol=[]
    if(player==symbolPlayer[0]):
        opponent = symbolPlayer[1]
    elif(player==symbolPlayer[1]):
        opponent = symbolPlayer[0]
    for i in range(position[1]+1,8):
        DownCol.append(table[position[0]][i])
    listaUnida = "".join(DownCol)
    index_space = listaUnida.find(" ")
    index_player = listaUnida.find(player)
    if(player in DownCol and (index_space ==-1 or index_player < index_space)):
        checking = True
        i = position[1]
        while(checking and i<=7):
            if(table[position[0]][i+1]==opponent):
                table[position[0]][i+1] = player
                i+=1
            else:
                checking =False

def checkRightRow(player,symbolPlayer,position,table):
    RightRow=[]
    if(player==symbolPlayer[0]):
        opponent = symbolPlayer[1]
    elif(player==symbolPlayer[1]):
        opponent = symbolPlayer[0]
    for i in range(position[0]+1,8):
        RightRow.append(table[i][position[1]])
    listaUnida = "".join(RightRow)
    index_space = listaUnida.find(" ")
    index_player = listaUnida.find(player)
    if(player in RightRow and (index_space ==-1 or index_player < index_space)):
        checking = True
        i = position[0]
        while(checking and i<=7):
            if(table[i+1][position[1]]==opponent):
                table[i+1][position[1]] = player
                i+=1
            else:
                checking =False

def checkLeftRow(player,symbolPlayer,position,table):
    LeftRow=[]
    if(player==symbolPlayer[0]):
        opponent = symbolPlayer[1]
    elif(player==symbolPlayer[1]):
        opponent = symbolPlayer[0]
    for i in range(position[0]-1,-1,-1):
        LeftRow.append(table[i][position[1]])
    listaUnida = "".join(LeftRow)
    index_space = listaUnida.find(" ")
    index_player = listaUnida.find(player)
    if(player in LeftRow and (index_space ==-1 or index_player < index_space)):
        checking = True
        i = position[0]
        while(checking and i>=0):
            if(table[i-1][position[1]]==opponent):
                table[i-1][position[1]] = player
                i-=1
            else:
                checking =False

def checkUpDiag1(player,symbolPlayer,position,table):
    UpDiag1 = []
    if(player==symbolPlayer[0]):
        opponent = symbolPlayer[1]
    elif(player==symbolPlayer[1]):
        opponent = symbolPlayer[0]
    l = min(position[0],position[1])
    for i in range(1,l+1):
        UpDiag1.append(table[position[0]-i][position[1]-i])
    listaUnida = "".join(UpDiag1)
    index_space = listaUnida.find(" ")
    index_player = listaUnida.find(player)
    if(player in UpDiag1 and (index_space ==-1 or index_player < index_space)):
        checking = True
        i = 1
        while(checking and position[0]-i>=0 and position[1]-i >= 0):
            if(table[position[0]-i][position[1]-i]==opponent):
                table[position[0]-i][position[1]-i] = player
                i+=1
            else:
                checking =False

def checkDownDiag1(player,symbolPlayer,position,table):
    DownDiag1 = []
    if(player==symbolPlayer[0]):
        opponent = symbolPlayer[1]
    elif(player==symbolPlayer[1]):
        opponent = symbolPlayer[0]
    l = min(8-position[0],8-position[1])
    for i in range(1,l):
        DownDiag1.append(table[position[0]+i][position[1]+i])
    listaUnida = "".join(DownDiag1)
    index_space = listaUnida.find(" ")
    index_player = listaUnida.find(player)
    if(player in DownDiag1 and (index_space ==-1 or index_player < index_space)):
        checking = True
        i = 1
        while(checking and (position[0]+i<=7) and (position[1]+i <= 7)):
            if(table[position[0]+i][position[1]+i]==opponent):
                table[position[0]+i][position[1]+i] = player
                i+=1
            else:
                checking =False

def checkUpDiag2(player,symbolPlayer,position,table):
    UpDiag2 = []
    if(player==symbolPlayer[0]):
        opponent = symbolPlayer[1]
    elif(player==symbolPlayer[1]):
        opponent = symbolPlayer[0]
    l = min(7-position[0],position[1])
    for i in range(1,l+1):
        UpDiag2.append(table[position[0]+i][position[1]-i])
    listaUnida = "".join(UpDiag2)
    index_space = listaUnida.find(" ")
    index_player = listaUnida.find(player)
    if(player in UpDiag2 and (index_space ==-1 or index_player < index_space)):
        checking = True
        i = 1
        while(checking and (position[0]+i <=7) and (position[1]-i >= 0)):
            if(table[position[0]+i][position[1]-i] ==opponent):
                table[position[0]+i][position[1]-i] = player
                i+=1
            else:
                checking = False

def checkDownDiag2(player,symbolPlayer,position,table):
    DownDiag2 = []
    if(player==symbolPlayer[0]):
        opponent = symbolPlayer[1]
    elif(player==symbolPlayer[1]):
        opponent = symbolPlayer[0]
    l = min(position[0],7-position[1])
    for i in range(1,l+1):
        DownDiag2.append(table[position[0]-i][position[1]+i])
    listaUnida = "".join(DownDiag2)
    index_space = listaUnida.find(" ")
    index_player = listaUnida.find(player)
    if(player in DownDiag2 and (index_space ==-1 or index_player < index_space)):
        checking = True
        i = 1
        while(checking and (position[0]-i >=0) and (position[1]+i <= 7)):
            if(table[position[0]-i][position[1]+i] ==opponent):
                table[position[0]-i][position[1]+i] = player
                i+=1
            else:
                checking = False

def flipTiles(player,symbolPlayer,position,table):
    checkUpCol(player,symbolPlayer,position,table)
    checkDownCol(player,symbolPlayer,position,table)
    checkLeftRow(player,symbolPlayer,position,table)
    checkRightRow(player,symbolPlayer,position,table)
    checkUpDiag1(player,symbolPlayer,position,table)
    checkDownDiag1(player,symbolPlayer,position,table)
    checkDownDiag2(player,symbolPlayer,position,table)
    checkUpDiag2(player,symbolPlayer,position,table)
