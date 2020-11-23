import numpy as np

# Method1: Using numpy
def transpose(mat):
    return np.transpose(mat) 

# Method2: Using loops
def transpose_loops(l1):
    l2 = []
    for i in range(len(l1[0])):
        row =[] 
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return np.matrix(l2)

# Method3: Using List comprehensions
def transpose_list_com(l1): 
	l2 =[[row[i] for row in l1] for i in range(len(l1[0]))] 
	return np.matrix(l2) 

# Method4: Using zip function
def transpose_zip(l1): 
	l2 = list(map(list, zip(*l1))) 
	return np.matrix(l2) 

# Driver code 
if   __name__ == '__main__':
    mat = [[2, 4, 1, 3],
          [6, 3, 9, 5],
          [3, 2, 3, 6],
          [2, 5, 4, 2]]
    
    print('Using numpy')    
    print(transpose(mat))
    print()
    
    print('Using loops')    
    print(transpose_loops(mat))
    print()
    
    print('Using List comprehensions')    
    print(transpose_list_com(mat))
    print()
    
    print('Using zip')    
    print(transpose_zip(mat)) 

