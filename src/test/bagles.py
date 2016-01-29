import random
DESCRIPTION = '''
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.
'''


def selectAnum():
    num = random.randint(100,1000)
    numlist = []
    numlist.append(int(num/100))
    numlist.append(int(num%100/10))
    numlist.append(num%10)
    return numlist


def oneGuess():
    myguess = 0
    while myguess<100 or myguess>999:
        myguess = input()
        myguess = int(myguess)
    
   
    digit3 = myguess%10
    digit2 = int(myguess%100/10)
    digit1 = int(myguess/100)
    
    #check 
    if digit3 not in numlist and digit2 not in numlist and digit1 not in numlist:
        print("Bagels") 
    else:
        result = []
        if numlist[2] == digit3:
            result.append(1) 
        elif digit3 in numlist and numlist.index(digit3)!=2:
            result.append(0)
            
        if numlist[1] == digit2:
            result.append(1) 
        elif digit2 in numlist and numlist.index(digit2)!=1:
            result.append(0)
            
        if numlist[0] == digit1:      
            result.append(1)
        elif digit1 in numlist and numlist.index(digit1)!=0:
            result.append(0)
            
        itwin = result.count(1)
        itwin1 = len(result)-itwin
        if itwin==3:
            print("You got it!")
            return 1
        else:
            print("Fermi "*itwin+"Pico "*itwin1) 
            
    return 0


if __name__ == "__main__":
    print(DESCRIPTION)
    
    continuePlay = "yes"
    while continuePlay=="yes":
        numlist = selectAnum()
        print("I have thought up a number. You have 10 guesses to get it.")
        
        #start guess
        countGuess = 1
        ifwin = 0
        while countGuess<11 and not ifwin:
            print("Guess #"+str(countGuess)+":")
            ifwin = oneGuess()
            countGuess+=1
        
        if ifwin==0:
            print("You lost it!")
            
        print("Do you want to play again? (yes or no)")
        continuePlay=input().lower()
        
        