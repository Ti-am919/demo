user_input = input("Your number ")

if user_input.isnumeric():
    user_input = int(user_input)
    if user_input == 1:
        print("one")
    if user_input == 2:
        print("two")
    if user_input == 3:
        print("three")
    elif user_input:
        print("many")
else:
    print("enter a number")