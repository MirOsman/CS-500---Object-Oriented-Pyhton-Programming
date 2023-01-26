countriesAndCapitals={'China':'Beijing','Germany':'Berlin','Thailand':'Bangkok','Japan':'Tokyo','United States':'Washington, D.C.'}
count=0
for key in countriesAndCapitals.keys(): #for loop read each time the key value.
        UserInput = input("What is the Capital of " + key + " ? ") #Take the user input
        if(UserInput.lower() == countriesAndCapitals[key].lower()): #not case sensitive so making both in lowercase
            count = count + 1 #it will count the number of correct guesses
            print("Your Answer is Correct.")
        else:
            print("The Correct Answer should be "+countriesAndCapitals[key])

print("The correct Count is ",count)



