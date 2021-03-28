class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        st=[0]
        for s in S:
            if s=="(":
                st.append(0)
            else:
                v=st.pop()
                if v==0:
                    st[-1]+=1
                else:
                    st[-1]+=v*2
        return st[0]
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        st=[0]
        for s in S:
            if s=="(":
                st.append(0)
            else:
                v=st.pop()
                st[-1]+=1 if v==0 else v*2
        return st[0]
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        st=[0]
        for s in S:
            if s=="(":
                st.append(0)
            else:
                v=st.pop()
                st[-1]+=max(1,v*2)
        return st[0]
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        depth=0
        ans=0
        for i,x in enumerate(S):
            if x=="(":
                depth+=1
            else:
                depth-=1
                if S[i-1]=="(":
                    ans+= 1<<depth
        return ans

