def trace(matrix):
    sum=0;
    o=len(matrix);
    k=len(matrix[0]);
    if o!=k:
        print("Not a square matrix")
    else:
        for i in range(o):
            sum=sum+matrix[i][i]
    return sum



matrix =(
         [[4, 6, 7, 3, 2],
          [ 7, 5, 8, 5, 6],
          [ 8, 2, 1, 2, 1],
          [ 3, 3, 6, 4, 7],
          [6, 4, 9, 5, 3]])

print (trace(matrix))
