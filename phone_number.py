# https://www.codewars.com/kata/525f47c79f2f25a4db000025

import re
def valid_phone_number(phone_number):
    return bool(re.match('^\(\d{3}\) \d{3}-\d{4}$', phone_number))

# Решение без re

def valid_phone_number_2(phone_number):
    n = [str(x) for x in range(10)]
    sample = ['(', n, n, n, ')', ' ', n, n, n, '-', n, n, n, n]
    if len(sample) != len(phone_number):
        return False
    for el in range(len(sample)):
        if phone_number[el] not in sample[el]:
            return False 
    return True