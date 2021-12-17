def partition(A, p, r):
    pivot = A[r]
    i = p - 1 #track A[j] < pivot
    for j in range(p, r):
        if A[j] <= pivot:
            i+=1 #grow Blue
            A[i], A[j] = A[j], A[i]
    #Swap A[i+1] & A[r] once done
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)
    print(A)
def main():
    A = [1,3,2,9,5,4,8,7]
    quicksort(A, 0, len(A) - 1)
if __name__ == '__main__':
    main()
    
