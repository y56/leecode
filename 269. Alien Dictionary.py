"""
BFS
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        G=collections.defaultdict(set) # Graph
        in_degree={c:0 for word in words for c in word }
        for former_word,latter_word in zip(words,words[1:]):
            for c,d in zip(former_word,latter_word):
                if c!=d:
                    if d not in G[c]:
                        G[c].add(d) # c < d
                        in_degree[d]+=1
                    break
            else:
                # e.g., 
                if len(former_word)>len(latter_word):
                    return ""
                
        ans=[]
        q=collections.deque([c for c in in_degree if in_degree[c]==0])
        while q:
            c=q.popleft()
            ans.append(c)
            for d in G[c]: # c < d
                in_degree[d]-=1
                if in_degree[d]==0:
                    q.append(d)
        if len(ans) < len(in_degree):
            return ""   
        return ''.join(ans)
"""
DFS
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        reversed_adj_list = {c : [] for word in words for c in word}
        
        for first_word, second_word in zip(words,words[1::]):
            for c,d in zip(first_word,second_word):
                if c!=d:
                    reversed_adj_list[d].append(c) #  c < d
                    break
            else:
                if len(first_word)>len(second_word):
                    return ''
                
        seen={} # once and twice
        ans=[]
        def dfs(node):
            if node in seen:
                if seen[node]=="grey":
                    return False # we detect a loop
                else: # black
                    return True
            seen[node]="grey"
            for next_node in reversed_adj_list[node]:
                # all next_node < node
                if dfs(next_node)==False: # we detect a loop
                    return False
            seen[node]="black"
            ans.append(node)
            return True
        
        if not all(dfs(node) for node in reversed_adj_list):
            return ''
        return ''.join(ans)
