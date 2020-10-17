def solve(n,m):
    if n <= 0 or m <= 0:
        return -1
    elif n == 1 and m == 1:
        return 0
    elif n == m:
        return -1
    
    if n < m:
        n,m = m,n
        
    if m == 1:
        return n - 1

    if n % m == 0:
        return -1
        
    small = solve(n%m,m)
    
    if small == -1:
        return -1
    else:
        return int(n/m) + small

def solution(x, y):
    n = int(x)
    m = int(y)
    
    if n < m:
        n, m = m,n
    
    ans = solve(n,m)
    if ans == -1:
        return "impossible"
    else:
        return str(ans)

if __name__ == '__main__':
    x = input('Enter x: ')
    y = input('Enter y: ')
    ans = solution(x,y)
    print(ans)