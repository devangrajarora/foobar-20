def solution(l):
    # Your code here
    n = len(l)
    ans = 0
    for j in range(1,n-1):
        
        small = 0
        big = 0
        
        for i in range(j):
            if l[j] % l[i] == 0:
                small += 1
        
        for k in range(j+1,n):
            if l[k] % l[j] == 0:
                big += 1
        
        ans += (small * big)
        
    return ans

if __name__ == '__main__':
    l = list(map(int,input().split()))
    ans = solution(l)
    print(ans)