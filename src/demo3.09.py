import random

x = 0
while x <= 10 :
    x += 1
    if x == random.randint(1,20):
        print(x)
        break
else:
    print("没有中断 While 循环")

numbers = [1,2,3,4,5,6]

for number in numbers:
    if number == random.randint(1,20):
        print(number)
        break
else:
    print("正常退出循环")