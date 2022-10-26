from itertools import product
def solution(numbers, target):
    answer = 0
    ll = [[idx, -idx] for idx in numbers]
    conclu = list(map(sum, list(product(*ll))))
    
    return conclu.count(target)