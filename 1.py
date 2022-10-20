a = int(input("Введите число:"))
cc = int(input("Введите целевую систему счисления:"))

while cc != 2 and cc != 8:
    print("Введена неправильная система счисления")
    cc = int(input("Введите целевую систему счисления:"))

if cc == 2:
    def otvet(x, d = ''):
        while x > 0:
                d = str(x % 2) + d
                x = x // 2
        return d

if cc == 8:
    def otvet(x, d = ''):
        while x > 0:
                d = str(x % 8) + d
                x = x // 8
        return d

print(otvet(a))