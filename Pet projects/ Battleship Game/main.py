from pprint import pprint

def play_field():
    sea = [[chr(ord('A') + i)] for i in range(10)]
    sea.append([str(i) + ' ' for i in range(0, 11)])
    for row in range(len(sea)):
        if row < 10:
            sea[row].append(' 0 ' * 10)
        print(' '.join(sea[row]))
        
        
ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}


def sea():
    board = [[' ', [str(i) for i in range(1, 11)]]]
    for i in range(11):
        i = [chr(ord('A') + i), ["O" for _ in range(10)]]
        board.append(i)
    pprint(board)
    
    
sea()
# TODO 1 Make multiple battleships:
#  You will need to be careful because you need to make sure that you do not place battleships on top of each
#  other on the game board.
#  You will also want to make sure that you balance the size of the board with the number of ships so the game is
#  still challenging and fun to play.

# TODO 2  Make battleships of different sizes:
#  This is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching.
#  You will need to make sure you do not accidentally place part of a ship off the side of the board.

# TODO 3 Make your game a two-player game:
#  Use functions to allow your game to have more features like rematches, statistics and more!

# play_field()
