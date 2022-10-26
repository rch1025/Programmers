def solution(s):
    answer = [] # 정답이 들어갈 공간
    count = 0
    zero_count = 0
    
    while len(s)>1:
        count+=1
        len_ = len(s)
        s = s.replace('0','')
        zero_len = len(s)
        zero_count += len_-zero_len # 제거된 0의 개수
        s = bin(len(s))[2:]
        
    return [count, zero_count]