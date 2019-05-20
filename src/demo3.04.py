name = input("你叫什么名字")
if name.startswith("Bill"):
    if(name.endswith("Gates")):
        print("欢迎 Bill Gates 先生")
    elif name.endswith("clinton"):
        print("欢迎 Bill Clinton")
    else:
        print("未知姓名")
elif name.startswith("李"):
    if name.endswith("宁"):
        print("欢迎李宁老师")
    else:
        print("未知姓名")
else:
    print("未知姓名")