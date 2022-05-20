from pprint import pprint
board = []
ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}


def sea():
    global board
    board = [[' ', [str(i) for i in range(1, 11)]]]
    for i in range(10):
        i = [chr(ord('A') + i), ["O" for _ in range(10)]]
        board.append(i)
    set_ships()
    

def set_ships():
    global board
    row = 2
    # column = input('')
    ship = input()
    for i in range(len(board[row][1])):
        if ship == 'c' and i < ships['Carrier']:
            board[row][1][i] = '1'
        # print(board[row])
    pprint(board)
sea()
