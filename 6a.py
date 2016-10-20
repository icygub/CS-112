#Program: 6a 
#Names: John, Walter
#Date: 10/18/2016
#Instructor: Jeff Light
#Description:  A program that receives as parameters three numbers and returns the largest number.

#Get the max number here
def max_num(first, second, third):
    if(first >= second and first >= third):  
        return first        
    elif (second >= first and second >= third):
        return second
    else:    
        return third       

def main():
    while True:
        #asks for user input
        print ('Enter first number:')
        first = int(input())
        print ('Enter second number:')
        second = int(input())
        print ('Enter third number:')
        third = int(input())
        max = max_num(first, second, third)
        print('Largest number is ' + str(max))
        
if __name__ == '__main__':
    main()  #excucte main function
