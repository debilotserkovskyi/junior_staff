from pprint import pprint
ships = {
    "Carrier": [5, 1],
    "Battleship": [4, 2],
    "Cruiser": [3, 3],
    "Submarine": [2, 4],
    "Destroyer": [1, 5]
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
    store_list = 15
    # CHANGE ^^^^^^^ to 0
    # board = [[' ', [str(i) for i in range(1, 11)]]]
    # for i in range(10):
    #     i = [chr(ord('A') + i), ["O" for _ in range(10)]]
    #     board.append(i)
    board = [[' ', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']],
             ['A', ['x', 'O', 'O', 'x', 'O', 'x', 'x', 'x', 'x', 'x']],
             ['B', ['O', 'O', 'O', 'x', 'O', 'O', 'O', 'O', 'O', 'O']],
             ['C', ['O', 'O', 'O', 'x', 'O', 'O', 'O', 'O', 'O', 'x']],
             ['D', ['x', 'O', 'O', 'x', 'O', 'O', 'x', 'x', 'O', 'x']],
             ['E', ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'x']],
             ['F', ['x', 'O', 'O', 'O', 'x', 'O', 'x', 'x', 'O', 'x']],
             ['G', ['O', 'O', 'O', 'O', 'x', 'O', 'O', 'O', 'O', 'O']],
             ['H', ['x', 'O', 'O', 'O', 'O', 'x', 'x', 'x', 'O', 'x']],
             ['I', ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'x']],
             ['J', ['x', 'O', 'x', 'x', 'O', 'x', 'x', 'x', 'O', 'x']]]

    def add_ship():
        global row
        # if place[0] == 'R':
        #     if place[1] in 'ABCDEFGHIJ' and (place[2] in '123456789' or place[2] == '10'):
        #         column = int(place[2])
        #
        #         for i in board:
        #             if place[1].upper() in i:
        #                 row = board.index(i)
        #
        #         for i in range(len(board[row][1])):
        #             if place[3] in ships and i < ships[place[3]][0]:
        #                 board[row][1][column + i] = '1'
        #
        # # place ship for column
        # elif place[0] == 'Cl':
        #     if (place[1] in '123456789' or place[1] == '10') and place[2] in 'ABCDEFGHIJ':
        #         column = int(place[1])
        #
        #         for i in board:
        #             if place[2] in i:
        #                 row = board.index(i)
        #
        #         for i in range(len(board[row][1])):
        #             if place[3] in ships and i < ships[place[3]][0]:
        #                 board[row + i][1][column] = '1'
                        
    while store_list <= 15:
        print(f'write where you want to place a ship in format (column or row) (letter or number) (number or letter)'
              f' (ship name)\n{ships}')
        
        place = input().title().split()
        print(place)
        store_list += 1
        
        # place ship for row
        
        store[place[3]] += 15
        
        for i in ships:
            if store[i] > ships[i][1]:
                break
            else:
                add_ship()
        
        pprint(board)
        print(store)
        
            
if __name__ == '__main__':
    sea()
    