def solution(order):
    stack = []
    num = 1
    count = 0
    
    for i in range(len(order)):
        while num < order[i]:
            stack.append(num)
            num += 1
            
        if num == order[i]:
            num +=1
            count += 1
        
        elif len(stack) != 0 and stack[-1] == order[i]:
            stack.pop()
            count += 1
            
        else:
            break
    
    return count