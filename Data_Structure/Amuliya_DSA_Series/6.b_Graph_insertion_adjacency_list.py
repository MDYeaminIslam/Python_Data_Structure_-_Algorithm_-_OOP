#here we will work with adjacency list representation of graph
#we'll use dictionary to represent adjacency list and key will be the node and value will be the list of nodes connected to it


def add_node(v):
    #checking if node already exists or not
    if v in graph:
        print(f"{v} is already present in the graph")
    else:
        graph[v] = []

#adding edge between nodes
#v1 is the starting node and v2 is the ending node
#undirected and unweighted graph

'''
def add_edge(v1,v2):
    if v1 not in graph:
        print(f"Node {v1} does not exist in the graph")
    elif v2 not in graph:
        print(f"Node {v2} does not exist in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


'''



#this is the undirected and weighted graph

def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(f"Node {v1} does not exist in the graph")
    elif v2 not in graph:
        print(f"Node {v2} does not exist in the graph")
    else:
        #storing the cost in the list
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)
        
#adding edge between nodes
#v1 is the starting node and v2 is the ending node
#directed and weighted graph

''' 
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(f"Node {v1} does not exist in the graph")
    elif v2 not in graph:
        print(f"Node {v2} does not exist in the graph")
    else:
        list1 = [v2,cost]
        graph[v1].append(list1)


'''

#adding edge between nodes
#v1 is the starting node and v2 is the ending node
#directed and unweighted graph

''' 
def add_edge(v1,v2):
    if v1 not in graph:
        print(f"Node {v1} does not exist in the graph")
    elif v2 not in graph:
        print(f"Node {v2} does not exist in the graph")
    else:
        graph[v1].append(v2)

'''

#nodes with their adjacent nodes will be stored in the dictionary
graph = {}
node_count = 0

add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("A","C",5)
print(graph)