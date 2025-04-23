# Bubble Sorting algorithm, Coctail Sorting algorithm, Selection Sorting algorithm, Gnome Sorting algorithm
# Merging sorting algorithm, Binary tree algorithm


# 1. Bubble Sorting Alrorithm
a = [5, 3, 2, 8, 7, 1, 6, 4]
n=0
m=0
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            m=m+1
        n=n+1

print("Bubble sorting: ", a)
print(n,m)


# 2. Selection sorting algorithm
a = [5, 3, 2, 8, 7, 1, 6, 4]
n=0
m=0
for i in range(len(a)):
    min_number = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_number]:
            min_number = j
            m=m+1
    a[i], a[min_number] = a[min_number], a[i]
    n=n+1

print("Selection sorting: ", a)
print(n,m)


# Matrix sort
A = [[23, 43], [11, 24], [49, 10]]

L=[0,0]
for j in range(2):
    for i in range(3):
        L[j]=L[j]+A[i][j]
print(L)
for i in range(3):
    A[i][0],A[i][1]=A[i][1],A[i][0]
print(A)



# Example 2 (Matrix sorting
A = [[30, 434, 647, 564], [711, 204, 470, 1209], [469, 210, 345, 112], [8422, 432,  545, 1938], [4509, 5564,9502, 2111]]

L = [0,0,0,0]
for i in range(4):
    for j in range(len(A)):
        L[i] = L[i]+A[j][i]
print(L)
for i in range(4):
    for j in range(3):
        if(L[j]>L[j+1]):
            L[j], L[j+1] = L[j+1], L[j]
            for k in range(len(A)):
                A[k][j], A[k][j+1] = A[k][j+1], A[k][j]
print(A)
#the code is not correctly done. sorting is not right. go through this again to make this correct.
