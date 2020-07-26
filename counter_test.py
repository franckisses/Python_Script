
from collections import Counter

print(Counter('success')) # 可迭代对象
a = Counter('success')
print('-'*30)

print(Counter(s=3,c=2,e=1,u=1))

# elements获取counter中的key值
print(list(a.elements()))
# most_common(N) 获取出现频率N高的值
print(a.most_common(2))