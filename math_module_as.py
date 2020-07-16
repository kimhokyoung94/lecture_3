import math as mt

def math_pow(n):
    a = int(input("원하는 숫자를 입력하세요"))
    b = int(input("원하는 제곱의 범위를 입력하세요"))
    for i in range(1,b+1):
        result = mt.pow(a,i)
        result_words = '{}**{} = {}'.format(a,i,result)
        result1 = mt.pow(n,i)
        result1_words = '{}**{} = {}'.format(n,i,result1)
        print(result_words)
        print(result1_words)

       



