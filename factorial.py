# Factorial of a Number

class Solution:
    def factorial(self, n):
        fac = 1
        for i in range(1, n + 1):
            fac *= i
        return fac
