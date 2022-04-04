def controllo(matrix):
    for i in range (0,3):
        if (matrix[i][0]=="X" and matrix[i][1]=="X" and matrix[i][2]=="X") or (matrix[0][i]=="X" and matrix[1][0]=="X" and matrix[2][i]=="X"):
            return "X"
        elif (matrix[i][0]=="O" and matrix[i][1]=="O" and matrix[i][2]=="O") or (matrix[0][i]=="O" and matrix[1][i]=="O" and matrix[2][i]=="O"):
            return "O"
      for i in range(0,3,+2):
          if (matrix[i][i]=="X" and matrix[i][i+1]=="X" and matrix[i][i+2]=="X") or (matrix[i][0]=="X" and matrix[i][1]=="X" and matrix[i][2]=="X")









#def farcire(player):






def display_board(scelta,pos):
    blankBoard="""
___________________
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
"""
    if ( scelta == 'O' or scelta== 'X'):
        blankBoard = blankBoard.replace(str(pos), scelta)

    print(blankBoard)



matrix=[["1","2","3"],
        ["4","5","6"],
        ["7","8","9"]]
print(matrix)
player1=input("Inserisci username: ")
player2=input("Inserisci username: ")
scelta=input(player1+" scegli X o O")
if scelta=='X':
    farcire()
