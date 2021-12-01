class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)

        for u, v in edges:
            if self.find(u, parent) == self.find(v, parent):
                return [u, v]
            self.union(u, v, parent, size)

    def union(self, u, v, parent, size):
        root_u, root_v = map(self.find, (u, v), (parent, parent))
        small, big = sorted([root_u, root_v], key=lambda x: size[x])
        parent[small] = big
        size[big] += size[small]

        return

    def find(self, node, parent):
        if node == parent[node]:
            return node
        parent[node] = self.find(parent[node], parent)

        return parent[node]
