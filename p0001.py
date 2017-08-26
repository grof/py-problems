import math

def mult(a,b,n):
    len_a = (n-1)/a
    len_b = (n-1)/b
    len_ab = (n-1)/(a*b)
    
    sum_a = a * len_a * (len_a + 1) / 2
    sum_b = b * len_b * (len_b + 1) / 2
    sum_ab = a * b * len_ab * (len_ab + 1) / 2

    sum_n = sum_a + sum_b - sum_ab

    return sum_n


print mult(3, 5, 1000)
