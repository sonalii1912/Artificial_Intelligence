state = [1,2,3,0,4,6,7,5,8]

goal = [1,2,3,4,5,6,7,8,0]

closelist =[]

def printMatrix(st):
    for i in range(9):
        if i>0 and i %3 ==0 :
            print("") #printing new line after 3 charcaters
        print(st[i],end=" ") #printing space after each chharacter
    print("")



def hValue(st,goal):

    count = 0 # variable to store number of misplaced tiles
    for i in range(9):
        #checking if tiles are same or not. if not then increment count
        if st[i]!=0 and st[i]!=goal[i]: 
            count+=1
    
    return count



def shuffle(st,move,pos):
    newH = 9999
    newSt = st.copy()

    for i in range(len(move)):
        tempState = st.copy()

        tempNum = tempState[pos]
        tempState[pos] = tempState[move[i]]
        tempState[move[i]] = tempNum

        if tempState not in closelist:
            tempH = hValue(tempState,goal)
            if tempH < newH :
                newH = tempH
                newSt = tempState.copy()
    return newSt,newH


level = 1
print("------------------- Level ",level," -------------------")
printMatrix(state)

h = hValue(state,goal)

while h > 0:
    pos = state.index(0)

    level += 1

    if pos == 0:
        moves = [1,3]
    elif pos==1:
        moves =[0,2,4]
    elif pos==2:
        moves =[1,5]
    elif pos==3:
        moves =[0,4,6]
    elif pos==4:
        moves =[1,3,5,7]
    elif pos==5:
        moves =[2,4,8]
    elif pos==6:
        moves =[3,7]
    elif pos==7:
        moves =[6,4,8]
    elif pos==8:
        moves =[5,7]

    state , h =  shuffle(state,moves,pos)

    print("------------------- Level ",level," -------------------")
    printMatrix(state)


