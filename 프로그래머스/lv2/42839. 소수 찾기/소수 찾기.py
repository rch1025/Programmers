def solution(numbers):
    from itertools import permutations
    answer = 0
    ww = []
    for num in range(1, len(numbers)+1):
        ww += list(map(int, map("".join, list(permutations(numbers, num)))))
    
    ww = list(set(ww))
    for w_one in ww:
        if (w_one==1) or (w_one==0): # 0혹은 1이면 취소
            continue
        count = 0
        for idx in range(2, int(w_one**0.5)+1):
            if w_one % idx == 0:
                count += 1
        if count==0:
            answer += 1
            
    return answer