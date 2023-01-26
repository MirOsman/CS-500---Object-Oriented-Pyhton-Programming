#function named long_words which takes num(integer) and wordList(list of strings) as parameters
def long_words(num, wordList):

    #return the list of strings returned which are longer than num
    #here we are using list comprehension the if block checks whether the string in wordList
    #is greaterr than num or not
    return [word for word in wordList if len(word)>num]

print(long_words(4, ['apple', 'bus', 'lamp', 'tie', 'orange']))