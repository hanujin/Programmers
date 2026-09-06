def solution(s):
    cnt = 0
    num0s = 0
    while s != "1":
        num0 = s.count("0")
        num0s += num0 
        s = (len(s) - num0) * 1
        s = bin(s)[2:]
        cnt += 1
        
    list = [cnt, num0s]
    
    return list