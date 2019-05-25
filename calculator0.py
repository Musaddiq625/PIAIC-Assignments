import os
while True:
    os.system('cls')
    print(" *** Calculator ***")
    try:
        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))
    except ValueError:
        print("Please Enter Only Integer Value!")
    restart = 'n'
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus")
    sel = int(input("Select Option No. ..? : "))
    if sel == 1:
        print("Addition")
        result = num1 + num2
        print("Addition of "+str(num1)+" and "+str(num2)+" is: "+str(result))
    elif sel == 2:
        print("Subtraction")
        result = num1 - num2
        print("Subtraction of "+str(num1)+" and "+str(num2)+" is: "+str(result))
    elif sel == 3:
        print("Multiplication")
        result = num1 * num2
        print("Multiplication of "+str(num1)+" and "+str(num2)+" is: "+str(result))
    elif sel == 4:
        print("Division")
        if num2 == 0:
            print("Error!\nCannot divide by zero")
        else:
            result = num1 / num2
            print("Division of "+str(num1)+" and "+str(num2)+" is: "+str(result))
    elif sel == 5:
        print("Modulus")
        result = num1 % num2
        print("Modulus of "+str(num1)+" and "+str(num2)+" is: "+str(result))
    else:
        print("Error!")

    while True:
        restart = input('\nDo you want to Restart (y/n): ')
        if restart in ('y', 'n'):
            break
        print("Invalid input")
    if restart == 'y':
        continue
    else:
        print ('Ba-Bye')
        break