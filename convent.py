def DEC2BIN(num):
    if num == 0:
        return 0
    else:
        return (num % 2 + 10 *
                DEC2BIN(int(num // 2)))


def OCT2DEC(num, i=0):
    if num >= 0 and num <= 7:
        return num * pow(8, i)
    last_digit = num % 10
    return (pow(8, i) * last_digit) + OCT2DEC(num // 10, i + 1)


def HEX2DEC(num):
    ch = dec = i = 0
    length = len(num) - 1
    while length >= 0:
        if num[length] >= '0' and num[length] <= '9':
            temp = int(num[length])
        elif num[length] >= 'A' and num[length] <= 'F':
            temp = ord(num[length]) - 55
        elif num[length] >= 'a' and num[length] <= 'f':
            temp = ord(num[length]) - 87
        else:
            ch = 1
            break
        dec = dec + (temp * (16 ** i))
        length = length - 1
        i = i + 1
    return dec


def BIN2DEC(num, pow, total):
    num = str(num)
    if (len(num) == 1):
        return int(num) * (2 ** pow) + total
    else:
        n = int(num[-1:])
        total += (n * (2 ** pow))
        return BIN2DEC(num[:-1], pow + 1, total)


def isHEX(s):
    hex_digits = set("0123456789abcdefABCDEF")
    for char in s:
        if not (char in hex_digits):
            return False
    return True


def isOCT(s):
    s = str(s)
    oct_digits = set("1234567")
    for char in s:
        if not (char in oct_digits):
            return False
    return True


def isBIN(s):
    s = str(s)
    oct_digits = set("01")
    for char in s:
        if not (char in oct_digits):
            return False
    return True


choice = 0
while choice != 7:
    choice = int(input("\n1.DEC -> BIN   2.OCT -> BIN   3.HEX -> BIN   4.BIN -> DEC   5.OCT -> DEC   6. HEX -> DEC   7.End App \n"))

    if choice == 1:
        num = int(input("Podaj liczbe w formacie DEC \n"))
        if type(num) == int:
            print(DEC2BIN(num))
        else:
            print("Nieprawidłowy Format")

    elif choice == 2:
        num = int(input("Podaj liczbe w formacie OCT \n"))
        if isOCT(num):
            print(DEC2BIN(OCT2DEC(num)))
        else:
            print("Nieprawidłowy Format")

    elif choice == 3:
        num = input("Podaj liczbe w formacie HEX \n")
        if isHEX(num):
            print(DEC2BIN(HEX2DEC(num)))
        else:
            print("Nieprawidłowy Format")

    elif choice == 4:
        num = int(input("Podaj liczbe w formacie BIN \n"))
        if isBIN(num):
            print(BIN2DEC(num, 0, 0))
        else:
            print("Nieprawidłowy Format")

    elif choice == 5:
        num = int(input("Podaj liczbe w formacie OCT \n"))
        if isOCT(num):
            print(OCT2DEC(num))
        else:
            print("Nieprawidłowy Format")

    elif choice == 6:
        num = input("Podaj liczbe w formacie HEX \n")
        if isHEX(num):
            print(HEX2DEC(num))
        else:
            print("Nieprawidłowy Format")
