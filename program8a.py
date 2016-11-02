#Program: 8a
#Names: Joseph Gonzalez & Riley Maxwell & John Diaz 
#Date: 10/31/2016
#Instructor: Bro. Light
#Description: This program adds the list of numbers input on the program


def main(): #main function need in all programs for automated testing
    
    myList = []
    
    while True:
        
        print('Please enter an integer(enter nothing to finish): ' )
        num = input()
        if num == '':
            break
        
        elif not(num.isdigit()):  #this validates if the input is a number
            print('That is not an integer! Please Try Again')
            continue
            
        myList.append(int(num)) #the append adds numbers to the list
        
        
    plus(myList) 
    
def plus(myList):
    sum = 0
    
    for i in range(len(myList)): #this statement adds all the numbers inputed
        sum += myList[i]
        
    print('Total is: ' + str(sum)) #this statement prints the result (TOTAL)
    for x in range(len(myList)): 
        
        print(str(x) + '\t' + str(myList[x])) #this statement makes the two seperate list after the total statement
        
        

if __name__ == '__main__':
    main()  #excucte main function
