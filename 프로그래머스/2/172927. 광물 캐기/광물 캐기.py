def solution(picks, minerals):
    
    weights = {"diamond":25, "iron":5, "stone": 1}
    fatigue = {
        "dia":   {"diamond": 1,  "iron": 1, "stone": 1},
        "iron":  {"diamond": 5,  "iron": 1, "stone": 1},
        "stone": {"diamond": 25, "iron": 5, "stone": 1}
    }
    minerals = minerals[:5 * sum(picks)]
    
    groups = []
    for i in range(0, len(minerals), 5):
        group = minerals[i:i+5]
        difficulty = sum(weights[mineral] for mineral in group)
        groups.append((difficulty, group))
    groups.sort(reverse=True)
    
    answer = 0
    for difficulty, group in groups:
        if picks[0] > 0:
            tool = "dia"
            picks[0] -=1       
        elif picks[1] > 0:
            tool = "iron"
            picks[1] -=1 
        elif picks[2] > 0:
            tool = "stone"
            picks[2] -=1 
        else:
            break

        for mineral in group:
            answer += fatigue[tool][mineral]
            
    return answer