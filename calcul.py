print("Calulator Python".center(30,"="))
print("""Method:
[+] increment
[-] Subtraction
[*] Multiplication
[/] Distribution
""")
while True:
    num = int(input("\n Enter the first number: "))
    mtd = input("Method: ")
    num1 = int(input("Enter the second number: "))
    if mtd == '+':
        hasil = num + num1
        print(num ,"+", num1 ,"=",hasil)
    elif mtd == '-':
        hasil = num - num1
        print(num ,"-", num1 ,"=",hasil)
    elif mtd == '/':
        hasil = num / num1
        print(num ,"/", num1 ,"=",hasil)
    elif mtd == '*':
        hasil = num * num1
        print(num ,"*", num1 ,"=",hasil)
    else:
        print("Enter the correct method!!")
