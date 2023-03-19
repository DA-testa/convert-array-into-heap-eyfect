# Vasīlijs Dvils-Dmittrijevs 221RDB381


def first(data, n, i, swaps):

    l = 2 * i + 1
    t = 2 * i + 2
    r = i
    
    if l < n and data[l] < data[r]:
        r = l

    if t < n and data[t] < data[r]:
        r = t

    if r != i:
        
        swaps.append((i,r))
        data[i], data[r] = data[r], data[i]
        first(data, n, r, swaps)


def build_heap (data):
    swaps = []
    n = len(data)

    for i in range(n// 2 -1, -1, -1):
        first(data, n, i, swaps)

    return swaps


def main():
    text = input()
    
    if 'I' in text:
        k = int(input())
        data = list(map(int, input().split()))
        
    if 'F' in text:
        f = input()
        with open("tests/" + f, 'r') as file:
            k = int(file.readline())
            data = list(map(int, file.readline().split()))

    
    assert len(data) == n

    
    swaps = build_heap(data)

    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
