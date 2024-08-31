
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

        # Adjancy List :
        graphList[v] = []

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

        # Adj. list:
        list1=[v2,cost]
        list2=[v1,cost]
        # graphList[v1].append(v2) -- for unweighted graph
        graphList[v1].append(list1)
   
def print_graph():
    print(nodes)
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"is not in graph")
    else:
        index1= nodes.index(v)
        node_count = node_count - 1
        nodes.pop(index1) # deleting from node list
        # deleting row
        graph.pop(index1)
        # deleting column
        for i in graph:
            i.pop(index1)  

        # Delete in adj. list
        graphList.pop(v)
        for i in graphList:
            list1 = graphList[i]

            # for unweightwed graph
            # if v in list1:
            #     list1.remove(v)

            # For weighted graph
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
                    break

                
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not in t he graph")
    elif v2 not in nodes:
        print(v2,"is not in t he graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        # for undirected graph
        # graph[index2][index1] = 0  

node_count = 0
nodes = []
graph = []
graphList ={}

print("Before insertion: ")
print_graph()
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("A","C",30)
add_edge("C","B",5)
print("After insertion: ")
print_graph()

print(graphList)

print("After deletion:")
# delete_edge("A","B")
# print_graph()

delete_node("B")
print(graphList)