A = [1,2,50,24,4,388,37]
B = [33,7,84,565,8,2]
A.sort()
B.sort()
print("The sorted A list")
print(list(A))
print("The sorted B list")
print(list(B))
C = A+B
C.sort()
print("The combined sorted list")
print(list(C))