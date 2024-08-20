from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def isValid(self, x,y, grid):
        if (x < 0 or x < 0 or x >= len(grid[0]) or y >= len(grid)):
            return False
        
        if grid[x][y]:
            return False
        
        if self.navigator_maze[x][y] == 1:
            return False
        
        return True
    def find_path(self, start, end):
        # IMPLEMENT FUNCTION HERE
        sx, sy = start
        ex, ey = end
        
        
        if self.navigator_maze[sx][sy] == 1 or self.navigator_maze[ex][ey] == 1:
            raise PathNotFoundException()
        if start == end:
            return [start]
        
        ver =  Stack()
        
        
        
        
        # print('lessgo')
        visited = [[False for i in range(len(self.navigator_maze[0]))] for j in range(len(self.navigator_maze))]
        
        
        visited[sx][sy] = True
        ver.push(start)
        

        while not ver.is_empty() and ver.top() != end:
            
            
                
            if self.isValid(sx , sy+1, visited):
                sy = sy + 1
                visited[sx][sy] = True
                ver.push((sx, sy))
                continue
            elif self.isValid(sx +1 , sy , visited):
                sx = sx + 1
                visited[sx][sy] = True
                ver.push((sx, sy))
                continue
            elif self.isValid(sx - 1, sy, visited):
                sx = sx - 1
                visited[sx][sy] = True
                ver.push((sx, sy))
                continue
            elif self.isValid(sx  , sy - 1, visited):
                sy = sy - 1
                visited[sx][sy] = True
                ver.push((sx, sy))
                continue
            else:
                ver.pop()
                if not ver.is_empty():
                    sx,sy = ver.top()
        # ver.display() 
        if ver.is_empty():
            raise PathNotFoundException()
        elif (len(ver)==1 and ver.top()== start):
            raise PathNotFoundException()
        else:
            return ver.data
