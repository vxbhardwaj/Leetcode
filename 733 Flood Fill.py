class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row,column, img= len(image),len(image[0]),image[sr][sc]
        def bfs(i,j):
            if i<0 or j<0 or i>=row or j>=column or image[i][j]==newColor or img!=image[i][j]:
                return
            image[i][j]=newColor
            bfs(i,j-1)
            bfs(i,j+1)
            bfs(i-1,j)
            bfs(i+1,j)
        bfs(sr,sc)
        return image