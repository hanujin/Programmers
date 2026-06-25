def solution(participant, completion):
    from collections import Counter
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]