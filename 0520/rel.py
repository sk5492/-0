#비교 연산자 : 두 수의 비교 결과를 boolean(True, False)
a = int(input("첫 번째 수 입력 : "))
b = int(input("두 번째 수 입력 : "))

print(a, '==', b, '->', (a==b))        #같은지 판별
print(a, '!=', b, '->', (a!=b))        #같지 않음
print(a, '>', b, '->', (a>b))        #적다
print(a, '<', b, '->', (a<b))        #크다
print(a, '>=', b, '->', (a>=b))        #작거나 동일하다
print(a, '<=', b, '->', (a<=b))        #크거나 동일하다
