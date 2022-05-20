from pprint import pprint
ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 2,
    "Destroyer": 1
}  # 1 2 3 4 5
global row


def sea():
    global row
    store = {
        "Carrier": 0,
        "Battleship": 0,
        "Cruiser": 0,
        "Submarine": 0,
        "Destroyer": 0
    }
    store_list = []
    board = [[' ', [str(i) for i in range(1, 11)]]]
    for i in range(10):
        i = [chr(ord('A') + i), ["O" for _ in range(10)]]
        board.append(i)
    
    while len(store_list) <= 15:
        print(f'write where you want to place a ship in format (column or row) (letter or number) (number or letter) '
              f'(ship name)\n{ships}')
        
        place = input().title().split()
        print(place)
        
        store_list += 1
        if place[3] in store:
            pass
    
        # place ship for row
        if place[0] == 'R':
            if place[1] in 'ABCDEFGHIJ' and (place[2] in '123456789' or place[2] == '10'):
                column = int(place[2])
                
                for i in board:
                    if place[1].upper() in i:
                        row = board.index(i)
                
                for i in range(len(board[row][1])):
                    if place[3] in ships and i < ships[place[3]]:
                        board[row][1][column+i] = '1'
        
        # place ship for column
        elif place[0] == 'Cl':
            if (place[1] in '123456789' or place[1] == '10') and place[2] in 'ABCDEFGHIJ':
                column = int(place[1])
                
                for i in board:
                    if place[2] in i:
                        row = board.index(i)
                
                for i in range(len(board[row][1])):
                    if place[3] in ships and i < ships[place[3]]:
                        board[row+i][1][column] = '1'
        
        pprint(board)
        
            
if __name__ == '__main__':
    sea()
    