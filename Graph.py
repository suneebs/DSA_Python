
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

def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)  
        # 1 for unweighted, cost for weighted
        graph[index1][index2] =  cost  
        # graph[index2][index1] =  cost   [ for directed graph ]
   
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
add_edge("A","B",10)
add_edge("C","B",5)
print("After insertion: ")
print_graph()