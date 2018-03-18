#Edmund Goodman - Creative Commons Attribution-NonCommercial-ShareAlike 2.5
#Conway's Game of Life
from copy import deepcopy
import os, time

def findNoNeighbours(x, y):
    #Find the number of adjacent living cells to a cell given its x,y co-ordinates
    total = 0
    for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        try:
            if grid[y+dy][x+dx] != 0:
                total += 1
        except IndexError:
            pass
    return total

def printGrid(grid):
    #Print the grid prettily
    time.sleep(0.01)
    os.system('clear')

    print("+" + "-"*len(grid) + "+")
    for y in grid:
        print("|", end="")
        for x in y:
            if x==0:
                print(" ", end="")
            else:
                print(u"\u2588", end="")
        print("|")
    print("+" + "-"*len(grid) + "+")


def getUpdates(height, width, grid, updates=[]):
    #Generate a list of all updates to be made this game cycle
    #You need to generate a list, as if you update immediately, it changes the
    #state of the board, giving it different properties
    for y in range(height):
        for x in range(width):
            #If squares are on the edge, expand the grid so neighbours can be checked
            if ((x-1<0 or y-1<0) and grid[y][x]!=0):
                #Insert row at top
                grid.insert(0, [0]*width)
                height += 1
                #Insert new 0's to beginning of all rows
                for y in range(0, height):
                    grid[y].insert(0, 0)
                width += 1
                #Don't update, as grid has been moved
                return height, width, []

            elif ((x+1>width-1 or y+1>height-1) and grid[y][x]!=0):
                #Append row at bottom
                grid.append([0]*width)
                height += 1
                #Append new 0's to end of all rows
                for y in range(0, height):
                    grid[y].append(0)
                width += 1
                #Don't update, as grid has been moved
                return height, width, []

            else:
                #Find number of neighbours of the point
                noNeighbours = findNoNeighbours(x, y)
                #Add it to the dictionary
                updates.append([[x,y], noNeighbours])

    #Return updated height and width, and produced grid
    return height, width, updates

#Build the grid
iterations, width, height = 0, 5, 5 #If iterations = 0, it goes on forever
grid, oldGrid = [[0]*width for _ in range(height)], None

#Add some data to the initial grid (e.g. a 'Glider')
grid[2][0]=1; grid[2][1]=1; grid[2][2]=1; grid[1][2]=1; grid[0][1]=1

#Output the grid
printGrid(grid)

while True:

    #Create a list of squares to update, and how to update them
    height, width, updates = getUpdates(height, width, grid)

    #Update the grid
    for update in updates:
        #Underpopulation
        if update[1] < 2:
            grid[update[0][1]][update[0][0]] = 0
        #Overpopulation
        elif update[1] > 3:
            grid[update[0][1]][update[0][0]] = 0
        #Reproduction
        if update[1] == 3:
            grid[update[0][1]][update[0][0]] = 1

    #Output the grid
    if updates != []:
        printGrid(grid)

    #Break after upper limit of iterations
    iterations -= 1
    if iterations == 1:
        break

    #Break if grid is static
    if oldGrid == grid:
        break
    oldGrid = deepcopy(grid)
