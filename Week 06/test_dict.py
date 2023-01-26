#write a function that returns a dictionary of students average
# key : student name, value : score average

def get_averages(scores: dict[str, list[int]]) -> dict[str,float] :
    averages : dict[str, float] = {}
    
    for k,v in scores.items():
        name : str = k      # e.g. Peter
        scorelist : list[int] = v     # e.g. [8,9,10]
        sum : int = 0
         
        for score in scorelist:
          sum += score
        average : float = sum / len(scores)
        averages[name] = average
    
    return averages


# write a function that returns a student who has the highest average

def get_best_student(scores : dict[str, list[int]]) -> str :
    averages : dict[str, float] = get_averages(scores)
    best_student : str = " "
    for name in averages:
        if best_student == " ":
            best_student = name
            
        elif averages[name] > averages[best_student] :
            best_student = name
 
    return best_student

# write a function that returns a list of student who have averages greater than 8.0

def get_best_students(scores : dict[str, list[int]]) -> list[str] :
    averages : dict[str, float] = get_averages(scores)
    best_students : list[str] = []
    for name in scores:
        if averages[name] >= 8.0:
            best_students.append(name)
 
    return best_students

def main():
    #courses : dict[str, str] = {"CS204": "C Programming", "CS360": "C++ Programming", "CS480": "Java Programming"}
    #print(courses)
    
    #print(courses["CS360"])
    
    #for k,v in courses.items():            #Dict will have key/value pairs in it but list will have a list of items
        #print(k, v)
    
    #for i in courses:
        #print(i)
    
    #for k in courses:                  #1st method
        #print(courses[k])
                                        
    #for k in courses:                     #2nd method
        #print(k, courses[k])     #Both methods are acceptable
        
    # a dictionary of students scores
    # Peter 8,9,10
    # Lily 10,6,7
    #Jun 9,8,9
    scores: dict[str, list[int]] = {}
    scores["Peter"] = [8,9,10]
    scores["Lily"] = [10,6,7]
    scores["Jun"] = [9,8,9]
    
    print(scores)
    print()
    print(get_averages(scores))
    print()
    print("The best student is = ", get_best_student(scores))
   # print()
    print("The best students is = ", get_best_students(scores))
        
if __name__ == "__main__":
 main()