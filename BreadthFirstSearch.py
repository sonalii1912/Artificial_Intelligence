# BFS Algorithm
tosearch = input("Which node is to be searched? :")
G={ 'A':['B','C'] , 'B':['D','E'] , 'D':['H','I'] , 'E':[] , 'C':['F','G'] ,'F':[] , 'G':[],'H':[],'I':[]}
visited =[]
queue =[]

def bfs(node,G,visited,queue,tosearch):
    flag=0
    visited.append(node)
    queue.append(node)
    while( queue ) :
        n=queue.pop(0)
        print(n,end='->')
        if ( n==tosearch ):
            flag=1
            break
        for neighbour in G[n]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    if(flag):
        print("\nElement found")
    else:
        print("Seach unsuccessfull")
    
print("The path is:")
bfs('A',G,visited,queue,tosearch)
