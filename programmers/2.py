def solution(s):
    answer = 0

    s = list(s)
    for r in range(len(s)):
        if r > 0:
            tmp = s.pop(0)
            s.append(tmp)
      
        stack = []
        for i in s:
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(i)
                    break
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
                    break
            elif i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(i)
                    break
        
        if not stack:
            answer += 1

    return answer

print(solution("}]()[{"))