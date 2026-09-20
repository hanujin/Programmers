def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    
    def char_2(string):
        char=[]
        for i in range(len(string)-1):
            c = string[i:i+2]
            if c.isalpha():
                char.append(c)
                
        return char
    
    from collections import Counter
    list1 = Counter(char_2(str1))
    list2 = Counter(char_2(str2))
    
    union = list1 | list2
    u = sum(union.values())
    intersection = list1 & list2
    i = sum(intersection.values())
    
    return int((i / u) * 65536) if u != 0 else 65536