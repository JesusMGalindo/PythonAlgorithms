from collections import defaultdict

#https://gist.github.com/econchick/4666413
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_nodes(self, value):
    for i in value:
        self.nodes.add(i) # add element into set
    
  def add_edge(self, from_node, to_node, distance):
      self.edges[from_node].append(to_node)
      self.edges[to_node].append(from_node) # dict to neighbour nodes
      self.distances[(from_node, to_node)] = distance # dict for distance
      self.distances[(to_node, from_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)
  while nodes: 
      min_node = None
      for node in nodes:
          if node in visited:
              if min_node is None:
                  min_node = node
              elif visited[node] < visited[min_node]:
                  min_node = node

      if min_node is None:
            break

      nodes.remove(min_node)
      current_weight = visited[min_node]
      
      print(f"Node({min_node}) with weight {current_weight} is added to Visited")
      for edge in graph.edges[min_node]:
        weight = current_weight + graph.distances[(min_node, edge)]
        if edge not in visited or weight < visited[edge]: # relaxation
          old = ''
          if edge not in visited:
            old = float("inf")
            visited[edge] = weight
            path[edge] = min_node
          else: 
            old = visited[edge]
            visited[edge] = weight
            path[edge] = min_node
          print(f"Relaxed: vertex[{edge}]: OLD: {old} New: {weight} PATH: {path}")


  yield visited, path

g = Graph()
g.add_nodes('A')
g.add_nodes('B')
g.add_nodes('C')
g.add_nodes('D')
g.add_nodes('E')
g.add_nodes('F')
g.add_nodes('G')
g.add_nodes('H')
g.add_nodes('I')
g.add_nodes('s')
g.add_nodes('t')


g.add_edge('s','A',1)
g.add_edge('s','D',4)
g.add_edge('s','G',6)
g.add_edge('A','B',2)
g.add_edge('A','E',2)
g.add_edge('B','C',2)
g.add_edge('C','t',4)
g.add_edge('D','A',3)
g.add_edge('D','E',3)
g.add_edge('E','C',2)
g.add_edge('E','F',3)
g.add_edge('E','I',3)
g.add_edge('F','C',1)
g.add_edge('F','t',3)
g.add_edge('G','D',2)
g.add_edge('G','E',1)
g.add_edge('G','H',6)
g.add_edge('H','E',2)
g.add_edge('H','I',6)
g.add_edge('I','F',1)
g.add_edge('I','t',4)
'''
g.add_edge('A','B',12)
g.add_edge('A','C',7)
g.add_edge('B','D',1)
g.add_edge('B','A',12)
g.add_edge('D','E',8)
g.add_edge('C','F',3)
g.add_edge('D','G',5)
g.add_edge('F','B',1)
g.add_edge('F','G',2)
g.add_edge('C','D',13)
g.add_edge('E','B',6)
'''

print(f"Edges: {g.edges}")
for i,j in dijsktra(g, 's'):
  print(f"Source node: 's'")
  print(f"Cost: {i}")
  print(f"Path: {j}")
