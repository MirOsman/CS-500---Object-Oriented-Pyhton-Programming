def is_Markov_matrix(matrix):
    
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
    size = int(input("Enter the size of matrix: "))
    matrix = [0] * size   # a list of integer        #or you can write matrix = [[]] * size         a list of list
    #matrix = [0.0] * size     a list of float       single row(one dimensional)
   # matirx = [''] * size       a list of strings
   
    for m in range(size):          # for dimensional row 
        matrix[m] = [0] * size
    print("Enter a {}-by-{} matrix row by row:".format(size, size))     #Get numbers from keyboard and fill in table
    #rowstr = input().split(" ")
    #print(rowstr)                    #just for one row
    #for c in range(size):
    #matrix[0][c] = float
    # (rowstr[c]) 

    for n in range(size):
        temp = input()
        list_of_var_float = list(map(float, temp.split(" ")))
        count = 0
        for k in list_of_var_float:
            matrix[n][count] = k
            count += 1
    if is_Markov_matrix(matrix):
        print("It is a Markov matrix")
    else:
        print("It is not a Markov matrix")
    
if __name__ == "__main__":
    main()
