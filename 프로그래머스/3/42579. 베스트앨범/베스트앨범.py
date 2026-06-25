def solution(genres, plays):
    answer = []
    genre_total={}
    genre_songs={}
    for i in range(len(genres)):
        g=genres[i]
        if g not in genre_total:
            genre_total[g]=0
        genre_total[g] += plays[i]
        
        if g not in genre_songs:
            genre_songs[g] = []
        genre_songs[g].append((plays[i], i))
    
    sorted_genres = sorted(genre_total, key=lambda g:genre_total[g], reverse=True)
    
    for g in sorted_genres:
        songs = genre_songs[g]
        
        songs.sort(key=lambda x:(-x[0], x[1]))
        
        for song in songs[:2]:
            answer.append(song[1])

    return answer