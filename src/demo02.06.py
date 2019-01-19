x= 1234.56789
print(format(x,'0.2f')) #保留2位小数
print(format(x,'>12.1f')) #12个长度内保留1位小数右对齐
print(format(x,'<12.3f')) #12个长度内保留3位小数左对齐
print(format(x,'0>12.1f'))#12个长度内保留1位小数，右对齐，数字前面补充0
print(format(x,'0<12.1f'))#12个长度内保留1位小数，左对齐，数字后面补充0
print(format(x,'^12.1f'))#12个长度内，中心对齐，保留1位小数
print(format(x,','))#每千分位，分隔
print(format(x,',.2f'))#每千分位，分隔并 保留2位小数
print(format(x,'e'))#科学计数法
print(format(x,'0.2e'))#科学计数法，保留两位小数