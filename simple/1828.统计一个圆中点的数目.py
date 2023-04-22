"""
给你一个数组points，其中points[i] = [xi, yi] ，表示第 i 个点在二维平面上的坐标。多个点可能会有 相同 的坐标。

同时给你一个数组 queries ，其中 queries[j] = [xj, yj, rj] ，表示一个圆心在 (xj, yj) 且半径为 rj 的圆。

对于每一个查询 queries[j] ，计算在第 j 个圆 内 点的数目。如果一个点在圆的 边界上 ，我们同样认为它在圆 内 。

请你返回一个数组 answer ，其中 answer[j]是第 j 个查询的答案

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/queries-on-number-of-points-inside-a-circle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for querie in queries:
            count = 0
            for point in points:
                if (pow(point[0] - querie[0], 2) + pow(point[1] - querie[1], 2)) <= pow(querie[2], 2):
                    count += 1
            res.append(count)
        return res



# sol = Solution()
# points = eval(input())
# queries = eval(input())
# sol.countPoints(points, queries)
