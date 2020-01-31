# 4. Median of Two Sorted Arrays
## solution
array A; len(A) is m; length for left_A is i; left_A index 0 ~ i-1  
array B; len(B) is n; length for left_B is j; left_B index 0 ~ j-1  

For m+n is even. half_len = (m+n)/2; have to take average as median;  
ave of max(A[i-1], B[j-1]) and min(A[i], B[j]); if i!=0 and j!=0  

For m+n is odd. half_len = (m+n)//2+1; total_left_length = total_right_length +1;  
median is max(A[i-1], B[j-1]); if i!=0 and j!=0  

to include both even and odd, half_len = (m+n+1)//2; which is ceil((m+n)/2))  

wolg, let n >= m,  

length j = ceil((m+n)/2)) - i = ceil((m + n - 2i) / 2) <= ceil((m + n - 2m) / 2)  

length i is in 0~m, when i is max as m, j is (n - m)/2, still >= 0, safe.  

so, it is safe to let len i in 0~m  

if it is n >= m, and we let j in 0~n,   
when j as n, all array B is at left-hand-side, even putting puttinf all array A on the right-hand-side is insufficient to counter that.  

```
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # wolg, let n >= m, len(B) >= len(A);
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)
        if not (n >= m):
            A, B, m, n = B, A, n, m
        
        # Let left_half_len - right_half_len be 0 for m+n even 
        # or 1 for m+n odd
        left_half_len = (m + n + 1) // 2 
        
        # i is len fo left part of A
        i_lower_b, i_higher_b = 0, m
        print('m', m)
        while i_lower_b <= i_higher_b:
            print('i_lower_b',i_lower_b,'i_higher_b',i_higher_b)
            i_try = (i_lower_b + i_higher_b) // 2
            j_try = left_half_len - i_try
            if i_try > 0 and A[i_try-1] > B[j_try]: 
            # don't have to check A[i_try] >= B[j_try-1]:
                i_higher_b = i_try - 1 
                # A moves right, ie, i_try goes down; 
                # if i_try is already 0, we can't go down
            elif i_try < m and A[i_try] < B[j_try-1]: 
            # don' have to check A[i_try-1] <= B[j_try]
                i_lower_b = i_try + 1
                # A moves left, ie, i_try goes up; 
                # if i_try is already m, we can't go 
            else: # i_try is perfect
                i = i_try
                j = j_try
                print('A',A, 'B',B)
                print('i',i,'j',j)
                # i might be 0
                if i == 0: # A as the short is all in RHS
                    # search in B's LHS for max
                    left_max = B[j-1]
                    # can't be i=0 and j=0
                elif j == 0: # B (the longer) is all in RHS
                    # avoid j-1 out of range
                    left_max = A[i-1]
                else:
                    left_max = max(A[i-1],B[j-1])
                
                if (m + n) % 2 == 1:
                    return float(left_max)
                
                if i == m: # A is all in LHS
                    right_min = B[j]
                elif j == n: # B is all in LHS
                    right_min = A[i]
                else:
                    right_min = min(A[i],B[j])
                
                print('left_max', left_max, 'right_min', right_min)
                return (left_max + right_min) / 2.0
```
