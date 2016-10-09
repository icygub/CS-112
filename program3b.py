#Program: 3b
#Names: John, Joseph
#Date: 9/27/2016
#Instructor: Bro. Light
#Description: This program represents a Body Mass Index (BMI) that calculates a person's height and weight.


def main(): #main function need in all programs for automated testing

    pounds = float(input('Enter weight in pounds: '))
    inches = float(input('Enter height in inches: '))
    kg = 0.45359237001 * pounds
    m = 0.0254 * inches
    bmi = round(kg/(m**2),2)

    if bmi < 18.5:
        print('BMI is', bmi, 'Underweight')
    elif bmi >= 18.5 and bmi < 24.9:
        print('BMI is', bmi,'Normal')
    elif bmi >= 25.0 and bmi < 29.9:
        print('BMI is', bmi,'Overweight')
    else:
        print('BMI is',bmi,'Obese')

    choice = input('Again? (y/n)')
    if choice == 'y' or choice == 'Y':
        main()
    elif choice == 'n' or choice == 'N':
        print('Bye')
    else:
        print('I guess that means bye')
        
    

if __name__ == '__main__':
    main()  #excucte main function
