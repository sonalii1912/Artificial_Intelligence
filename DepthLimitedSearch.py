#DLS Algorithm
graph ={
    'a':['b','c'],
    'b':['d','e'],
    'c':['f','g'],
    'd':['h','i'],
    'e':['j','k'],
    'f':['l','m'],
    'g':['n','o'],
    'h':[],
    'i':[],
    'j':[],
    'k':[],
    'l':[],
    'm':[],
    'n':[],
    'o':[]
}

def DLS(start , goal , path , level , maxD):
    flag =1
    print("\ncurrent level :",level)
    print("Goal node testing for :",start)
    path.append(start)
    if start==goal:
        return path
    flag=0
    if level == maxD:
        return False
    print("Expanding current Node:",start)
    for child in graph[start]:
        if DLS(child,goal,path,level+1,maxD):
            return path
        path.pop()
    return False

    
    

start = input("Enter a starting Node:")
goal = input("Enter the Goal Node:")
maxD = int(input("Enter the limit for search:"))
print()
path=[]
res = DLS(start , goal ,path , 0, maxD)
if(res):
    print("The path to the goal node is :")
    print(path)
else:
    print("No path is available to the given goal node.")

