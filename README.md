# Calulator-Python
Basic,Here I share a simple calculator in python language 

# Bahasa Indonesia
  
 ```py
 print("Calulator Python".center(30,"="))
print("""Metode:
[+] Tambah
[-] Kurang
[*] Kali
[/] Bagi
""")
while True:
    num = int(input("\nMasukan angka: "))
    mtd = input("Metode: ")
    num1 = int(input("masukan angka kedua: "))
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
        print("Masukan metode yang valid!!") 
 ```
