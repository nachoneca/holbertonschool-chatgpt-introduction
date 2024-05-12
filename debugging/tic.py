#!/usr/bin/python3
def print_board(board):
    """
    Imprime el tablero de tic-tac-toe.

    Args:
        board (list): El tablero de tic-tac-toe representado como una lista de listas.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Verifica si hay un ganador en el juego de tic-tac-toe.

    Args:
        board (list): El tablero de tic-tac-toe representado como una lista de listas.

    Returns:
        bool: True si hay un ganador, False de lo contrario.
    """
    # Verifica si hay un ganador en las filas
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Verifica si hay un ganador en las columnas
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Verifica si hay un ganador en las diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Función principal que ejecuta el juego de tic-tac-toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if board[row][col] == " ":
                board[row][col] = player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as integers within range.")

    print_board(board)
    print("Player " + player + " wins!")

tic_tac_toe()
