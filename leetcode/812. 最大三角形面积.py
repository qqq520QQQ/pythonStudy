class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        len_len = len(points)
        res = []
        for i in range(len_len - 2):
            for j in range(i + 1, len_len - 1):
                for k in range(j + 1, len_len):
                    print(points[i], points[j], points[k])
                    s = points[i][0]*(points[j][1]-points[k][1])+\
                        points[j][0]*(points[k][1]-points[i][1])+\
                        points[k][0]*(points[i][1]-points[j][1])
                    res.append(abs(s/2))
        print(res)
        print(max(res))
        return max(res)
points = [[4,6],[6,5],[3,1]]
ss = Solution()
ss.largestTriangleArea(points)