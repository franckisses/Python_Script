
# 此类写法可以在外部直接通过 from Package import 函数
# from .module1 import moudule1
# from .module2 import moudule2

# 定义在模块倒入的时候，加载的变量，里边是字符串
__all__ = ['module1', 'module2', 'subpackage']
# 可以控制倒入的参数的数量，保持干净的环境变量