print('<Hello \n World>')
#str函数将1234转换为字符串
print(str(1234))
#len函数不能直接获取数字的长度
# print(len(1234)) 不能直接获取数字的长度
print(len(str(1234)))
print(str('<Hello \n World>'))
print(repr('<hello \n world>'))
print(len(str('<Hello \n World>')))
print(len(repr(str('<Hello \n World>'))))
print(len(repr('<Hello \n World>')))
print('<Hello \\n World>')
print(len('<hello \\n world>'))
print(r'hello \n world')
print(len(r'<hello \n world>'))#并不计算r