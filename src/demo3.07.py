print(1,end=" ")
print(2,end=" ")
print(3,end=" ")
print(4,end=" ")
print(5,end=" ")
print(6,end=" ")
print(7,end=" ")
print(8,end=" ")
print(9,end=" ")
print(10,end=" ")

print("\n 用while循环输出 1~10")
x = 1
while x<=10:
    print(x,end=" ")
    x += 1

print("\n 使用一个列表")

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    print(number,end=" ")

numbers = range(1,10000)
print("\n 用for循环列表中的值")

for number in numbers:
    print(number,end=" ")

print("\n 1-100 的乘积")
numbers = range(1,1001)
for number in numbers:
    print(number * number,end=" ")
