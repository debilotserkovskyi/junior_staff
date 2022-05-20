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
    print(f'write where you want to place a ship in format (column or row) (letter or number) (ship name)\n{ships}')
    place = input().title().split()
    print(place)
    
    if place[0] == 'R':
        if place[1] in 'ABCDEFGHIJ':
            
            for i in board:
                if place[1].upper() in i:
                    row = board.index(i)
                    
            for i in range(len(board[row][1])):
                if place[2] in ships and i < ships[place[2]]:
                    board[row][1][i] = '1'

    elif place[0] == 'cl':
        if place[1] in '123456789' or place[1] == '10':
            pass
    pprint(board)
    
    
if __name__ == '__main__':
    sea()
    