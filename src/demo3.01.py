# 输出使用空格分割符的多参数值
print("name =", "Bill");
# 输出用空格分隔的多参数值
print("age =", 30);
# 使用加号（+）连接字符串
print("Apple"+","+"Orange"+","+"Banana");
# 修改多参数值分隔符为逗号（，）,然后输出多参数值
print("Apple", "Orange", "Banana", sep=",");
# 修改多参数值分隔符为（&），然后输出多参数值
print("Can", "you", "tell", "me", "how", "to", "get", "to", "the","nearest", "tube","station",sep="&");
# 运行结果 Hello World
print("Hello",end="");
print("World");
# 修改输出字符串结尾符为长度为0的字符串，这样下一次调用print汉书，输出的内容不仅会在统一行而且会首尾相结，运行结果：abc
print("a",end="");
print("b",end="");
print("c");