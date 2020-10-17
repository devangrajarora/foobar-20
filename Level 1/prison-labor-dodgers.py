def solution(x, y):
    n = len(x)
    m = len(y)
    if n > m:
        x,y = y,x

    dx = {}
    for num in x:
        dx[num] = 1
    
    for num in y:
        if num not in dx:
            return num
            
        