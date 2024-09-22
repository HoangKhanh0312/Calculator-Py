def space():
    print("<========>")
def minus():
    a = int(input("Co bao nhieu so can tinh ?\n:"))
    number = []
    i = 1
    while i <= a:
        num = float(input(f"Nhap so thu {i}:"))
        number.append(num)
        i += 1
    sub = number[0]
    for nums in number[1:]:
        sub -= nums
    print(sub)
    space()
    main()
def plus():
    a = int(input("Co bao nhieu so can tinh ?\n:"))
    number = []
    i = 1
    while i <= a:
        num = float(input(f"Nhap so thu {i}:"))
        number.append(num)
        i += 1
    sub = number[0]
    for nums in number[1:]:
        sub += nums
    print(sub)
    space()
    main()
def multiply():
    a = int(input("Co bao nhieu so can tinh ?\n:"))
    number = []
    i = 1
    while i <= a:
        num = float(input(f"Nhap so thu {i}:"))
        number.append(num)
        i += 1
    sub = number[0]
    for nums in number[1:]:
        sub *= nums
    print(sub)
    space()
    main()
def divide():
    a = int(input("Co bao nhieu so can tinh ?\n:"))
    number = []
    i = 1
    while i <= a:
        num = float(input(f"Nhap so thu {i}:"))
        number.append(num)
        i += 1
    sub = number[0]
    for nums in number[1:]:
        sub /= nums
    print(sub)
    space()
    main()
def main():
    print("+ - x : q")
    op1 = input(":")
    op = op1.lower()
    space()
    if op == '+':
        plus()
    elif op == '-':
        divide()
    elif op == 'x' or op == '*':
        multiply()
    elif op == ':' or op == '/':
        divide()
    elif op == 'q':
        exit(0)
    else:
        main()
main()