# use filter() to find the students who have the score higher than 95
students = [ {"name": "Peter", "score": 99},
{"name": "Lily", "score": 78},
{"name": "Tom", "score": 100}]

goodStudents = list(filter(lambda x : x['score'] > 95, students))

#print(goodStudents)

# get students whose name start with L

getStudentsL = list(filter(lambda x : x['name'][0] == "L" , students))

print(getStudentsL)