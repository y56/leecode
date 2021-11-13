https://leetcode.com/problems/arithmetic-subarrays/discuss/909120/python3-using-set-no-sort-O(MN)

Find the min and max of each subarray, create a set of the subarray, compute the difference between two numbers (difference = (max - min)//(len -1)), check if each number is in the set, worse case time O(len(nums)* len(r)). example : [1, 3, 2, 4, 5], min = 1, max = 5, diff = (5-1)/4, check if each number is in set, starting from min, min + diff, min + diff x 2, min + diff x 3, .... ....

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArith(n):
            mx, mn, st = max(n), min(n), set(n)
            if (mx - mn)%(len(n)-1) != 0: return False
            step = (mx - mn)//(len(n)-1)
            if not step: return mx == mn
            for i in range(mn, mx, step):
                if i not in st:
                    return False
            return True
        res = []
        for i in range(len(l)):
            res.append(isArith(nums[l[i]:r[i]+1]))
        return res

@10292020 updated based on ioakeimo's suggestion.

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArith(n):
            st = set(n)
            if len(n) != len(st): return len(st) == 1 # take care of duplicates
            mx, mn, = max(n), min(n)
            if (mx - mn)%(len(n)-1) != 0: return False
            step = (mx - mn)//(len(n)-1)
            for i in range(mn, mx, step):
                if i not in st:
                    return False
            return True

        return [isArith(nums[start:stop+1]) for start, stop in zip(l,r)]

