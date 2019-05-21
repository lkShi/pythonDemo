x=0
while x< 100:
    if x == 5:
        break
    print(x, end=" ")
    x += 1
names= ["Bill","Nike","Joan"]
print("\n 在for循环中使用break")

for name in names:
    if not name.startswith("B"):
        break
    print(name)

print("\n continue 在for循环中的使用")
for name in names:
    if name.startswith("B"):
        continue
    print(name)

print("\n 嵌套循环")

arr1 = [1, 2, 3, 4, 5]
arr2 = ["Bill", "Arr", "Nike"]
arr = [arr1, arr2]

i = 0
while i < len(arr):
    for value in arr[i]:
        print(value, end=" ")
    i += 1
    print(" ")