


#Variables globales
board = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]
jugador1 = "X"
gameRunning = True

# tablero de juego
def printBoard(board):              #Aca simplemente armamos el tablero con los espacios de la lista board
    print(" -------------")
    print(" | " + board[0] + " | " + board[1] + " | " + board[2]+ " | ")
    print(" -------------")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5]+ " | ")
    print(" -------------")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8]+ " | ")
    print(" -------------")

# entrada de AMBOS jugadores
def playerInput(board):                #juega el jugador1, reemplazamos los valores vacios por X
    entrada = int(input("Elegi un casillero del 1 al 9: "))
    if board[entrada-1] == " ":         #restamos para que coincida con el slicing de la lista
        board[entrada-1] = jugador1          
    else:
        print("El casillero que elegiste esta lleno. Por favor elegi otro.")
        
# cambiar de jugador    
def switch():    #Cambiamos entre jugador 1 y 2
    global jugador1
    if jugador1 == "X":         #! aspecto a mejorar: incluir dos imputs
        jugador1 = "O"
    else:
        jugador1 = "X"

# chequeo 
def checkHorizont(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        return True

def checkvertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        return True
    elif board[2] == board[4] == board[6] and board[4] != " ":
        return True

#analizamos vertical, horizontal y diagonalmente
def check_quien_gana(board):    #si se da alguna de las 3 condiciones paramos el juego
    global gameRunning
    if checkHorizont(board) == True:
        printBoard(board)
        print("ta te ti!")
        gameRunning = False  

    elif checkvertical(board):
        printBoard(board)
        print("ta te ti!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print("ta te ti!")
        gameRunning = False

#chequeo de empate
def checkempate(board):  #chequeamos si no hay casillas vacias y ademas si no hay tateti
    global gameRunning
    if " " not in board:
        printBoard(board)
        print("Empate")
        gameRunning = False



#ejecucion
while gameRunning == True:
    printBoard(board)
    playerInput(board)
    check_quien_gana(board)
    switch()
    check_quien_gana(board)
    checkempate(board)
    
    
    
 #! aspectos a mejorar: incluir dos imputs, persolizar con el nombre de cada jugador, crear una interfaz en pygamy o tkinter