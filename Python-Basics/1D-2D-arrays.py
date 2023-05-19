#interview question
L = [1,2,3,4,5,6]

L[0] = L[5] = 0

print(L)


# First method to create a 1 D array 
N = 5
arr = [0]*N 
print(arr) 

# Second method to create a 1 D array 
N = 5
arr = [0 for i in range(N)] 
print(arr) 

# Using above first method to create a 
# 2D array 
rows, cols = (5, 5) 
arr = [[0]*cols]*rows 
print(arr) 

# Using above second method to create a 
# 2D array 
rows, cols = (5, 5) 
arr = [[0 for i in range(cols)] for j in range(rows)] 
print(arr) 
