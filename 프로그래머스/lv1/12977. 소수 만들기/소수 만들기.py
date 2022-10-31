def solution(nums):
    from itertools import combinations
    answer = 0
    ll = list(combinations(nums, 3))
    ll = list(map(sum, ll))
    all = ll

    for ww in all:
        count = 0
        for idx in range(2, ww):
            if ww % idx==0:
                count += 1
        if count==0:
            answer+=1
    
    return answer
