def karatsuba(num1,num2):
    if (num1 < 10) or (num2 < 10):
        return num1 * num2

    str_num1 = str(num1)
    str_num2 = str(num2)
    m = min(len(str_num1),len(str_num2))
    mid = m//2

    a = int(str_num1[:mid])
    b = int(str_num1[mid:])
    c = int(str_num2[:mid])
    d = int(str_num2[mid:])

    z0 = karatsuba(b,d)
    z1 = karatsuba((a+b),(c+d))
    z2 = karatsuba(a,c)

    return (z2*(10**(2*mid))) + ((z1-z2-z0) * 10**mid) + z0
