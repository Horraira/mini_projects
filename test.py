def validParentheses(str):
    stack = []
    for foo in str:
        if foo == '(' or foo == '{' or foo == '[':
            stack.append(foo)
        else:
            if not stack:
                return False
            else:
                top = stack[-1]
                if top == '(' and foo == ')' \
                        or top == '{' and foo == '}' \
                        or top == '[' and foo == ']':
                    stack.pop()
                else:
                    return False
    return not bool(len(stack))

