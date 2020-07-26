


def appendtest(newitem, lista=[]):
    print(id(lista))
    lista.append(newitem)
    print(id(lista))
    return lista


print(appendtest(1)) # [1]

print(appendtest('a')) # [1,'a']

# python 函数中传递的是对象，可变对象在调用者和被调用这之间共享，因此当首次调用
# appendtest(1) 的时候，[]-->[1] ,当再次调用时候由于默认参数不会重新计算，在[1]的基础上
# 添加了 [1,'a']
# 如果要避免这种事情发生，那么可以将参数设置为lista = None,在函数内部进行操作。