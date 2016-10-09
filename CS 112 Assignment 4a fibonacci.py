#Program: 4a
#Names: John, Walter
#Date: 10/4/2016
#Instructor: Jeff Light
#Description: Prints out fibonacci sequence up to the amount the user specifies

def main():
    #Rejects numbers <= 2, floats, or any letters
    while True:
        print ("How many Fibonacci numbers do you want (input > 2)?")
        num = input();
        if num.isdigit():
            if int(num) > 2:
                break
        print ("Please enter an integer > 2")
    
    print()
    numFibLoop = int(num)
    prevFib = 0;
    currentFib = 1;
    print(1)

    #Prints fibonacci. Length is numFibLoop variable.
    while (numFibLoop-1) > 0:
        newFib = currentFib + prevFib
        print (newFib)
        prevFib = currentFib
        currentFib = newFib
        numFibLoop -= 1
    main()    
       
    
if __name__ == '__main__':
    main()  #excucte main function
