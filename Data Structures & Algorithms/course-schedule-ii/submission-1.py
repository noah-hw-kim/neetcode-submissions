"""
Input: numCourses = 3, prerequisites = [[1,0]]
Output: [0,1,2]

0
1 <- 0
2

Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
Output: []

0 <- 1
1 <- 2
2 <- 0

Input: numCourses = 1, prerequisites = []
Output: [0]

constraints:
    1 <= numCourses <= 1000
    0 <= prerequisites.length <= 1000
    All prerequisite pairs are unique.

approach:
brute force (adj list) - O(V+E), O(E)

Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
Output: []

course to prerequistes
{
0:[1]
1:[2]
2:[0]
}

visited = {}
ans = [2,1,0]


0 -> 1 -> 2

Input: numCourses = 3, prerequisites = [[1,0]]
Output: [0,1,2]

{
0:[]
1:[0]
2:[]
}

visited = {}
taken = {0,1}
ans = [0,1,2]

Input: numCourses = 3, prerequisites = [[1,0], [1,2], [0,2]]
Output: [0,1,2]



"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crs_to_prereqs = {}
        for crs in range(numCourses):
            crs_to_prereqs[crs] = []

        for crs, pre in prerequisites:
            crs_to_prereqs[crs].append(pre)

        path = set()
        taken = set()
        ans = []

        def dfs(crs):
            # base
            if crs in path:
                return False
            if crs in taken:
                return True

            # iterative
            path.add(crs)
            for pre in crs_to_prereqs[crs]:
                if not dfs(pre):
                    return False
            
            taken.add(crs)
            ans.append(crs)
            path.remove(crs)

            crs_to_prereqs[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return ans




        