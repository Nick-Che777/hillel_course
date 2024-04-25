def додавання(x, y):
    return x + y

def віднімання(x, y):
    return x - y

def множення(x, y):
    return x * y

def ділення(x, y):
    if y == 0:
        return
    else:
        return x / y

print("виконати дію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

дія = input("Ввести номер дії (1/2/3/4): ")

first = int(input("enter number: "))
second = int(input("enter number: "))

if дія == '1':
    print("Результат:", додавання(first, second))
elif дія == '2':
    print("Результат:", віднімання(first, second))
elif дія == '3':
    print("Результат:", множення(first, second))
elif дія == '4':
    print("Результат:", ділення(first, second))
else:
    print("")
