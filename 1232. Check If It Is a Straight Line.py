class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def f(pre_x,pre_y,x,y):
            if pre_x==x:
                return float("inf")
            return (y-pre_y)/(x-pre_x)
        
        first_slope=None
        pre_x=coordinates[0][0]
        pre_y=coordinates[0][1]
        for x,y in coordinates[1:]:
            if first_slope==None:
                first_slope=f(pre_x,pre_y,x,y)
            else:
                if first_slope!=f(pre_x,pre_y,x,y):
                    return False
            pre_x,pre_y=x,y
        return True
"""
try not to use float("inf")
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def f(pre_x,pre_y,x,y):
            return (y-pre_y)/(x-pre_x)
        first_is_verticle=None
        first_slope=None
        pre_x=coordinates[0][0]
        pre_y=coordinates[0][1]
        for x,y in coordinates[1:]:
            if first_slope==None and first_is_verticle==None:
                if pre_x==x:
                    first_is_verticle=True
                else:
                    first_slope=f(pre_x,pre_y,x,y)
            else:
                if pre_x==x:
                    if first_is_verticle!=True:
                        return False
                else:
                    if first_slope!=f(pre_x,pre_y,x,y):
                        return False
            pre_x,pre_y=x,y
        return True
"""
Don't compute slope. Compute cross product. It is 0 when parallel and has no INF.
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates)==2:
            return True
        
        def cross_product(vec_1,vec_2):
            return vec_1[0]*vec_2[1]-vec_1[1]*vec_2[0]
        
        pre_vec=(coordinates[1][0]-coordinates[0][0],
                 coordinates[1][1]-coordinates[0][1])
        pre_x=coordinates[1][0]
        pre_y=coordinates[1][1]
        for x,y in coordinates[2:]:
            vec=(x-pre_x,y-pre_y)
            if cross_product(vec,pre_vec)!=0:
                return False
            pre_vec=vec
            pre_x=x
            pre_y=y
        return True
