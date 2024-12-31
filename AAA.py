A = [6,5,4,3,2,1]


def solution(A):
    # Implement your solution here
    for x in range(len(A)):
        for i in range(len(A)-x-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
            # i += 1

    return A

m = 0
if len(A) % 2 == 0:
    m = (A[len(A)/2-1] + A[len(A)/2])//2
else:
    m = A[len(A)//2]   

print(m)
print(len(A))
print(solution(A))