import os           #引入模块
import sys
f_handler = open('out.log','w') #打开文件
oldstout = sys.stdout           #保存默认的python标准输出
sys.stdout = f_handler          #将输出指向f_handler 即 out.log文件
os.system('cls')                #情空控制台
sys.stdout = oldstout           #恢复标准输出