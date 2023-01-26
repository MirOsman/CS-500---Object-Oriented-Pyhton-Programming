#function named smaller_than which takes limit integer and numbers list of integers
def smaller_than(limit,numbers):

    #return the list of integers which are smaller than limit
    #here we are using list comprehension the if block checks whether the integer of numbers list
    #is smaller than limit or not
    return [i for i in numbers if i < limit]
print(smaller_than(8, [3,5,9,-10,9]))
