# https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):
    balance = 0
    for el in string:
        if el == '(':
            balance += 1
        elif el == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0
    