# 题目：给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 思路：最简单就是所有子序列算一次sum，然后比较，但很费时间
# 局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。

# 解法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 使用count实时记录子序列和，当其小于0时就要归零重新开始计。
        count = 0
        result = -float('INF')  # 考虑有负数情况
        for i in range(len(nums)):
            count += nums[i]
            # 实时更新result
            if count > result:
                result = count
            # 实时判断count情况
            if count <= 0:
                count = 0
                
        return result