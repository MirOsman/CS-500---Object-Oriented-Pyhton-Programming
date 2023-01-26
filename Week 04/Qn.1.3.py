def find_first_squareblock():
    r=[]
    R=int(input("Enter the no of rows  : "))
    M=[]
    Max=0
    fl=[]
    
    for i in range(R):
        row=[]
        for j in range(R):
            e=int(input("Enter the elements row by row :"))
            row.append(e)
        M.append(row)
    
    S=[[0 for col in range(R)] for row in range(2)]
    for i in range(R):
        for j in range(R):
            Element =M[i][j]
            if (Element):
                if j:
                    Element= 1+min(S[1][j-1],min(S[0][j-1],S[1][j]))
            S[0][j]=S[1][j]
            S[1][j]=Element
            
            Max= max(Max,Element)
    fl.append(i)
    fl.append(j)
    fl.append(Max)
    print("the largest matrix is",Max,"and it is at ",i-Max,j-Max)

    return print(fl) 
 
find_first_squareblock()