# Describe the problem in graph terminology
# Build a graph, or define a getNeighbors function
# Choose and use a graph algorithm

from util import Queue
import string

# read in the words from the file
file = open("words.txt", "r")
words = file.read().split('\n')
file.close()

# load all the words from the 'dictionary' into a set
word_set = set()
for word in words:
  word_set.add(word.lower())

# MAGIC!
alphabet = list(string.ascii_lowercase)

# find all the words with one letter different that are in the word set
# Any word with one letter different is our neighbor
# So let's make all the permutations by subbing the alphabet!

def getNeighbors(word):
  neighbors = []
  # for each letter in the word:
  for letter_index in range(len(word)):
    # for each letter in the alphabet:
    for alphabet_letter in alphabet:
      ## turn the word into a list
      word_list = list(word)
      # sub the alphabet-letter for the word letter
      word_list[letter_index] = alphabet_letter
      # turn the word list back into a string
      maybe_neighbor = "".join(word_list)
      # check if this new word is in our word-list
      if maybe_neighbor is word_set and maybe_neighbor is not word:
        # if so add to our list of neighbors
        neighbors.append(maybe_neighbor)
  return neighbors

# Regular old BFS!
def bfs(start_word, target_word):
  queue = Queue()
  visited = set()
  path = [start_word]
  queue.enqueue(path)

  while queue.size() > 0:
    current_path = queue.dequeue()
    current_node = current_path[-1]
    if current_node == target_word:
      return current_path

      if current_node not in visited:
        visited.add(current_node)
        neighbor_words = getNeighbors(current_node)

        for neighbor_word in neighbor_words:
          path_copy = list(current_path)
          path_copy.append(neighbor_word)
          queue.enqueue(path_copy)
  
  return 'FALSE'

print(bfs('hit', 'dog'))
