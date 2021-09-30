#Defining a function to calculate the range of values.
def calcValues(low_num,upper_num,choice):
    evenlist = []#Defining an even list array to hold even numbers
    oddlist = []#Defining an odd list array to hold odd numbers
   
   #statement outputs a list of even numbers or odd numbers within the range depending on what the user chooses.
    for value in range(low_num,upper_num): 
        if(value%2==0):
            evenlist.append(value)
        else:
            oddlist.append(value)
    if choice == 'E':
        print(evenlist)
    elif choice == 'O':
        print(oddlist)
    else:
        print('Invalid')

def UserInput(): # Defining a user input function.
    while True: #Exception handling
        try:
            Lower_limit=int(input("Enter the first number for range: ")) #Allows user to input a value for lower limit
        except ValueError:
            print('Sorry I did not understand that')
            continue
        else:
            break
    while True:
        try:
            Upper_limit=int(input("Enter the second number for range: ")) #Allows user to input a value for an upper limit
        except ValueError:
            print('Sorry I did not understand that')
            continue
        else:
            break
    userchoice = str(input('Do you want to display even(E) or odd(O)?  ')) #Allows a user to make a choice: (E) or (O)
    return calcValues(Lower_limit,Upper_limit,userchoice.upper()) 

UserInput() #Calls the userInput function

tryAgain = str(input('Do you want to run this again? Y/N:  '))

while tryAgain.upper() == 'Y':
    UserInput()
    tryAgain = str(input('Do you want to run this again? Y/N:  '))
else:
    if tryAgain.upper() == 'N':
       print('Thank You for using the program')
    else:
        print('Invalid Input')