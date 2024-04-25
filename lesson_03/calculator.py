print("perform an action:")
print("1. add")
print("2. sub")
print("3. mult")
print("4. div")

action = input("enter the action number (1/2/3/4): ")

first = int(input("enter number: "))
second = int(input("enter number: "))

if action == '1':
    print(first + second)
elif action == '2':
    print(first - second)
elif action == '3':
    print(first * second)
elif action == '4':
    if second != 0:
        print(first / second)
    else:
        print("Null forbiden")
