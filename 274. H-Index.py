class _Solution:
    def hIndex(self, citations: List[int]) -> int:
        # the n-th paper has citations[n] citations
        N=len(citations)
        citations.sort()
        for e in citations:
            if e>=N:
                return N
            N-=1
        return 0
"""
rom Approach #1, we sort the citations to find the h-index. However, it is well known that comparison sorting algorithms such as heapsort, mergesort and quicksort have a lower bound of O(nlog⁡n)O(n\log n)O(nlogn). The most commonly used non-comparison sorting is counting sort.

    Counting sort operates by counting the number of objects that have each distinct key value, and using arithmetic on those tallies to determine the positions of each key value in the output sequence. Its running time is linear in the number of items and the difference between the maximum and minimum keys, so it is only suitable for direct use in situations where the variation in keys is not significantly greater than the number of items.

    ---by Wikipedia

However, in our problem, the keys are the citations of each paper which can be much larger than the number of papers nnn. It seems that we cannot use counting sort. The trick here is the following observation:

    Any citation larger than nnn can be replaced by nnn and the hhh-index will not change after the replacement

The reason is that hhh-index is upper bounded by total number of papers nnn, i.e.

h≤n h \leq n h≤n
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N=len(citations) # total num of papers
        papers=[0]*(N+1) # buckets for counting sort
        # number of papers w/ m citations is papers[m]
        for c in citations: # couting sort
            papers[min(c,N)]+=1 # for c > N, we count them as N
        k=N
        numof_papers_w_more_than_k_citations=0
        for numof_papers in papers[::-1]:
            numof_papers_w_more_than_k_citations+=numof_papers
            if numof_papers_w_more_than_k_citations>=k:
                return k
            k-=1
        
