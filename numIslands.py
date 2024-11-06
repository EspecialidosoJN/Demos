class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.Vlen = len(grid)
        if self.Vlen < 0:
            return 0
        self.Hlen = len(grid[0])
        if self.Hlen < 0:
            return 0
        self.x=0
        self.y=0
        self.islands = 0
        connecting = False
        while self.y < self.Vlen:
            self.x=0
            while self.x < self.Hlen:
                pos = self.grid[self.y][self.x]
                if pos == "1":
                    self.islands += 1
                    self.propagateLRUD(self.y,self.x)
                self.x += 1
            self.y += 1
        return self.islands
                    
                    
    def propagateLRUD(self,y,x):
        if self.grid[y][x] == "0":
            return 0
        self.grid[y][x] = "0"
        xn = x+1
        yn = y+1
        xp = x-1
        yp = y-1
        if xn < self.Hlen:
            self.propagateLRUD(y,xn)
        if yn < self.Vlen:
            self.propagateLRUD(yn,x)
        if xp >= 0:
            self.propagateLRUD(y,xp)
        if yp >= 0:
            self.propagateLRUD(yp,x)
# example grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
