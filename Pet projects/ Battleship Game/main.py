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
    place = input().lower().split()
    print(place)
    
    if place[0] == 'r':
        if place[1] in 'ABCDEFGHIJ'.lower():
            
            for i in board:
                if place[1].upper() in i:
                    row = board.index(i)
                    
            for i in range(len(board[row][1])):
                if place[2] == 'c' and i < ships['Carrier']:
                    board[row][1][i] = '1'
                elif place[2] == 'b' and i < ships['Battleship']:
                    board[row][1][i] = '1'
                elif place[2] == 'cr' and i < ships['Cruiser']:
                    board[row][1][i] = '1'
                elif place[2] == 's' and i < ships['Submarine']:
                    board[row][1][i] = '1'
                elif place[2] == 'd' and i < ships['Destroyer']:
                    board[row][1][i] = '1'

    elif place[0] == 'cl':
        if place[1] in '123456789' or place[1] == '10':
            pass
    pprint(board)
    
    
if __name__ == '__main__':
    sea()
    