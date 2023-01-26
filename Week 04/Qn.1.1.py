# Function to find the size of the first square submatrix with minimun size 3
# present in a given binary matrix
      
def find_square_matrix(size, *elements):

    numbers = list(elements)
    if size ** 2 != len(numbers):
        return "Number of elements does not match the size of the matrix"
    else:
        matrix = []
        factor = 0
        for i in range(0, size):
            row = []
            for j in range(factor * size, (factor + 1) * size):
                row.append(numbers[j])
            factor += 1
            matrix.append(row)
            i += 1
        return matrix

 
 
def find_first_squareblock(matrix : list[int]) -> list[int]:
      for m in range(0, len(matrix)) :
        sm = 0
        for n in range(0, len(matrix[m])):
            val = matrix[n][m]
            if val < 0:
                return False
            sm = sm + val          
  
        if (sm != 1) :
            return False
        return True
def main():
    size = int(input("Enter the number of rows in matrix: "))
    matrix = [0] * size
    for m in range(size):
        matrix[m] = [0] * size
    print("Enter a {}-by-{} matrix row by row:".format(size, size))

    for n in range(size):
        temp = input()
        list_of_var_float = list(map(float, temp.split(" ")))
        count = 0
        for k in list_of_var_float:
            matrix[n][count] = k
            count += 1
    
    print("The first square matrix is at (" , ") with size: ")
 
if __name__ == '__main__':
    main()