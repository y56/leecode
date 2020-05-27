func _minMeetingRooms(intervals [][]int) int {
    start := make([]int,len(intervals))
    end := make([]int,len(intervals))
    for i, val := range intervals {
        start[i] = val[0]
        end[i] = val[1]
    }
    sort.Ints(start)
    sort.Ints(end)
    i := 0
    ans := 0
    for _,val := range(start) {
        if val < end[i] {
            ans++
        } else {
            i++
        }
    }
    return ans
}
/*==============================================================*/
type IntHeap []int
func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func minMeetingRooms(intervals [][]int) int {
    if intervals == nil || len(intervals) == 0 {
        return 0
    }
    sort.Slice(intervals, func(i, j int) bool {
        if intervals[i][0] < intervals[j][0] {
            return true
        }   
        return false
    })
    h := &IntHeap{}
    heap.Init(h)
    for _, interval := range intervals {
        currentStartTime := interval[0]
        currentEndTime := interval[1]
        if h.Len() != 0 && (*h)[0] <= currentStartTime{
            _ = heap.Pop(h).(int)
        }
        heap.Push(h, currentEndTime)
    }
    
    return h.Len()
}
