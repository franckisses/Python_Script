"""
 this is for python module  test!
"""

# from Packages.module1 import moudule1

#print('this is start import [from Packages.module1 import moudule1]')
#moudule1()

# from Packages import moudule2,moudule1

# moudule1()
# print('---'*20)
# moudule2()



from Packages import * 
# just import __all__ list variable!
print(dir())

module1.moudule1()