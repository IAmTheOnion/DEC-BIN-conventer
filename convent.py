def DEC2BIN(num):
    if num == 0:
        return 0
    else:
        return (num % 2 + 10 *
                DEC2BIN(int(decimal_number // 2)))
 


def OCT2DEC(num, i):
    if num >=0 and num <= 7:
        return num*pow(8, i) 
    last_digit = num % 10
    return (pow(8, i) * last_digit) + OCT2BIN(num // 10, i+1)
