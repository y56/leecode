func _frequencySort(s string) string {
	m := make(map[rune]int)
	for _,val := range s {
        m[val]++ // s[i] is byte // val by range is rune
	}
	buckets := make([][]rune, len(s)+1)
	for char, count  := range m {
        buckets[count] = append(buckets[count],char)
	}
	result := make([]rune, 0, len(s))
	for i := len(buckets) - 1; i >= 0; i-- {
		chars := buckets[i]
        if len(chars) == 0 { // use len(.)==0 to check empty
			continue
		}
        for _,char := range chars {
            for ii := 0; ii < i; ii++ {
                result = append(result, char)                   
            }
		}
	}
    return string(result)
}
/*=========================================================*/
func frequencySort(s string) string {
	m := make(map[byte]int)
	for i := range s {
        m[s[i]]++ // s[i] is byte // val by range is rune
	}
	buckets := make([][]byte, len(s)+1)
	for char, count  := range m {
        buckets[count] = append(buckets[count],char)
	}
	result := make([]byte, 0, len(s))
	for i := len(buckets) - 1; i >= 0; i-- {
		chars := buckets[i]
        if len(chars) == 0 { // use len(.)==0 to check empty
			continue
		}
        for _,char := range chars {
            for ii := 0; ii < i; ii++ {
                result = append(result, char)                   
            }
		}
	}
    return string(result)
}
