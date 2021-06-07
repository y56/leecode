class Solution:
    def minFlips(self, s: str) -> int:
        odd1=sum(x=='1' for x in s[1::2])
        odd0=sum(x=='0' for x in s[1::2])
        even1=sum(x=='1' for x in s[0::2])
        even0=sum(x=='0' for x in s[0::2])
        if len(s)%2==0: 
        # For even len(s), rotation leads to only two choices bc of symmetry
            a=even1+odd0 # num of flips to become 01...01
            b=even0+odd1 # num of flips to become 10...10
            return min(a,b)
        else:
            ans=inf
            for x in s: # need to try every rotation for odd len(s)

                # counts changing bc of rotation
                if x=='1':  # if we are move an '1' from head to tial
                    even1-=1
                    odd1+=1
                else:  # if we are move a '0' from head to tial
                    even0-=1
                    odd0+=1

                # even/odd exchanges bc of rotation
                odd1, odd0, even1, even0 \
                = \
                even1, even0, odd1, odd0

                a=even1+odd0 # num of flips to become 01...010
                b=even0+odd1 # num of flips to become 10...101
                ans=min(ans, min(a,b) )
            return ans

