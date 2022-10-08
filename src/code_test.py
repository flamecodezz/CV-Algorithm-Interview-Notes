class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals) -> int:
        # Write your code here
        begin = [0] * len(intervals)  # 保存起点, 红点表示
        end = [0] * len(intervals)    # 保存终点，蓝点表示

        for i in range(len(intervals)):
            begin[i] = intervals[i][0]
            end[i] = intervals[i][1]
        begin.sort() # 排序
        end.sort()

        i, j = 0, 0
        count = 0   # 计数
        res = 0     # 保存结果
       
       # 使用双指针扫描，有点不好理解
       # 如果用一个数组装所有点，那么就失去标志位了，所以还是分开装，至于怎么怎么理解这个双指针
       # 谁在左边，就扫描到谁，所以用一个if判断
        while i < len(begin) and j < len(end):
            # 遇到红点，count加一，i移动一位
            if begin[i] < end[j]:
                count += 1
                i += 1
            # 遇到蓝点，count减一，j移动一位
            else:
                count -= 1
                j += 1
            # 记录扫描过程中的最大值
            res = max(res, count)
        return res
    
if __name__ == '__main__':
    intervals = [(0,30),(5,10),(15,20)]
    soulution = Solution()
    ans = soulution.min_meeting_rooms(intervals)
    print(ans)



        

