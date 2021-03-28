class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove=[]
        index_stack=[]
        for i,x in enumerate(s):
            if x not in "()":
                continue
            if x=="(":
                index_stack.append(i)
            elif index_stack:
                index_stack.pop()
            else:
                to_remove.append(i)
        my_set=set(to_remove+index_stack)
        ans=''
        for i,x in enumerate(s):
            if i not in my_set:
                ans+=x
        return ans
    
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove=set()
        index_stack=[]
        for i,x in enumerate(s):
            if x not in "()":
                continue
            if x=="(":
                index_stack.append(i)
            elif index_stack:
                index_stack.pop()
            else:
                to_remove.add(i)
        to_remove.update(set(index_stack))
        return ''.join([x for i,x in enumerate(s) if i not in to_remove])

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def delete_bad_para_one_way(s, opening):
            numof_open=0
            res=''
            for i,x in enumerate(s):
                if x==opening:
                    numof_open+=1
                elif x in "()":  # the closing
                    if numof_open==0:
                        continue
                    numof_open-=1
                #else: # is abc
                res+=x
            return res
        s=delete_bad_para_one_way(s,"(")
        s=delete_bad_para_one_way(s[::-1],")")
        return s[::-1]
        
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        numof_open=0
        tot_open=0
        tmp=[]
        for i,x in enumerate(s):
            if x=="(":
                numof_open+=1
                tot_open+=1
            elif x==")":  # the closing
                if numof_open==0:
                    continue
                numof_open-=1
            #else: # is abc
            tmp.append(x)
        open_to_keep=tot_open-numof_open
        res=[]
        for x in tmp:
            if x=="(":
                if open_to_keep==0:
                    continue
                else:
                    open_to_keep-=1
            res.append(x)
        return ''.join(res)

