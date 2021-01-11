class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # linked list: a node is pointing to its pre
        D = collections.defaultdict(list) # adjacency list
        for a,b in prerequisites:
            # a needs b
            # b is pre
            D[a].append(b) # a pointing to b

        
        def dfs(node):
            if self.done: # a global flag to tell everybody we are done
                return
            
            if node in locally_seen: # detect a loop # we have a new `locally_seen` for each start of dfs
                self.done = True # signal everyone we are done
                return
            
            locally_seen.add(node) # record path, go deeper
            for child in D[node]: # dfs fanning out
                if (child not in D or # no further child
                    child in globally_checked): # already checked to be no loops after it 
                    continue # skip checking it
                dfs(child)
                
            # as we finish checking its childs, we remove it from the recorded path
            locally_seen.remove(node) # go upper, remove breadcrumb
            
            globally_checked.add(node) # no loops from this node

        globally_checked = set() # record globally for those nodes we checked
        locally_seen=set() # record ancestor path for each dfs
        self.done=False # a global signal to indicate "done"
        for root in range(numCourses):
            
            if root in globally_checked: # already checked to be no loops
                continue
                
             # record visited nodes in this dfs
            
            dfs(root)
            
            if self.done:
                return False
                
            
        return True # at the end, no loops detected
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # linked list: a node is pointing to its pre
        # childs = [[]]*numCourses # wrong # they will be the same list
        # collections.defaultdict(list) # ok
        childs = [[] for _ in range(numCourses)] # ok
        
        indegrees = [0]*numCourses # count incoming edges for a node
        for a,b in prerequisites:
            # a needs b # b is pre # b is a's child
            childs[a].append(b) # a pointing to b # it is ok if you let b point to a
            indegrees[b]+=1
        no_incoming=[i for i in range(numCourses) if indegrees[i]==0] # those nodes w/ no incoming edges
        removed_edges=0
        while no_incoming!=[]:
            be_checked=no_incoming.pop()
            for child in childs[be_checked]:
                indegrees[child]-=1
                removed_edges+=1
                if indegrees[child]==0:
                    no_incoming.append(child)

        return removed_edges==len(prerequisites)
        
        
