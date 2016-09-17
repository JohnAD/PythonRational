def decimal_integer_divide(numerator, denominator, prec=8):
    '''
        divide numerator by denominator where both are decimal string
        representations of integers
    '''
    answer = ""
    n = [int(digit) for digit in numerator if digit in ['0','1','2','3','4','5','6','7','8','9']]
    d = int(denominator)
    # print "n", n
    remainder = 0
    decimalGenerated = False
    nonZeroDigitSeen = False
    decimalCount = 0

    # part 1: everything before the decimal point
    #
    while len(n):
        remainder = remainder*10+n.pop(0)
        if d <= remainder:
            next_digit = remainder / d
            remainder = remainder % d
            nonZeroDigitSeen = True
            answer += str(next_digit)
        else:
            if nonZeroDigitSeen:
                answer += "0"

    # part 2: everything after the decimal point
    #
    if remainder==0:
        return answer
    if nonZeroDigitSeen:
        answer += "."
    else:
        answer += "0."
    while True:
        remainder = remainder*10
        if d <= remainder:
            next_digit = remainder / d
            remainder = remainder % d
        else:
            if remainder==0:
                break
            next_digit = 0
        answer += str(next_digit)
        decimalCount += 1
        if decimalCount>=prec:
            break
    return answer

# TODO: handle negative numbers
# TODO: round last digit based on precision
# TODO: properly move precision based on first non-zero digit?

import random
for i in range(15):
    n = int(random.random()*50000)+1
    d = int(random.random()*50000)+1
    # n = 1534
    # d = 3
    print "{} / {}".format(n, d)
    f = 1.0*n/d
    print "  answer with float: {}".format(str(f))
    a = decimal_integer_divide(str(n), str(d), prec=12)
    print "  answer with fraction: ", a
print "done"
