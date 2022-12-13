class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        l1=len(matrix)
        l2=len(matrix[0])
        
        if (matrix==None or l1==0):
            return 0
        else:
            i=l1-2
            while i>=0:
                j=0
                while j<l2:
                    minimum=matrix[i+1][j]
                    if(j>0):
                        minimum=min(minimum,matrix[i+1][j-1])
                    if(j<l2-1):
                        minimum=min(minimum,matrix[i+1][j+1])
                    matrix[i][j]+=minimum
                    j+=1
                i-=1
            print(matrix)
            return min(matrix[0])

                         
