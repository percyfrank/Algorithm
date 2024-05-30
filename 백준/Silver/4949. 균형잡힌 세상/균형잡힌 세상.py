import sys

while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break

    stack = []
    flag = True
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break

    print("yes") if not stack and flag else print("no")