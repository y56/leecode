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
