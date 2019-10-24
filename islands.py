islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]   

big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
               
def getNeighbor1s(node, matrix):
  neighboring_ones = []
  row, col = node

  stepNorth = stepSouth = stepWest = stepEast = False

  if row > 0:
    stepNorth = row - 1
  if row < len(matrix) -1:
    stepSouth = row + 1
  if col > 0:
    stepWest = col - 1
  if col < len(matrix[row]) -1:
    stepEast = col + 1

  if stepNorth is not False and matrix[stepNorth][col] == 1:
    neighboring_ones.append((stepNorth, col))
  if stepSouth is not False and matrix[stepSouth][col] == 1:
    neighboring_ones.append((stepSouth, col))
  if stepWest is not False and matrix[row][stepWest] == 1:
    neighboring_ones.append((row, stepWest))
  if stepEast is not False and matrix[row][stepEast] == 1:
    neighboring_ones.append((row, stepEast))
  
  return neighboring_ones

def dft_recursive(node, visited, matrix):
  if node not in visited:
    visited.add(node)
    
    neighbors = getNeighbor1s(node, matrix)

    for neighbor in neighbors:
      dft_recursive(neighbor, visited, matrix)

# iterate over matrix:
def count_islands(matrix):
  visited = set()
  total_islands = 0
  for row in range(len(matrix)):
    for col in range(len(matrix[row])):
      if matrix[row][col] == 1 and (row, col) not in visited:
        total_islands += 1
        node = (row, col)
        dft_recursive(node, visited, matrix)
  return total_islands

print(count_islands(islands)) # should return 4
print(count_islands(big_islands))