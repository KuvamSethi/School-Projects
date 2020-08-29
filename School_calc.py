a = "Advanced Calculator"
print()
print(" "*4, "~" * len(a))
print(" "*4, a)
print(" "*4, "~" * len(a))
print()
print("Choice\t\tOperator")
print("-" * 35)
print(" 1\t\tAddition(+)")
print("-" * 35)
print(" 2 \t\tSubtraction(-)")
print("-" * 35)
print(" 3 \t\tMultiplication(*)")
print("-" * 35)
print(" 4 \t\tDivision(/)")
print("-" * 35)
print(" 5 \t\tFloor Division(//)")
print("-" * 35)
print(" 6 \t\tRemainder(%)")
print("-" * 35)
print(" 7 \t\tPower(xⁿ)")
print("-" * 35)
print(" 8 \t\tSquare(x²)")
print("-" * 35)
print(" 9 \t\tCube(x³)")
print("-" * 35)
print(" 10 \t\tSquare Root(√x)")
print("-" * 35)
print(" 11 \t\tCube Root(∛x)")
print("-" * 35)
print(" 12 \t\tNth Root(ⁿ√x)")
print("-" * 35)
print(" 13 \t\tReset")
print("-" * 35)
print(" 14 \t\tExit")
print("-" * 35)
print()

First_no = float(input("\nEnter Number(that needs to be operated) : "))
Result = First_no
new_result = 0

while True:
    choice = input("Enter your Choice : ")
    if choice == "1":
        while True:
            print("\nYou selected ADDITION(+) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    if new_result != 0:
                        print(f"Current Number : {Result}")
                    a = float(input(f"Enter the Number to be Added to {Result} : "))
                    prev_Result = Result
                    Result += a
                    new_result = 1
                    ans = f"Final Result : {prev_Result} + {a} = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "2":
        while True:
            print("\nYou selected SUBTRACTION(-) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    if new_result != 0:
                        print(f"Current Number : {Result}")
                    a = float(input(f"Enter the Number to be Subtracted to {Result} : "))
                    prev_Result = Result
                    Result -= a
                    new_result = 1
                    ans = f"Final Result : {prev_Result} - {a} = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "3":
        while True:
            print("\nYou selected MULTIPLICATION(*) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    if new_result != 0:
                        print(f"Current Number : {Result}")
                    a = float(input(f"Enter the Number to be Multiplied to {Result} : "))
                    prev_Result = Result
                    Result *= a
                    new_result = 1
                    ans = f"Final Result : {prev_Result} * {a} = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "4":
        while True:
            print("\nYou selected DIVISION(/) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    print(f"Numerator : {Result}")
                    a = float(input(f"Enter the Number to be Divided to {Result} : "))
                    prev_Result = Result
                    Result /= a
                    new_result = 1
                    ans = f"Final Result : {prev_Result} / {a} = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "5":
        while True:
            print("\nYou selected FLOOR DIVISION(//) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    print(f"Numerator : {Result}")
                    a = float(input("Enter the Denominator : "))
                    prev_Result = Result
                    Result //= a
                    new_result = 1
                    ans = f"Final Result : {prev_Result} // {a} = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "6":
        while True:
            print("\nYou selected REMAINDER(%) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    print(f"Numerator : {Result}")
                    a = float(input("Enter the Denominator : "))
                    prev_Result = Result
                    Result %= a
                    new_result = 1
                    ans = f"Final Result : {prev_Result} % {a} = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "7":
        while True:
            print("\nYou selected POWER(**) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    print(f"Base Number : {Result}")
                    a = float(input("Enter Exponent : "))
                    prev_Result = Result
                    Result **= a
                    new_result = 1
                    ans = f"Final Result : {prev_Result} ** {a} = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "8":
        while True:
            print("\nYou selected SQUARE(x²) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    if new_result != 0:
                        print(f"Current Number : {Result}")
                    prev_Result = Result
                    Result **= 2
                    new_result = 1
                    ans = f"Final Result : {prev_Result} ^ 2 = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "9":
        while True:
            print("\nYou selected CUBE(x³) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    if new_result != 0:
                        print(f"Current Number : {Result}")
                    prev_Result = Result
                    Result **= 3
                    new_result = 1
                    ans = f"Final Result : {prev_Result} ^ 3 = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "10":
        while True:
            print("\nYou selected SQUARE ROOT(√x) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    if new_result != 0:
                        print(f"Current Number : {Result}")
                    prev_Result = Result
                    Result **= 1/2
                    new_result = 1
                    ans = f"Final Result : √{prev_Result} = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "11":
        while True:
            print("\nYou selected CUBE ROOT(∛x) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    if new_result != 0:
                        print(f"Current Number : {Result}")
                    prev_Result = Result
                    Result **= 1/3
                    new_result = 1
                    ans = f"Final Result : ∛{prev_Result} = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "12":
        while True:
            print("\nYou selected Nth ROOT(ⁿ√x) OPERATION..")
            confirm = input("Do you want to CONFIRM or RESET your choice (C/R) : ")
            print()
            if confirm in "Cc":
                while True:
                    if new_result != 0:
                        print(f"Current Number : {Result}")
                    a = float(input("Enter the  Value of n : "))
                    prev_Result = Result
                    Result **= 1/a
                    new_result = 1
                    ans = f"Final Result : {a} √{prev_Result} = {Result}"
                    print()
                    print("=" * len(ans))
                    print(ans)
                    print("=" * len(ans))
                    print()
                    print()
                    inp = input("Do you want to -\n\n-> Y:Calculate with a different operator\n-> R:Repeat Operator\n-> N:Exit Calculator\n\nInput (Y/R/N) : ")
                    print()
                    if inp in "rR":
                        continue
                    elif inp in "yY":
                        break
                    elif inp in "nN":
                        final = f"Final Answer : {Result}"
                        print("=" * len(final))
                        print(final)
                        print("=" * len(final))
                        print()
                        print("Thank you for using our Calculator:)")
                        break
            elif confirm in "rR":
                break
            break
        break
    elif choice == "13":
        while True:
            Result = float(input("Enter A New Number : "))
            new_result = 0
            break
    elif choice == "14":
        if new_result != 0:
            print()
            final = f"Final Answer : {Result}"
            print("=" * len(final))
            print(final)
            print("=" * len(final))
        else:
            print("\nThere was no Calculation performed")
        print("Thank you for using our Calculator:)")
        break




