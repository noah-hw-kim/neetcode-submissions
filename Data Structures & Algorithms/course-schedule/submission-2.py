"""
Input: numCourses = 2, prerequisites = [[0,1]]
Output: true

0 <- 1

Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
Output: false

1 -> 0
0 -> 1

* if there's a bidirection relationship. Then we can't complete the courses

Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
Output: false

1 -> 0
2 -> 1
0 -> 2

{0:[1]
1:[2]
2:[0]}

visited = {0,1,2}

what if
{0:[1,2]
1:[2]
2:[]}

visited = {0,1,2}

* if there's a cycle, then we can't complete

constraints (very important):
    1 <= numCourses <= 1000
    0 <= prerequisites.length <= 1000
    prerequisites[i].length == 2
    0 <= a[i], b[i] < numCourses
    All prerequisite pairs are unique.

approach:
brute force - t=O(V+E), s=O(V+E)
1. create a graph (adj list)
2. explore from 0, 1, ..., and see if there's a cycle -> return False
3. 


edge case
numCourses=5
prerequisites=[[1,4],[2,4],[3,1],[3,2]]

0:[]
1:[4]
2:[4]
3:[1,2]
4:[]

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        crs_to_pre = {}

        for i in range(numCourses):
            crs_to_pre[i] = []

        for crs, pre in prerequisites:
            crs_to_pre[crs].append(pre)

        visited = set()

        def dfs(crs):
            # base
            if crs in visited:
                return False

            # iterative
            visited.add(crs)

            for pre in crs_to_pre[crs]:
                if not dfs(pre):
                    return False
                crs_to_pre[crs] = []
            
            visited.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True



        