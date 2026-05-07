class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        


        def fact(n):
            prod = 1
            for i in range(1,n + 1):
                prod *= i 

            return prod

        numer = fact( m + n - 2)
        denom = fact(m -1) * fact(n - 1)

        return numer // denom

        