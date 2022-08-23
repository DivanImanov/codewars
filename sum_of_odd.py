# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064

def row_sum_odd_numbers(n):
    odd_numbers = list(range(1, sum(range(n+1))*2, 2))
    return sum(odd_numbers[-el] for el in range(1, n + 1))
