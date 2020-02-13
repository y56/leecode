###### tags: `leetcode`

# 76. Minimum Window Substring

## Counter()
```python=
def minWindow(self, s: str, t: str) -> str:
    t_count = collections.Counter(t)
    window_count = {}  
    l, r = 0, 0
    num_of_hits = 0
    ans = (float("inf"), None, None)
    while r < len(s):
        window_count[s[r]] = window_count.get(s[r], 0) + 1
        if window_count[s[r]] <= t_count[s[r]]: 
        # not exceeding, still useful conts
            num_of_hits += 1

        # num_of_hits is enough, record a candidate and try to shrink size
        while l <= r and num_of_hits == len(t):
            if r - l + 1 < ans[0]: 
                ans = (r - l + 1, l, r)
            window_count[s[l]] -= 1
            if window_count[s[l]] < t_count[s[l]]: 
            # num_of_hits is reduced only if we have less than `t`
                num_of_hits -= 1
            l += 1  
        r += 1
    if ans[0] == float("inf"):
        return ''
    return s[ans[1]:ans[2]+1]
```
## filtering
```python=
def minWindow(self, s: str, t: str) -> str:
    t_count = collections.Counter(t)
    filtered_s = []
    for i_ele in enumerate(s): 
        if i_ele[1] in t_count:
            filtered_s.append((i_ele))
    window_count = {}  
    l_filtered_s, r_filtered_s = 0, 0
    num_of_hits = 0
    ans = (float("inf"), None, None)
    while r_filtered_s < len(filtered_s):
        ch = filtered_s[r_filtered_s][1]
        window_count[ch] = window_count.get(ch, 0) + 1
        if window_count[ch] <= t_count[ch]: 
        # not exceeding, still useful conts
            num_of_hits += 1

        # num_of_hits is enough, record a candidate and try to shrink size
        while l_filtered_s <= r_filtered_s and num_of_hits == len(t):
            ch = filtered_s[l_filtered_s][1]
            l_s = filtered_s[l_filtered_s][0]
            r_s = filtered_s[r_filtered_s][0]
            if r_s - l_s + 1 < ans[0]: 
                ans = ( r_s - l_s + 1, l_s, r_s)
            window_count[ch] -= 1
            if window_count[ch] < t_count[ch]: 
            # num_of_hits is reduced only if we have less than `t`
                num_of_hits -= 1
            l_filtered_s += 1  
        r_filtered_s += 1
    if ans[0] == float("inf"):
        return ''
    return s[ans[1]:ans[2]+1]
```
