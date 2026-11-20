"""
Input:
n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

0 - 1 - 2
3 - 4

Input:
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

0 - 1 - 2 - 3 - 4

Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= aᵢ < n -> node in range
0 <= bᵢ < n -> node in range
aᵢ != bᵢ -> no self loop
There are no repeated edges.

approach
Input:
n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

compo = 2

0 - 1 - 2
3 - 4

1. start with n
2. construct graph with edge in edges
3. decrement compo by 1 every time

problem!
n = 5, edges = [[0,1],[1,2],[0,2],[3,4]]
Output: 2

0 - 1 - 2
|-------|
3 - 4
-> we can't blindly decrement compo by 1
-> need to check if both edges are already connected or not

=> we need to find if both nodes are connected?
=> if not connected, we merge them and compo -= 1
=> else (connected), we don't do anything
=> disjoint union - O(V + E), O(V + E)

parent = [0,0,0,3,4]
rank = [3,1,1,2,1]

count = 2
p1 = 3
p2 = 4

0 - 1
| - 2

3 - 4




"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):
            cur = node
            while cur != parent[cur]:
                cur = parent[cur]

            return cur

        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)

            if p1 == p2:
                return False

            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        ans = n
        
        for n1, n2 in edges:
            if union(n1, n2):
                ans -= 1
        
        return ans

        