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
    for i in range(11):
        i = [chr(ord('A') + i), ["O" for _ in range(10)]]
        board.append(i)
    # pprint(board)
        

sea()
