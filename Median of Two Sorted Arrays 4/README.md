# 4. Median of Two Sorted Arrays
## 
array A; len(A) is m; index for A is i
array B; len(B) is n; index for B is j

Let consider the case where m+n is even.

half_len = (m+n)/2

left part of A, index 0~(i-1), i items
left part of B, index 0~(j-1), j items

for length, i + j = (m+n)/2

wolg, let n >= m,

length j = (m + n)/2 - i = (m + n - 2i)/2 = 

length i is in 0~m, when i is m, j is (n - m)/2, >= 0, safe.

