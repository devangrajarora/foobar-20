def solution(a):
    # Your code here
    a.sort()
    n = len(a)

    if n == 0:
        return 0
    
    if n == 1:
        return a[0]

    pos = 0
    zero = 0
    neg = 0

    for num in a:
        if num == 0:
            zero += 1
        elif num < 0:
            neg += 1
        else:
            pos += 1

    if pos == 0:
        if neg < 2:
            if zero > 0:
                return 0
            else:
                return a[0]
    
    ans = 1

    for i in range(0,n):
        if i != n-1 and a[i] < 0 and a[i+1] < 0:
            print(a[i],a[i+1])
            ans *= (a[i] * a[i+1])
            a[i+1] = 0
        if a[i] > 0:
            ans = ans * a[i]

        print("ans:",ans)
    return str(ans)

if __name__ == "__main__":
    
    a = list(map(int,input().split()))
    print(solution(a))