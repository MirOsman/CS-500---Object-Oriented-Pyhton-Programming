#taking list of strings as input from the user
inp = [i for i in input().split()]
letters = ["car","ABBA","def","love", "Orange", "anti"]

#list named vowels
vowels = ['a','e','i','o','u']

#lambda function to check last character is vowel or not
isVowel = lambda x: x[-1].lower() in vowels

#store the list of strings with vowel as the last character
out = [word for word in inp if(isVowel(word))]

#print the out list

#print(out)


letters = ["car","ABBA","def","love", "Orange", "anti"]

result = [word for word in input if (lambda x:x[-1].lower() in "aeiow")(word)]
print(result)