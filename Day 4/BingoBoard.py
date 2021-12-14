
class BingoBoard:
    
    def __init__(self, lines):
        self.board = []
        self.drawn = [[0 for i in range(5)] for i in range(5)]

        # print(f"New board! I got {len(lines)} lines")
        for line in lines:
            nums = [i for i in line.split(' ') if i != '']
            self.board.append([int(i) for i in nums])


    def pickNumber(self, picked):
        for row in range(5):
        # for row in self.board:
            for col in range(5):
                if int(picked) == self.board[row][col]:
                    self.drawn[row][col] = 1

        bingo = self.checkBingo()
        # print(f"Aaand... bingo? {bingo}")
        # if bingo: print(f"yes! we have bingo with board {self.board}")
        return bingo
        
    def checkBingo(self):
        for row in range(5):
            for col in range(5):
                if int(self.drawn[row][col]) == 1: 
                    if col == 4: return True
                else: break

        for col in range(5):
            for row in range(5):
                if int(self.drawn[row][col]) == 1:
                    if row == 4: return True
                else: break
        
        return False

    def calcScore(self, called):
        score = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.drawn[row][col] == 0:
                    score += self.board[row][col]
        print(f"score b4 mult: {score} number called {called} so thus {score*int(called)}")
        return score * int(called)

    def __str__(self):
        return str(self.board)