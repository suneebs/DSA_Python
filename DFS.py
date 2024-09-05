nodes = []
node_count = 0
graph = {}
visited = set()

def add_node(n):
    global node_count
    if n in nodes:
        print("node is already present")
    else:
        node_count += 1
        nodes.append(n)
        graph[n] = []

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not a vertex")
    if v2 not in nodes:
        print(v2,"is not a vertex")
    # l1=[v1,w]
    # l2=[v2,w]
    graph[v1].append(v2)
    graph[v2].append(v1)

def DFS(n,visited,graph):
    if n not in nodes:
        print(n,"is not a vertex")
        return
    if n not in visited:
        print(n,' ',end='')
        visited.add(n)
        for i in graph[n]:
            DFS(i,visited,graph)
            # DFS(i[0],visited,graph)  --- in weighted graph
            


add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A","B")
add_edge("B","E")
add_edge("A","C")
add_edge("A","D")
add_edge("B","D")
add_edge("C","D")
add_edge("E","D")
print(graph)

DFS("A",visited,graph)