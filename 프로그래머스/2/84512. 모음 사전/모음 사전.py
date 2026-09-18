def solution(word):
    answer = 0
    dictionary = {'A': 0, 'E': 1, 'I': 2, 'O':3, 'U':4}
    weights = [
    5**0 + 5**1 + 5**2 + 5**3 + 5**4,
    5**0 + 5**1 + 5**2 + 5**3,
    5**0 + 5**1 + 5**2,
    5**0 + 5**1,
    5**0
    ]
    
    for i, ch in enumerate(word):
        answer += weights[i] * dictionary[ch] + 1
        
    return answer
    