from BingoBoard import BingoBoard

def main():
    with open("./Day 4/input.txt") as f:
        inputs = f.read().split('\n')

    boards = createBoards(inputs)
    drawnNums = inputs[0].split(',')

    one(boards, drawnNums)
    two(boards, drawnNums)

def one(boards, drawnNums):
    for drawn in drawnNums:
        won = False
        for b in range(len(boards)):
            if (boards[b].pickNumber(int(drawn))): 
                won = True
                print("looping out now")
                break    
        if (won): 
            print(f"Score! Bingo score: {boards[b].calcScore(int(drawn))}")
            print(f"Winning board: {boards[b].board}")
            break

def two(boards, drawnNums):
    for drawn in drawnNums:
        # print(f"drawing number {drawn}")
        for b in list(boards):
            if b.pickNumber(int(drawn)): 
                boards.remove(b)
                if len(boards) == 0:
                    print(f"Last to win! Score is {b.calcScore(drawn)} with board {b}")
                    return boards
            
                
    

def createBoards(inputs):
    boards = []
    boardStrings = []
    for i in range(2, len(inputs) + 1):
        if ((i-1)%6==0 and i != 2):
            boards.append(BingoBoard(boardStrings))
            boardStrings = []
            #i += 1
        else: 
            boardStrings.append(inputs[i])
            # print(f"appended line {i}")

    # for board in boards: print(f"Board! {board}")
    # for board in boards: print(board)
    return boards


if __name__ == "__main__":
    main()
