import networkx as nx
import matplotlib.pyplot as plt
 
g=nx.Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)
print(g.nodes())
g.add_node(7)
print(g.nodes())
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(4,6)
g.add_edge(5,4)
g.add_edge(2,3)
print(g.edges())
g.add_edge(9,8)
print(g.edges())
nx.draw(g)
plt.show()

