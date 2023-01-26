 
 
def find_first_squareblock(matrix : list[int]) -> list[int]:
      rows : int = len(matrix)
      columns : int = len(matrix[0])
      
      dp : list[list[int]] = [0] * rows + 1
      for i in range(rows + 1) :
          matrix[i] = [0] * columns + 1
          
          maxsqlen = 0
          for i in range(1, rows + 1):
              for j in range(1, columns + 1) :
                  #if matrix [i-1][j-1] == 1:
                  if matrix [i][j] == 1:
                      dp[i][j] = 1
                  else :
                      matrix [i][j] = 1 
                      #dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + 1)
                      dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
                      maxsqlen = max(maxsqlen, dp[i][j])
                      dp.append[i]
                      dp.append[j]
                      dp.append[maxsqlen]
                      
          for k in range(len(dp)) :
              print(dp[k])
          return[maxsqlen]
                      
                      
def main():
    print("Find the first square matrix with minimun size 3")
    rows : int = int (input("Enter the number of rows in the matrix : "))
    
    matrix : list[list[int]] = [[0] * (rows + 1) * (rows + 1)]
    print("Enter the matrix row by row:")
    for j in range(rows):
        temp : str = input()
        list_of_var_int : list[int] = list(map(int,temp.split(" ")))
    
    print("The first square submatrix is at ("  ") with size: ")
 
if __name__ == '__main__':
    main()