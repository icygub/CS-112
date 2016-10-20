#6d
#Walter and John
#10/20/2016
#Professor: Brother Light
#Description: 

def is_float(num):
    result = False
    try:
        float(num)
        result = True
    except ValueError:
        result = False        
    return result
        
def main():
    while True:
        print("Enter something:")
        num = input()
        tOrF = is_float(num)
        if (tOrF == True):
            print("Is a float!")
        else:
            print("Not a float!")
    
    
if __name__ == '__main__':
    main()
