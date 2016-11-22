#Program: 10b
#Names: Riley Maxwell, John Diaz
#Date: 11/18/2016
#Instructor: Daffy Duck
#Description: Updated shopping list program

import shelve
from single import get_command

def addItems(shoppingList): #add items...
    while True:
        print("Add item to the list <item:amount>: ")
        item = input()
        if item == '':
            break
        else: #adds item to list
            try:
                colon = item.index(':')
            except:
                print('Please try again!')
                continue
            junk = item[:colon].strip()
            number = item[colon + 1:].strip()
            newItem = junk + ':' + number
            shoppingList.append(newItem)
            print('Item added: ' + newItem)
       
    #end
    
def deleteItems(shoppingList): #delete items...
    print("Here is the Delete Items menu")
    printItems(shoppingList)
    while True:
        print("Delete item: ")
        item = str(input())
        if item == '':
            break
        elif item in shoppingList: #removes if in list
            shoppingList.remove(item)
            print('Item deleted: ' + item)
        else:
            print("Not in the list.")
            continue    
    #end

def printItems(shoppingList):
    print()
    if (len(shoppingList) > 0):
        print('Shopping List'.center(20, '-'))
        for i in range(len(shoppingList)): #prints each item individually
            colon = shoppingList[i].index(':')
            junk = shoppingList[i][:colon]
            number = (shoppingList[i])[colon + 1:]
            print(junk.ljust(15,'.') + number.rjust(5))
    else:
        print('Nothing loaded. Shopping list is empty')
    print()
    #end

def sortItems(shoppingList):
    shoppingList.sort()
    printItems(shoppingList)
    #end


def save(shoppingList,shelfList):
    
    print('\nList saved\n')
    shelfList['shoppingList'] = shoppingList

    
def load(shoppingList,shelfList): #loads the list and calls the print function
    
    try:
        theShelf = shelfList['shoppingList']
        for delI in range(len(shoppingList)):   
            del shoppingList[delI]
        for addI in range(len(theShelf)):
            shoppingList.append(theShelf[addI])
        printItems(shoppingList)
        #return shelfList['shoppingList']
        
    except:
        print('\nNo list saved!\n')
    

def main(): #main function need in all programs for automated testing

    shelfList = shelve.open('mydata')
    #your program goes here
    shoppingList = []
    while True:
        print("1. Add Items")
        print("2. Delete Item")
        print("3. Show Items")
        print("4. Sort Items")
        print("5. Save List")
        print("6. Load List")
        print("7. Exit")
        print('enter a command ',end='')
        cmd = int(get_command(['1','2','3','4','5','6','7'])) #gets user input
     
        if cmd == 1:
            addItems(shoppingList)
        elif cmd == 2:
            deleteItems(shoppingList)
        elif cmd == 3:
            printItems(shoppingList)
        elif cmd == 4:
            sortItems(shoppingList)
        elif cmd == 5: #save list
            save(shoppingList,shelfList)
        elif cmd == 6:
            load(shoppingList,shelfList)
        elif cmd == 7:
            break
    shelfList.close()
 
if __name__ == '__main__':
    main()  #excucte main function
