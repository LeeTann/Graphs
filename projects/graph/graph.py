"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

        pass  # TODO
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        set_of_friends = self.vertices[v1]
        set_of_friends.add(v2)

    def getNeighbors(self, vertex):
        return self.vertices[vertex]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()

        visited = set()

        queue.enqueue(starting_vertex)
        
        while queue.size():
            current_node = queue.dequeue()
            print("bft", current_node)

            if current_node not in visited:
                visited.add(current_node)
            
                for neighbor in self.vertices[current_node]:
                    queue.enqueue(neighbor)
            
        pass  # TODO
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        stack = []

        visited = set()
        
        stack.append(starting_vertex)

        while len(stack) > 0:
            current_node = stack.pop()
            print("dft", current_node)

            if current_node not in visited:
                visited.add(current_node)

                for neighbor in self.vertices[current_node]:
                    stack.append(neighbor)

        pass  # TODO
    def dft_recursive(self, node, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Base case
        if node not in visited:
            print("node", node)
            visited.add(node)

            neighbors = self.getNeighbors(node)
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)

        pass  # TODO
    def bfs(self, starting_vertex, destination_vertex):
        """
        Search + shortest path

        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        quque = Queue()
        visited = set()

        path = [starting_vertex] # enqueing a list to get all possible solution
        quque.enqueue(path)

        while quque.size() > 0:
            current_path = quque.dequeue()
            current_node = current_path[-1] #last node

            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.getNeighbors(current_node)

                for neighbor in neighbors:
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
                    quque.enqueue(path_copy)

        pass  # TODO
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()

        path = [starting_vertex]
        stack.push(path)

        while stack.size() > 0:
            current_path = stack.pop()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path
            
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.getNeighbors(current_node)
                print("neighbors", neighbors)

                for neighbor in neighbors:
                    new_path = current_path[:]
                    new_path.append(neighbor)
                    stack.push(new_path)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
