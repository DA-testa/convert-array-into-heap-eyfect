# Vasīlijs Dvils-Dmittrijevs 221RDB381


def first(data, a, i, swaps):
    l = 2 * i + 1
    k = 2 * i + 2
    f = i
    if l < a and data[l] < data[f]:
        f = l
        
    if k < a and data[k] < data[f]:
        f = k
        
    if f != i:
        swaps.append((i,f))
        data[i], data[f] = data[f], data[i]
        first(data, a, f, swaps)    

def sec (data):
    swaps = []
    a = len(data)
    for i in range(a// 2 -1, -1, -1):
        first(data, a, i, swaps)
    return swaps

def main():
    txt = input()
    
    if 'I' in txt:
        n = int(input())
        data = list(map(int, input().split()))

    if 'F' in text:
        f = input()
        with open("tests/" + f, 'r') as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
            
    assert len(data) == n

    swaps = sec(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j) 



if __name__ == "__main__":
    main()
