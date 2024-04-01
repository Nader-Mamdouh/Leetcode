class NumMatrix(object):

    def __init__(self, matrix):
        for i in range(len(matrix)):
            matrix[i].append(0)

        temp=[ 0 for i in range(len(matrix[0]))]
        matrix.append(temp)
        
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                matrix[i][j]+=matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]

        for i in range(len(matrix)):
            print(matrix[i])

        self.matrix=matrix

    def sumRegion(self, row1, col1, row2, col2):
        return self.matrix[row2][col2]-self.matrix[row1-1][col2]-self.matrix[row2][col1-1]+self.matrix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)