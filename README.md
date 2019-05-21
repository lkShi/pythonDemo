# python练习

#TDD *(test-driven development)测试驱动开发*
        TDD是一种开发方式，就是在正式开发之前，先确定关键点，并事先指定这些关键点什么样是正常的，什么样是异常的。例如，
     age变量就是一个关键点，该变量值必须满足 age >= 18 才是正常的。如果程序由于某些原因（可能是修改程序，修改数
     据库，获取这其他原因），age < 18 了 ，这是TDD就会通知开发人员，age 变量异常。因此，通过 TDD 可以及时发现
     程序中的bug或异常，以便及时处理。也就是在开发程序之前，为程序画了一个安全区，如果越过安全区，开发人员就会知晓
# exec (param1,param2,param3)
    exec 函数有3个参数，param1 = 指需要运行的语句，
                     param2 = 指作用域，目前还不懂作用域怎么使用
                     param3 = 可以将作用域中的值传入 语句中，参数名要对应
```python
    a = 20
    args = {'a':20,'b':30}
    scop ={}
    exec('print(a+b)',scop,args)
```
# eval 
    eval与exec类似，只不过，这个eval可以返回值，比如返回 表达式的值
```python
    eval('1+2-4')
    eval('2 *(6-4)')
    scop = {'x':20}
    args={'y':40}
    eval('x+y',scop,args)
```