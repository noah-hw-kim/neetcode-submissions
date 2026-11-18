"""
initial
- no cycles
- n-1 edges

after
- added an edge

* return an edge that can be remove but the graph is still a connected non-cyclical

goal:
- an edge that can be removed while keep the graph connected

Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
Output: [3,4]

{1:[2,3,4]
2:[1]
3:[1,4]
4:[1,3,5]
5:[4]}

1
| | |
2 3 4

root = [1,2,3,4]
size = [1,1,1,1]

find() -> get the root of given node
union() -> merge small size node's root to the bigger size node's root

while union(), if we find two nodes' roots are same, we return false to indicate we found an answer

constraints:
    n == edges.length
    3 <= n <= 1000
    1 <= edges[i][0] < edges[i][1] <= edges.length
    There are no repeated edges and no self-loops in the input.

approach - O(V+E), O(V+E):
Union and find



"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges) + 1)]
        size = [1 for i in range(len(edges) + 1)]
        
        def find(node):
            cur = node
            while cur != root[cur]:
                cur = root[cur]
            return cur

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return False

            if size[root1] >= size[root2]:
                root[root2] = root1
                size[root1] += size[root2]
            else:
                root[root1] = root2
                size[root2] += size[root1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1,n2]

        