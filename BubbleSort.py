def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    print(arr)               
    
def main():
    array = [1,2,8,9,4,6,7]
    bubble_sort(array)

if __name__ == '__main__':
    main()
# Bubble sort duyệt qua danh sách và so sánh các cặp phần tử liền kề. 
# Các phần tử được hoán đổi nếu chúng không đúng thứ tự