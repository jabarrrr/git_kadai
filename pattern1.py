import math

#数字入力
a = int(input('1つ目の数字を入力してください。:'))
b = int(input('2つ目の数字を入力してください。:'))

#四則演算
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

#最小公倍数と最大公約数
print("最小公倍数:", math.lcm(a,b))
print("最大公約数:", math.gcd(a,b))

#剰余
print("a / b の余り:", a % b)

#aとbの間に存在する整数の和
total=0
if b>=a:
    for i in range(b-a+1):
        total=total+i+a
else:
    for i in range(a-b+1):
        total=total+i+b
print("aからbまでの整数の和:", total)

#べき乗
print("aのべき乗:", a ** b)
print("bのべき乗:", b ** a)