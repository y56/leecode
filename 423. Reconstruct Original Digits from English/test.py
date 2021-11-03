class Solution:
    def originalDigits(self, s: str) -> str:
#         w is unique for: two   
#         u is unique for: four
#         x is unique for: six
#         g is unique for: eight
#         z is unique for: zero
#    then
#         f is unique for: five
#    then
#         i is unique for: nine
#    then
#         o is unique for: one
#    then
#         t/h/r unique for: three
#    then
#         seven
        numof=[0]*10
        c=collections.Counter(s)
        numof[2]=c['w']
        c['t']-=c['w']
        c['o']-=c['w']

        numof[4]=c['u']
        c['f']-=c['u']
        c['o']-=c['u']
        c['r']-=c['u']

        numof[6]=c['x']
        c['s']-=c['x']
        c['i']-=c['x']

        numof[8]=c['g']
        c['e']-=c['g']
        c['i']-=c['g']
        c['h']-=c['g']
        c['t']-=c['g']

        numof[0]=c['z']
        c['e']-=c['z']
        c['r']-=c['z']
        c['o']-=c['z']

        numof[5]=c['f']
        c['i']-=c['f']
        c['v']-=c['f']
        c['e']-=c['f']

        numof[9]=c['i']
        c['n']-=c['i']*2
        c['e']-=c['i']

        numof[1]=c['o']
        c['n']-=c['o']
        c['e']-=c['o']

        numof[7]=c['v']

        numof[3]=c['t']

        return ''.join([str(i)*x for i,x in enumerate(numof)])

# TODO: backtracking

