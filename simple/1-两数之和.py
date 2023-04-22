"""
题目:
    1) 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。

    2) 数组中同一个元素在答案里不能重复出现

"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lens = len(nums)
    hash_dict = {

    }
    print(nums)
    # 创建查找字典
    for lindex, lvalue in enumerate(nums):
        # 索引当字典的value
        hash_dict[lvalue] = lindex
    print('创建查询表:', hash_dict)

    i = 0
    # 一个for循环完所有值, 且每次循环查找字典有没有符合条件的key取出索引
    for lvalue in nums:

        res = hash_dict.get(target - lvalue)

        print(i, '-', lvalue, ':', res)

        # 判断字典取出的索引和列表的索引是否相等
        if res is not None and res != i:
            return [i, res]

        i += 1


"""

for lvalue in enumerate(hash_dict):
    # 取出值对应的索引
    i = hash_dict[lvalue]
    
    # 在字典内搜索和答案值相同的key值
    res = hash_dict.get(target - lvalue)
    
    # 返回当前索引
    if res is not None and res != i:
        return [i, res]
    
    # 当前索引下, 找不到答案, 进入下一个索引
    
    
该写法无法避免字典key重复问题


定义新索引跟原索引绑定, 遇到相同key的时候新索引和旧索引不同满足if

    for new_index, lvalue in enumerate(hash_dict):

        new_dict[lvalue] = new_index
        
        res = hash_dict.get(target - lvalue)

        if res is not None and res != new_index:
            return [new_index, res]
            
"""
# [2, 3, 3, 3, 9]
# 转字典
# { 2:0, 3:3, 9:4}
# 新索引
#  2:0      3:3       9:4
#   ↑        ↑         ↑
#   0        1         2
# 0->2<-0  1->3<-3  2->2<-4
# 新旧索引指向同一个值
if __name__ == '__main__':
    print('答案: ', twoSum([3, 3, 3, 1, 9], 10))
