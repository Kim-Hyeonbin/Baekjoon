A, B = map(int, input().split())

# 최대공약수 구하기 (유클리드 호제법)
a, b = A, B
while b != 0:
    a, b = b, a % b
gcd = a

# 최소공배수 구하기
lcm = A * B // gcd

print(f"{gcd}\n{lcm}")
