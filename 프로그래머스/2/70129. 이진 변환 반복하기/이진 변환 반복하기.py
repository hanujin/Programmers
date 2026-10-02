def solution(s):
    answer = []
    count = 0
    num = 0
    
    while s != "1":
        n = s.count("0")
        s = bin(len(s) - n)[2:]
        
        count += 1
        num += n
    
    return [count, num]