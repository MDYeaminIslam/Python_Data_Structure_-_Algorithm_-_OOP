#Here we'll learn about Graph insertion
#Graph is a non-linear data structure
#v is the vertex or node
def add_node(v):
    global node_count
    if v in nodes:
        print(f"Node {v} already exists in the graph")
    else:
        #increasing the node count
        node_count = node_count + 1
        #putting the new node in the vertex list
        nodes.append(v)
        for n in graph:
            n.append(0)#adding 0 at the end of each row because we are adding a new node.And we are adding a new node in each row iterating all the nodes in the list.
        temp = []
        #here node_count is the number of nodes in the graph and that amount or collumns we are adding in the new row
        for i in range(node_count):
            temp.append(0)#adding 0 at the end of each collumn of new row because we are adding a new node
        graph.append(temp)

#adding the edge between two nodes
#undirected and unweighted graph
#v1 is the starting node and v2 is the ending node.Connection between from v1 to v2
'''
def add_edge(v1,v2):
    if v1 not in nodes:
        print(f"Node {v1} does not exist in the graph")
    elif v2 not in nodes:
        print(f"Node {v2} does not exist in the graph")
    else:
        index1 = nodes.index(v1) #index() function returns the index of the first occurence of the value
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1

'''
#this is the undirected and weighted graph
def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(f"Node {v1} does not exist in the graph")
    elif v2 not in nodes:
        print(f"Node {v2} does not exist in the graph")
    else:
        index1 = nodes.index(v1) #index() function returns the index of the first occurence of the value
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost
        
#for weighted directed graph
'''
def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(f"Node {v1} does not exist in the graph")
    elif v2 not in nodes:
        print(f"Node {v2} does not exist in the graph")
    else:
        index1 = nodes.index(v1) #index() function returns the index of the first occurence of the value
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        

'''
#deleting node from the graph
def delete_node(v):
    global node_count
    if v not in nodes:
        print(f"Node {v} does not exist in the graph")
    else:
        #getting the index of the node that we want to delete
        index1 = nodes.index(v)
        #decresing the node count
        node_count = node_count - 1
        nodes.remove(v) #removing the node from the list
        graph.pop(index1) #removing the row from the graph
        #removing the collumn from the graph
        for i in graph:
            i.pop(index1) #delete the collumn from the graph
        

#printing entire graph here in a matrix form
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end=" ")
        print()
        

#all the vertices or nodes stored in a list called nodes
nodes = []
#matrics stored in a list called graph
graph = [] 
node_count = 0

print("Before adding any node")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("A","C",20)
print("After adding any node")
print(nodes)
print(graph)
print('\n')
print_graph()
print('Graph after deleting node: ')
delete_node("A")
print(nodes)
print(graph)




