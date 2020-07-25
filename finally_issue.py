"""
this test just for the finallu werid
"""



def ReturnTest(a):
    try:
        if a <= 0:
            raise ValueError('data can not be integer')
        else:
            return a
    except ValueError as e:
        print('[error]:',e)
    finally:
        print('the end')
        return -1

print(ReturnTest(0))
print('-'*20)
print(ReturnTest(2))

# 第二个测试是因为a > 0,会执行else分支，但是由于存在finally语句，此时会先执行finally语句
# finally语句中存在return 此时直接返回。
#  