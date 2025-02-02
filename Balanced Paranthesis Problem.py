# Time Complexity: O(n) Auxiliary Space: O(n) for stack
from collections import deque

def check_pair(val1,val2):
    return (val1 == '(' and val2 == ')') or (val1 == '[' and val2 == ']') or (val1 == '{' and val2 == '}')


def check_balanced(expr):
    stack = deque()

    for i in range(len(expr)):
        if expr[i] == '(' or expr[i] == '[' or expr[i] == '{':
            stack.append(expr[i])
        else:
            if len(stack) == 0:
                return False
            elif check_pair(stack[-1], expr[i]):
                stack.pop()
                continue

            return False

    return True


# driver code
expr = "({})[]"

if check_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")