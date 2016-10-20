#6c
#Walter and John
#10/20/2016
#Professor: Brother Light
#Description: User inputs three numbers. Calculates if first is between second and third

def between(first, second, third):
    result = False
    if ((first > second and first < third) or (first < second and first > third)):
        result = True
    return result

	

def main():
    while True:
        print("Enter first number:")
        first = int(input())
        print("Enter second number:")
        second = int(input())
        print("Enter third number:")
        third = int(input())
        result = between(first, second, third)
        print("Result is " + str(result))
        print()

if __name__ == '__main__':
    main()
