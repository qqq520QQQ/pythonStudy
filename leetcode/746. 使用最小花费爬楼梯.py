class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        res = 0
        tag = 0
        len_len = len(cost)
        for i in range(len_len):
            if (cost[i] > cost[i+1]) & (i == 0):
                break
            if (i == tag) & (i < len_len - 2):
                if cost[i+1] > cost[i+2]:
                    res = res + cost[i]
                    tag = i + 2
                else:
                    res = res + cost[i]
                    tag = i + 1
            elif i >= len_len - 2:
                res += cost[i]
                break
            elif i != tag:
                continue
        print(res)
cost = [10,15,20]
ss = Solution()
ss.minCostClimbingStairs(cost)