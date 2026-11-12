"""
Input: adjList = [[2],[1,3],[2]]
Output: [[2],[1,3],[2]]

node 1 -> node 2

node 2 -> node 1
node 2 -> node 3

node 3 -> node 2

0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.
graph is connected with undirected edges -> one node, we can traverse any

node 1
val = 1
neighbors = [node2]

node 2

1) which node is already visited
2) get next traverse node
3) deep copy

approach brute force bfs - O(node*edge), O(n)
node 1 -> node 2
node 2 -> node 1

node 2 -> node 3
node 3 -> node 2

traverse_list = 
visited = {node 1}
q = []

somehow connect node 1 with node 2

org_to_new
{node1:node1_new
node2:node2_new
}

1 -> 1 (neighbor = new 2)
2 -> 2 (neightbor = new 1)

1) how to prevent to double adding? does visited set works as we have a undirected relationship
does checking if it's in a map?

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        org_to_new = {node:Node(node.val)}
        q = deque()
        q.append(node)

        while q:
            n = q.popleft()

            for neighbor in n.neighbors:
                if neighbor not in org_to_new:
                    org_to_new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                org_to_new[n].neighbors.append(org_to_new[neighbor])


        
        return org_to_new[node]






