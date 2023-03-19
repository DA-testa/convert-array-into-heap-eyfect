# python3
# Vasīlijs Dvils-Dmitrijevs 221RDB381


def sift_down(data):
    n = len(data)
    min = i
    
    l=2*i+1
    if l < n and data[l] < data[min]:
        min=l
        
    r=2*i+2
    if r < n and data[r] < data[min]:
        min=r
        
    if i != min:
        data[i], data[min] = data[min], data[i]
        swaps.append((i, min))
        sift_down(data, min, swaps)
        
        
def build_heap(data):
    n = len(data)
    swaps = []
    
    for i in range(n // 2, -1, -1)
        hpf(data, i, n, swaps)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    assert 1 <= n <= 10**5

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
