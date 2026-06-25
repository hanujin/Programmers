def solution(number, k):
    answer = ''
    stack=[]
    for num in number:
        while k > 0 and stack:
            if stack[-1] < num:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(num)
        
    if k > 0:
        stack=stack[:-k]
        
    return "".join(stack)