
# Add Node
def add_node(v):
    global node_count
    if (v in nodes):
        print("Node is already present in the graph")
    else:
        node_count = node_count + 1
        nodes.append(v)

        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def print_graph():
    print(nodes)
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()


node_count = 0
nodes = []
graph = []
print("Before insertion: ")
print_graph()
add_node("A")
add_node("B")
add_node("C")
print("After insertion: ")
print_graph()