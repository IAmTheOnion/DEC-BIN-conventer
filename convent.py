def DEC2BIN(num):

    if num == 0:

        return 0

    else:

        return (num % 2 + 10 *

                DEC2BIN(int(decimal_number // 2)))
 
