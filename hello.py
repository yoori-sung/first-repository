def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 사용 예시
num1 = 54
num2 = 24
result = gcd(num1, num2)
print(f"{num1}와 {num2}의 최대공약수는 {result}입니다.")