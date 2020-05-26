func _findMaxLength(nums []int) int {
    ans := 0
    L := len(nums)
    count := 0 // #ones - #zeros so far
    // Its range is: -len(nums) <= count <= len(nums)
    
    table := make([]int, L * 2 + 1) 
    // table[count + len(nums)] is the left-most index when `count` occurs
    
    unvisited := L + 1 // This is a value can't be reach by `count`
    offset := L
    
    for i, _ := range table {
        table[i] = unvisited // this value imply un-visited
    }
    
    table[0 + offset] = -1 
    
    for i, e := range nums {
        if e==1 {
            count += 1
        } else {
            count -= 1
        }
        if table[count + offset] == unvisited {
            table[count + offset] = i
        } else {
            if (i - table[count + offset]) > ans {
                ans = i - table[count + offset]
            }
        }
    }
    return ans
}

func findMaxLength(nums []int) int {
    ans := 0
    table := make(map[int]int)
    count := 0 // #ones - #zeros so far
    // Its range is: -len(nums) <= count <= len(nums)
    
    table[0] = -1
    
    for i, e := range nums {
        if e==1 {
            count += 1
        } else {
            count -= 1
        }
        if _, ok := table[count]; !ok {
            table[count] = i
        } else {
            if (i - table[count]) > ans {
                ans = i - table[count]
            }
        }
    }
    return ans
}
