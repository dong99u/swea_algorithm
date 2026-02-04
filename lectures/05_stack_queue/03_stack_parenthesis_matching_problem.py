def check_match(expression):
    stack = []

    target = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in expression:
        open = target.get(char)

        if open is not None:
            # 스택이 비어 있지 않거나 매칭이 되지 않는다면
            if not stack or stack[-1] != open:
                return False
            stack.pop()
        elif char in target.values():
            stack.append(char)

    # 스택이 비어있으면 True, 아니면 False
    return not stack



# 예시
examples = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)", 'ab{}']
for ex in examples:
    if check_match(ex): 
        print(f"{ex} 는 올바른 괄호") 
    else:
        print(f"{ex} 는 올바르지 않은 괄호")  
