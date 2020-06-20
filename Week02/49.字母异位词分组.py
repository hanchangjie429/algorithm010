#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 遍历数组，分别sort每一个字符串 然后将结果存入hashmap
        hashmap = {}
        for i in strs:
            keys = ''.join(sorted(i))
            if keys not in hashmap:
                #这里要注意我们的键值对里面的值以列表形式存储，这样能够保证后续能够对字典进行append操作
                hashmap[keys] = [i]
            else:
                hashmap[keys].append(i)
        return list(hashmap.values())
# @lc code=end

