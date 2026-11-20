"""
mistake
- thought this is a same problem as Number of Connected Components in an Undirected Graph

what is a tree?
- connected
- no cycle
- no self loop or repeated edges

base case:
- if len(edges) < n - 1: return False. Not all connected

approach:
1. base is similar to union and find
2. how do we know if all nodes are connected? -> 
1) we start with the number of comp = n.
2) do union and find
3.1) if found same root/parent -> return False. Cycle!
3.2) else decrement number of comp by 1
4) After all union, we return True if the number of comp is only 1. else, there's not connected part

or we don't need to track of number of comp and use base case

"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if len(edges) < n - 1:
        #     return False

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
            if not union(n1, n2):
                return False
            ans -= 1
        
        return True if ans == 1 else False