import math
import random

WELCOME = '''
Welcome to Tic Tac Toe!
'''
MSG1 = "The computer will go first."
MSG2 = "What is your next move? (1-9)"
MSG3 = "Do you want to play again? (yes or no)"


def getUserChoise():
    choice=''
    while choice not in TYPE:
        print("Do you want to be X or O?") 
        choice=input().upper()
    return choice

def getNextMove():
    print(MSG2)
    num = 0
    while num<1 or num>9:
        num = input()
        num = int(num)
    return num
    
def drawGraph():   
    print()
    print("   |   |   ") 
    print(" "+grid[7]+" | "+grid[8]+" | "+grid[9]+" ") 
    print("   |   |   ") 
    print("-"*11)
    print("   |   |   ") 
    print(" "+grid[4]+" | "+grid[5]+" | "+grid[6]+" ") 
    print("   |   |   ") 
    print("-"*11)
    print("   |   |   ") 
    print(" "+grid[1]+" | "+grid[2]+" | "+grid[3]+" ") 
    print("   |   |   ") 
   
   
def judgeWin(lastmoveplayer):
    WINCOMBINE = {1:[[2,3],[4,7],[5,9]],2:[[5,8],[1,3]],3:[[1,2],[5,7],[6,9]],4:[[1,7],[5,6]],5:[[3,7],[4,6],[2,8]],6:[[4,5],[3,9]],7:[[8,9],[3,5],[1,4]],8:[[2,5],[7,9]],9:[[7,8],[1,5],[3,6]]}
           
    lastnum = moveRecorder[lastmoveplayer][-1]
    checklist = WINCOMBINE[lastnum]
     
    templist = moveRecorder[lastmoveplayer][0:len(moveRecorder[lastmoveplayer])-1]
    for i in templist:
        for j in checklist:
            temp=j.copy()
            if i in j:
                temp.remove(i)
                if temp[0] in templist:
                    return 1               
         
                 
    if " " not in grid:
        return 2
     
    return 0
         
         
def computerMove():    
    #check if any move to make computer win
    temp=list(set(moveRecorder[computerChoise]).union(set(moveRecorder[choice]))) 
    possibleMoves = list(set(range(1,10)).difference(set(temp))) 
    for i in possibleMoves:
        moveRecorder[computerChoise].append(i)
        if judgeWin(computerChoise):
            moveRecorder[computerChoise].remove(i)
            return i
        moveRecorder[computerChoise].remove(i)
         
    #check if any move to make player win
    for i in possibleMoves:
        moveRecorder[choice].append(i)
        if judgeWin(choice):
            moveRecorder[choice].remove(i)
            return i
        moveRecorder[choice].remove(i)
     
    #check if any blanks to make two own items 
    templist = moveRecorder[computerChoise]
   
    rindex=[]
    cindex=[]
    dig=[]
    for i in templist:
        rindex.append(math.floor((i-1)/3))
        cindex.append((i-1)%3)
         
        if (i-1)%2==0: 
            if (i-1)%4==0:
                dig.append(1)
            else:
                dig.append(0)
        else:
            dig.append(2)
             
             
    templist = moveRecorder[choice]
   
    rindex1=[]
    cindex1=[]
    dig1=[]
    for i in templist:
        rindex1.append(math.floor((i-1)/3))
        cindex1.append((i-1)%3)
     
        if (i-1)%2==0: 
            if (i-1)%4==0:
                dig1.append(1)
            else:
                dig1.append(0)
        else:
            dig1.append(2)       
                 
    ###single in a row
    count=-1
    for i in rindex:
        count+=1
               
        #only one item is in this row, no matter which paler's
        temp = rindex.copy()
        temp[0:0]=rindex1
        if temp.count(i) == 1:
            #candidate col
            templist = list(range(3))
            templist.remove(cindex[count])
            
             
            for j in templist:
                if j in cindex1:
                    return i*3+j+1
            return i*3+max(templist)+1; 
            
    ###single in a col
    count=-1
    for i in cindex:
        count+=1
         
        temp = cindex.copy()
        temp[0:0]=cindex1
        if temp.count(i) == 1:
            #candidate col
            templist = list(range(3))
            templist.remove(rindex[count])
             
            for j in templist:
                if j in rindex1:
                    return j*3+i+1
                 
    ###single in a diagonal 
    count=-1
    for i in dig:
        if i!=2:
            count += 1
             
            temp = dig.copy()
            temp[0:0] = dig1
            if temp.count(i) == 1:
                templist = list(range(3))
                templist.remove(rindex[count])
                 
                if dig1.count(i) == 1 :
                    templist.remove(rindex1[dig1.index(i)])
                elif rindex1.index(1)==cindex1.index(1):
                    templist.remove(1)
                    
                for j in templist:
                    if j in rindex1:
                        return i * 4 + 1 if i > 0 else i * 4 + 3
             
         
    ###random select one
    possibleMoves = list(set(possibleMoves).difference(set(moveRecorder[computerChoise])))
    return possibleMoves[random.randint(1,len(possibleMoves))]
     
    return i*3+templist[0]+1
                 
     
     
     
def run():
    num = 0    
    lastmoveplayer = computerChoise
    while not num:
        #user move
        num = getNextMove()
        while grid[num] != " ":
            num = getNextMove()
        grid[num] = choice
        moveRecorder[choice].append(num)
        lastmoveplayer = choice
        drawGraph()
          
        #computer move
        num = judgeWin(lastmoveplayer)
        if not num:
            num = computerMove()
            grid[num] = computerChoise
            moveRecorder[computerChoise].append(num)
            lastmoveplayer = computerChoise
            drawGraph()
            num = judgeWin(computerChoise)         
         
    if num == 1:
        print(WIN[lastmoveplayer])
    elif num == 2:
        print("Even!")       




if __name__ == "__main__":
    print(WELCOME)
    
    
    continuePlay = "yes"
    while continuePlay=="yes":
        TYPE = ["X","O"]
        choice = getUserChoise()
        TYPE.remove(choice);
        computerChoise = TYPE[0]
        WIN = {computerChoise:"The computer has beaten you! You lose.",choice:"YOU win!"}
     
        #initial
        print(MSG1)
        moveRecorder = {"X":[],"O":[7]}
        grid=[""," "," "," "," "," "," ",computerChoise," "," "]
        drawGraph()
         
        #run
        run()
        
        #end
        print(MSG3)
        continuePlay=input().lower()
    




