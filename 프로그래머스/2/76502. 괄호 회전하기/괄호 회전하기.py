def solution(s):
    def is_correct(s):
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        stack=[]
        for i in s:
            if i in ("[", "(", "{"):
                stack.append(i)
            elif len(stack) != 0 and pairs[i] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return True if len(stack) == 0 else False
                
    answer = 0     
    n = len(s)     
    for i in range(n):
        new = s[i:] + s[:i]
        if is_correct(new):
            answer += 1

    return answer