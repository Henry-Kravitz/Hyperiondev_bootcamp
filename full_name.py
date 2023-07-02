name = input('Enter Your Name:   ') # The user enters there name
if len(name) == 0:
    print("You haven't entered anything. Please enter your full name.") # If the user doesnt enter a name this mesxage is printed

elif len(name) >= 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.") # If the user's name equals or is more than 25 characters this message is printred

elif len(name) <=4:
    print('Please make sure that you have entered your name and surname')
    
else: print("Thank you for entering your name.") # Prints a message