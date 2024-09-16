class Solution:
    def getnums(self,board,x,y):
        num=0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if i >= 0 and i<len(board) and j>=0 and j<len(board[i]) and board[i][j]=='M':
                    num+=1
        return num            

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        x,y=click
        if board[x][y]=='M':
            board[x][y]='X'
        else:
            num=self.getnums(board,x,y)
            if num:
                board[x][y]=str(num)
            else:
                board[x][y]='B'
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        if i >= 0 and i<len(board) and j>=0 and j<len(board[i]) and board[i][j]!='B':
                            self.updateBoard(board,[i,j])
        return board                
