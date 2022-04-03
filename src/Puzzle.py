# Nama  : Muhammad Gilang Ramadhan
# NIM   : 13520137
# Puzzle.py
# Containing property of the puzzle and Branch and Bound Algorithm

import heapq as pq
import copy

class Puzzle:
    # Initialate

    # Puzzle as blank arr
    puzzle = []
    # The solution of the puzzle
    Solution = [] 
    # Direction to move : DOWN, RIGHT, UP, LEFT
    Direction = [(1,0),(0,1),(-1,0),(0,-1)] 
    # Kurang Function for each entry
    Tempkurang = [0 for i in range(16)]
    # List of visited node
    visited = []
    # Value X
    ValueX = 0
    # Total
    Total = 0
    # Minimum Cost
    mincost = 10**9 + 7

    def __init__(self, FileName):
        self.puzzle = [] 
        self.Solution = [] 
        self.Tempkurang = [0 for i in range(16)] 
        self.visited = []
        self.ValueX = 0 
        self.total = 0
        self.mincost = 1e9+7 
        self.getPuzzle(FileName)

    # Get Puzzle from Input file .txt
    def getPuzzle(self,FileName):
        temp_puzzle = []
        puzzle_set = set({})
        with open(FileName) as f:
            lines = f.readlines()
            if len(lines)==4:
                for line in lines:
                    if len(line.split())==4:
                        temp_puzzle.append([int(i) for i in line.split()])
                        for i in line.split():
                            puzzle_set.add(int(i))
                    else:
                        return
            else:
                return
        if puzzle_set!={i for i in range(16)}:
            return
        self.puzzle = temp_puzzle

    # Calculate sum of KURANG(i) + X
    def SumKurang(self):
        cost = 0
        flat = [i for j in self.puzzle for i in j]
        for i in range(len(flat)):
            temp = 0
            if flat[i]==0 and (((i//4)%2 == 1 and i%2 == 0) or ((i//4)%2 == 0 and i%2==1)):
                self.ValueX = 1
            for j in range(i+1,len(flat)):
                if ((flat[i]>flat[j] or flat[i]==0) and flat[j]!=0):
                    temp += 1
                    cost += 1
            self.Tempkurang[flat[i]] = temp
        return cost + self.ValueX
    
    # Calculate sum cost
    def SumCost(self, puzzle):
        flat = [i for j in puzzle for i in j]
        cost = 0
        for i in range(len(flat)):
            if ((i+1)%16 != flat[i]):
                cost+=1
        return cost

    # Get coordinat zero value position from the puzzle
    def getZeroPos(self, puzzle):
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                if puzzle[i][j]==0:
                    return (i,j)
        return (-1,-1)
    
    # Using Branch and Bound Algorithm to solve the puzzle
    def solve(self): 
        kurang = self.SumKurang()
        if kurang%2==0:
            # temp current total cost, depth, puzzle, moves to puzzle
            heap = []
            cost = self.SumCost(self.puzzle)
            pq.heappush(heap,(cost,0,copy.deepcopy(self.puzzle),[]))

            while len(heap)>0:
                curCost, depth, curPuzzle, path = pq.heappop(heap)
                self.visited.append(curPuzzle)
                self.total += 1
                if (curCost<=self.mincost and curCost != depth):
                    # Transitions
                    x0,y0 = self.getZeroPos(curPuzzle)
                    for dx,dy in self.Direction:
                        if (0<=x0+dx<4 and 0<=y0+dy<4): # If the coordinat not valid
                            newPuzzle = copy.deepcopy(curPuzzle)
                            newPuzzle[x0][y0], newPuzzle[x0+dx][y0+dy] = newPuzzle[x0+dx][y0+dy], newPuzzle[x0][y0]
                            newPath = copy.deepcopy(path)
                            newPath.append((dx,dy))
                            cost = self.SumCost(newPuzzle)
                            if (not newPuzzle in self.visited):
                                pq.heappush(heap,(cost+depth+1, depth+1, newPuzzle, newPath))
                else:
                    if (curCost>self.mincost): # Bound
                        continue
                    if (curCost == depth): # Solution found
                        if (curCost<self.mincost):
                            self.mincost = curCost
                            self.Solution = path
                        continue
        return kurang
