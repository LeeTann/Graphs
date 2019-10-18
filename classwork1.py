# def bft(start_node):
#   # make a queue, so the nodes are about to visit can wait in line
#   # make a set, to track all the nodes we have already visited

#   # enquue the start node

#   # while this queue isn't empy:
#   ## dequque whatever is at the front, and this is our current node
  
#   ## if they have not been visited: 
#   ### mark the current node as visited by putting it in our visited set

#   ## get all of the current node's friends/ neighbors

#   ## for each of those friends:
#   ### put them into our queue to be visted

#   q = Queue()

#   visited = set(A, B, C, E, F, G)

#   current_node = G

#   neighbors = [F]

def bft(self, start_node):
  q = Queue()

  visited = set()

  q.enqueue(start_node)

  while q.size():
    current_node = q.dequque()

    if current_node not in visited:
      visited.add(current_node)
      
      neighbors = self.getNeighbors(current_node)
      
      for neighbor in neighbors:
        q.enqueue(neighbor)


def dft(self, start_node):
  # make a stack, for the nodes we are about to visit
  stack = []
  # make a set for visited nodes
  visited = set()
  # put the start node on the stack
  stack.append(start_node)
  # while the stack isnt empty:
  while len(stack):
  ## pop off whatever is on the top of the stack, this is our current node
    current_node = stack.pop()
  ### if current node has not yet been visited:
    if current_node not in visited:
      visited.add(current_node)
      neighbors = self.getNeighbors(current_node)
      for neighbor in neighbors:
        stack.append(neighbor)
  ### mark the current node as visited by putting it in our visited set
  ### get all of the current nodes friends/ neighbors
  ### for each of those friends:
  ### put them in the queue to be visited