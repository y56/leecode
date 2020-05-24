func intervalIntersection(A [][]int, B [][]int) [][]int {
    ans:=make([][]int,0)
    for i, j := 0, 0; i<len(A) && j<len(B); {
        lo:=max(A[i][0],B[j][0])
        hi:=min(A[i][1],B[j][1])
        if lo<=hi {
            ans=append(ans,[]int{lo,hi})
        }
        if A[i][1]<B[j][1] { // the smaller shall go to next
            i++ // if equal, doesn't matter, wolg let A go to next
        } else if A[i][1]>B[j][1] {
            j++
        } else {
            i++
            j++
        }
    }
    return ans
}
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
func min(a, b int ) int {
    if a < b {
        return a
    }
    return b
}
