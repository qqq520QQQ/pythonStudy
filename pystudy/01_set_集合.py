# 定义集合
my_set = {'ithema', 'aijidiajos', 'asdasdas', 'asddadas', 'asdasdas', 'asddadas'}
my_set_empty = set()
print(f'my_set的内容是: {my_set}, 类型是：{type(my_set)}')
print(f'my_set的内容是: {my_set_empty}, 类型是：{type(my_set_empty)}')

# 集合不支持下标索引  允许修改
# 添加新元素add()方法
my_set.add('python')
# 添加无效
my_set.add('ithema')
print(f'添加元素后的my_set：{my_set}')

# 移除元素
my_set.remove('python')
print(f'移除元素后的my_set：{my_set}')

# 随机取元素
element = my_set.pop()
print(f'集合被取出元素是：{element}， 取出后集合：{my_set}')

# 清空集合
my_set.clear()
print(f'集合被清空后：{my_set}')

# 取两个集合的差集 集合1有而集合2没有的元素
set1 = {1,2,3}
set2 = {1,6,5}
set3 = set1.difference(set2)
print(f'取出差集后的结构是：{set3}')
print(f'取出差集后，原set1的内容{set1}')
print(f'取出差集后，原set2的内容{set2}')

# 消除两个元素的差集   在集合1内删除和集合2相同的元素
# 集合1被修改   集合2不变
set1 = {1, 2, 3}
set2 = {1, 6, 5}
set1.difference_update(set2)
print(f'消除差集后，原set1的内容{set1}')
print(f'消除差集后，原set2的内容{set2}')

# 合并集合 unior()  得到新集合   集合1， 2不变
set1 = {1, 2, 3}
set2 = {1, 6, 5}
set3 = set1.union(set2)
print(f'合并后:{set3}')
print(f'合并后，原set1的内容{set1}')
print(f'合并后，原set2的内容{set2}')