i = True
while i:
    a=input("Enter the first number: ").strip()
    b=input("Enter the second number: ").strip()
    c=input("Enter a operator choice(+, -, *, /, %): ").strip()
    op = ['+', '-', '*', '/', '%']
    if c not in op:
        print("Invalid operator")
        continue

    else:
        print(eval(a+c+b))
        i = True if input("do you want to calculate more?(yes/no) ") == 'yes' else False
print("Thank you, Good byee!")
