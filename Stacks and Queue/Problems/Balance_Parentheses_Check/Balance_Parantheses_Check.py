
"""
Program to check for balanced Parentheses



"""
from Stacks.MyStack import MyStack


def check_Balance_Parant(str):

    # Check is even number of brackets
    if len(str) % 2 != 0:
        return False

    stack = MyStack()

    for s in str:

        if s == '{' or s == '[' or s == '(':
            stack.push(s)
        else:

            if s == ')' and stack.peek() == '(':
                stack.pop()
            elif s == '}' and stack.peek() == '{':
                stack.pop()
            elif s == ']' and stack.peek() == '[':
                stack.pop()
            else:
                stack.push(s)

    if stack.isEmpty():
        return True
    else:
        return False


print(check_Balance_Parant('[](){([[[]]])}('))
print(check_Balance_Parant('[{{{(())}}}]((()))'))
print(check_Balance_Parant('[[[]])]'))
print(check_Balance_Parant('[[[]])'))
#print(check_Balance_Parant('[]]['))