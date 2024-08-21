if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans=0
    for i in range(n):
        if arr[i]!=arr[i+1]:
            ans=arr[i+1]
            break
        else:
            continue
    print(ans)
