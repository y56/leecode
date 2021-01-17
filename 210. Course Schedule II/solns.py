"""
topological sort, dfs
"""
class Solution:
    WHITE = 1 # untouched
    GRAY = 2 # visited, not completed
    BLACK = 3 # completed
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
         # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            for neighbor in adj_list[node]:
                if color[neighbor] == Solution.WHITE:
                    dfs(neighbor)
                elif color[neighbor] == Solution.GRAY:
                     # An edge to a GRAY vertex represents a cycle
                    is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []
"""
topological sort, indegree
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []
    
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = defaultdict(int)
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] += 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = [k for k in range(numCourses) if k not in indegree]

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree:

            # Pop one node with 0 in-degree
            vertex = zero_indegree.pop()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            for neighbor in adj_list[vertex]:
                indegree[neighbor] -= 1

                # Add neighbor to Q if in-degree becomes 0
                if indegree[neighbor] == 0:
                    zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []
