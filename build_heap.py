def sift_down(data, n, i, swaps):

    l = 2 * i + 1
    t = 2 * i + 2
    min_index = i
    
    if l < n and data[l] < data[min_index]:
        min_index = l

    if t < n and data[t] < data[min_index]:
        min_index = t

    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(data, n, min_index, swaps)


def build_heap(data):
    n = len(data)
    swaps = []

    for i in range(n// 2 -1, -1, -1):
        sift_down(data, n, i, swaps)

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
