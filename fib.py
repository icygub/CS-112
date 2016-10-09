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

while (numFibLoop-1) > 0:
    newFib = currentFib + prevFib
    print (newFib)
    prevFib = currentFib
    currentFib = newFib
    numFibLoop -= 1
        
