"""
204. Count Primes
Easy

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

"""
Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Wheel factorization
https://en.wikipedia.org/wiki/Wheel_factorization

Mertens' theorems
https://en.wikipedia.org/wiki/Mertens%27_theorems

Prime number theorem
https://en.wikipedia.org/wiki/Prime_number_theorem

Sieve of Eratosthenes geek4geek
https://www.geeksforgeeks.org/sieve-of-eratosthenes/

Time complexity of an algorithm to find prime numbers
https://stackoverflow.com/questions/25151024/time-complexity-of-an-algorithm-to-find-prime-numbers

Sieve of Atkin, O(n) time
https://en.wikipedia.org/wiki/Sieve_of_Atkin

What is the sum of the prime numbers up to a prime number n ? 
https://math.stackexchange.com/questions/623872/what-is-the-sum-of-the-prime-numbers-up-to-a-prime-number-n
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
        is_prime=[True]*n
        is_prime[0]=False
        is_prime[1]=False
        for i in range(2,n):
            j=2
            while i*j<n:
                is_prime[i*j]=False
                j+=1
        return sum(is_prime)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
        is_prime=[True]*n
        is_prime[0]=False
        is_prime[1]=False
        for i in range(2,n):
            j=2
            while is_prime[i] and i*j<n: # if this is not a prime, its multiples are already checked
                is_prime[i*j]=False
                j+=1
        return sum(is_prime)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
        is_prime=[True]*n
        is_prime[0]=False
        is_prime[1]=False
        for i in range(2,n):
            j=i # start from itself, not from 2
            while is_prime[i] and i*j<n:
                is_prime[i*j]=False
                j+=1
        return sum(is_prime)
"""
O( n lg lg n ) time
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
        is_prime=[True]*n
        is_prime[0]=False
        is_prime[1]=False
        for i in range(2,int(n**0.5)+1): # from 2 to floor(n**0.5)
            j=i
            while is_prime[i] and i*j<n: # while check extra is_prime[i]
                is_prime[i*j]=False
                j+=1
        return sum(is_prime)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
        is_prime=[True]*n
        is_prime[0]=False
        is_prime[1]=False
        for i in range(2,int(n**0.5)+1):
            j=i
            if is_prime[i]: # not go to while if no need
                while i*j<n:
                    is_prime[i*j]=False
                    j+=1
        return sum(is_prime)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
        is_prime=[True]*n
        is_prime[0]=False
        is_prime[1]=False
        for i in range(2,int(n**0.5)+1): 
            if is_prime[i]:
                is_prime[i*i::i]=[False]*len(is_prime[i*i::i]) # this is much faster the while # time improve from 59%/860ms to 80%/260ms
        return sum(is_prime)
"""
wheel factorization
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
        is_prime=[True]*n
        is_prime[0]=False
        is_prime[1]=False
        #  wheel 
        is_prime[4::2]=[False]*len(is_prime[4::2])
        is_prime[9::3]=[False]*len(is_prime[9::3])
        is_prime[25::5]=[False]*len(is_prime[25::5])
        is_prime[49::7]=[False]*len(is_prime[49::7])
        is_prime[121::11]=[False]*len(is_prime[121::11])
        for i in range(3,int(n**0.5)+1,2): # only loop on odd num
            if is_prime[i]:
                is_prime[i*i::i]=[False]*len(is_prime[i*i::i])
        return sum(is_prime)
