#Program: 6b
#Names: Walter, John
#Date: 10/20/2016
#Instructor: Jeff Light
#Description: Receives variables x and y, and calculates x to power of y.

def power(x, y):
    #multiples x by itself, doing this y-1 times
    for count in range(0,y-1):
        x *= x
    return x    

def main(): #main function need in all programs for automated testing
    #program continues until typing Ctrl-C
    while True:
        #asks for input, calls power with x and y as arguments
        print ("Enter x:")
        x = int(input());
        print ("Enter y:")
        y = int(input());
        answer = power(x,y)
        print ("x raised to y is " + str(answer))
        print()
    
if __name__ == '__main__':
    main()  #excucte main function
