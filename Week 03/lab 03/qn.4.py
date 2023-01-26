# Initializing a 2D array with 4 rows and 2 columns with all 0 values
votes = [[0 for i in range(2)] for j in range(4)]

# variable to check we have to loop again or not 
choice = 0

# This loop will ask for inputs until user quits 
while(choice != -1):
    
    # A List to hold all the items of the menu  
    food_items = ['Pizza', 'Cupcake', 'Coffee', 'Pasta']
    
    print("\nThe four items of the menu are :\n1. Pizza\n2. Hotdog\n3. Ham\n4. Cheese")
    print("\nEnter 1: Like\t2: Dislike")
    
    # For loop to ask the user whether (s)he likes a particular food item or not
    for i in range(4):
        
        # User input 
        print("Enter your choice for",food_items[i],": ", end="")
        num = int(input())
        
        # Here 1 signifies that user likes the food and its count will be incremented by 1
        if(num==1):
            votes[i][0] += 1 
        
        # Here 2 signifies that user dislikes the food and its count will be incremented by 1
        elif(num==2):
            votes[i][1] += 1 
        
    # Asking the user whether other candidates also have to cast vote
    choice = int(input("\n Do you have another student ?(1 to enter) (-1 to exit ) : "))
    
    
# Printing the voting data
print("\nThe result of the votes is :")
print("\t\tLikes\tDislikes")

# Iterating through 4 rows
# \t prints a tab
for i in range(4):
    print(food_items[i], end="\t\t")
    
    # Iterating through 2 columns of the 2d array
    for j in range(2):
        print(votes[i][j], end="\t")
        
    # To print the data to a new line 
    print()
        

    