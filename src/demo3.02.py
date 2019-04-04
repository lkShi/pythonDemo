x,y,z = 1,2,3
print(x,y,z);

x,y = y,x
print(x,y)

# x,y,z = 1,2 抛出异常
# x,y = 1,2,3 抛出异常
x = y =20

print(x,y)

x *=2 #增量赋值
print(x)
x %=3 #增量赋值
print(x)