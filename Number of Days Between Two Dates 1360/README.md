# 1360. Number of Days Between Two Dates
```python=
# from datetime import date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
    
        # d1 = date(int(date1[0:4]), int(date1[5:7]), int(date1[8:10]))
        # d2 = date(int(date2[0:4]), int(date2[5:7]), int(date2[8:10]))
        # delta = d2 - d1
        # return abs(delta.days)

# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year) 
        def monthday(y):
            if y%4!=0: # not by 4
                return [0,31,28,31,30,31,30,31,31,30,31,30,31] # common
            # by 4
            elif y%100!=0:
                return [0,31,29,31,30,31,30,31,31,30,31,30,31] # leap
            elif y%400!=0:
                return [0,31,28,31,30,31,30,31,31,30,31,30,31] # common
            else:
                return [0,31,29,31,30,31,30,31,31,30,31,30,31] # leap

        def betweeen_year(y_old,y_new): # include left and right endpoints
            return sum([sum(monthday(y)) for y in range(y_old,y_new+1)])

        def betweeen_month(m_old, m_new,y): # include left and right endpoints
            return sum(monthday(y)[m_old:m_new+1])
        
        def til_end_of_month(y,m,d):
            return monthday(y)[m] - d + 1
                
        def til_end_of_year(y,m,d):
            return til_end_of_month(y,m,d) + betweeen_month(m+1, 12, y)
        
        def start_of_year_til_theday(y,m,d):
            return betweeen_month(1, m-1, y) + d     
        
        
        
        y1 = int(date1[0:4]) 
        m1 = int(date1[5:7])
        d1 = int(date1[8:10])
        
        y2 = int(date2[0:4]) 
        m2 = int(date2[5:7])
        d2 = int(date2[8:10])
        
        # maitain date2 > date1
        if y1 > y2:
            date1,date2=date2,date1
        elif y1 == y2:
            if m1 > m2:
                date1,date2=date2,date1
            elif m1 == m2:
                if d1 > d2:
                    date1,date2=date2,date1
                    
        y1 = int(date1[0:4]) 
        m1 = int(date1[5:7])
        d1 = int(date1[8:10])
        
        y2 = int(date2[0:4]) 
        m2 = int(date2[5:7])
        d2 = int(date2[8:10])
        
        if y2 > y1:
            return til_end_of_year(y1,m1,d1) + betweeen_year(y1+1,y2-1) + start_of_year_til_theday(y2,m2,d2) - 1
        else:
            if m2 > m1: # under y1==y2
                return til_end_of_month(y1,m1,d1) + betweeen_month(m1+1, m2-1, y1) + d2 - 1
            else:
                return d2 - d1
```
