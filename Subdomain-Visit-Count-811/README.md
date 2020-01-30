# 811. Subdomain Visit Count

## me 1
```python=
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
        
```
## me 2
```python=
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict_ = {}
        for item in cpdomains:
            count, domain_str = item.split(' ')
            domain_list = domain_str.split('.')
            
            key = domain_list[-1]  # highest domain name
            if key not in dict_:
                dict_[key] = 0
            dict_[key] += int(count)
            
            for ele in domain_list[-2::-1]:
                key = ele + '.' + key
                if key not in dict_:
                    dict_[key] = 0
                dict_[key] += int(count)

        res = []
        for key in dict_:
            res.append(str(dict_[key])+' '+key)
        
        return res
```
