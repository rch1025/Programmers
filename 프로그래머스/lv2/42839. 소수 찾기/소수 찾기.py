def solution(numbers):
    from itertools import permutations
    answer = 0
    ww = []
    for num in range(1, len(numbers)+1):
        ww += list(map(int, map("".join, list(permutations(numbers, num)))))
    
    ww = list(set(ww))
    for w_one in ww:
        if (w_one==1) or (w_one==0): # 0혹은 1이면 skip -> 소수에 해당 안 됨
            continue
        count = 0
        for idx in range(2, int(w_one**0.5)+1): # 루트의 +1한 것만 비교하기
            if w_one % idx == 0:
                count += 1 # 1 혹은 자기 자신이 아닌 다른 수에서 약분이 되면 count에 1 추가
        if count==0:
            answer += 1 # count가 0이라면 소수이기에 +1
            
    return answer