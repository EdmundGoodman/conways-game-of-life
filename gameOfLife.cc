#include<iostream>

//Set initial conditions
extern const int width = 10;
extern const int height = 10;

void printGrid(int grid[height][width]) {
  //Print the grid array
  //system("clear");
  for (int y=0; y<height; y++) {
    for (int x=0; x<width; x++) {
      //std::cout << grid[y][x];
      if (grid[y][x] == 0) {
        std::cout << " ";
      } else {
        std::cout << "\u2588";
      }
    }
    std::cout << std::endl;
  }
  std::cout << std::endl;
}

int findNoNeighbours(int grid[height][width], int x, int y) {
  //Return the number of neighbours a given (x,y) square has
  int total = 0;
  int dyValues[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
  int dxValues[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
  for (int i=0; i<8; i++) {
    int dy = dyValues[i];
    int dx = dxValues[i];
      //Stop at the edges of the grid
      if ((y+dy>0 and y+dy<8) and (x+dx>0 and x+dx<8)) {
        if (grid[y+dy][x+dx] != 0) {
          total += 1;
        }
      }
  }
  return total;
}

int main() {
  //Set the number of iterations
  int iterations = 5;

  //Initialise the grid
  int grid[height][width];
  for (int y=0; y<height; y++) {
    for (int x=0; x<width; x++) {
      grid[y][x] = 0;
    }
  }

  //Add some data to the initial grid (e.g. a 'Glider')
  grid[3][1]=1; grid[3][2]=1; grid[3][3]=1; grid[2][3]=1; grid[1][2]=1;

  //Print the grid
  printGrid(grid);

  while (true) {
    //Generate a array of the number of neighbours each grid square has
    int gridNeighbourValues[height][width];
    for (int y=0; y<height; y++) {
      for (int x=0; x<width; x++) {
        gridNeighbourValues[y][x] = findNoNeighbours(grid, x, y);
      }
    }

    //Update the grid based on each squares INITIAL number of neighbours (from the gridNeighbourValues array)
    for (int y=0; y<height; y++) {
      for (int x=0; x<width; x++) {
        if (gridNeighbourValues[y][x] < 2) { //Underpopulation
          grid[y][x] = 0;
        } else if (gridNeighbourValues[y][x] > 3) { //Overpopulation
          grid[y][x] = 0;
        } else if (gridNeighbourValues[y][x] == 3) { //Reproduction
          grid[y][x] = 1;
        }
      }
    }

    //Print the grid
    printGrid(grid);

    //Stop looping when the required number of iterations have been evaluated
    iterations --;
    if (iterations == 1) {
      break;
    }
  }

  return 0;
}
