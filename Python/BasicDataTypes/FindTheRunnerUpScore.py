if __name__ == '__main__':
    n = int(input())
    arr = input().split(sep=" ", maxsplit=n - 1)
    arr = [int(a) for a in arr]
    arr.sort(reverse=True)
    maxScore = arr[0]
    for a in arr[1:]:
        if not (a == maxScore):
            print(a)
            break
