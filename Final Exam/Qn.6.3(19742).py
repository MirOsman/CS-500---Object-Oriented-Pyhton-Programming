#from functools import the reduce function
from functools import reduce

#function named get_code which takes list of strings named word_list
def get_code(word_list):

    #In reduces' function which takes list which contains the length of each word in word_list
    #The lambda function multiply the first parameter with 10 and add the second parameter to a
    result = reduce(lambda a,b:a*10+b,[len(word) for word in word_list])

    #finally result was returned
    return result
word_list = ['hello', 'world', 'how', 'goes', 'tears']
print(get_code(word_list))

 