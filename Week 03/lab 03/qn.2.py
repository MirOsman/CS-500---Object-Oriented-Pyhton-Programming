def show_menu():
    print("1 - Find the largest score.")
    print("2 - Find the smallest score.")
    print("3 - Find the sum.")
    print("4 - Find the average score.")
    print("5 - Find the mode of score.")
    print("6. Exit")
    

def get_data():
    score_list_str = input("Enter a list of scores(from 0 to 10), use space as a separator: ")
    score_list = list(map(int,score_list_str.split(" "))) 
    return score_list

def process_data(score_list):
    min = 10
    max = 0
    sum = 0
    average = 0.0
    mode = 0
    mode_map = {}
    mode_max = 0
    
    for score in score_list:
         sum += score
         if score < min:
             min = score
         if score > max:
             max = score
         if score in mode_map:
             mode_map[score] += 1
         else:
             mode_map[score] = 1
             
         
    average = sum / len(score_list)
    print(mode_map)
    for key, value in mode_map.items():
        if mode_max < value:
            mode_max = value
    mode = [k for k, v in mode_map.items() if v == mode_max]
    return max,min,sum,average,mode

def main():
  score_list = get_data()
  max, min, sum, average, mode = process_data(score_list)
  print(max,min,sum,average,mode)
    
  while True:
        show_menu()
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            print("The largest score is", max)
        elif choice == 2:
            print("The smallest score is",min)
        elif choice == 3:
            print("The sum is", sum)
        elif choice == 4:
            print("The average is", average)
        elif choice == 5:
            print("The mode is", mode)
        elif choice == 6:
            break
    
        

if __name__ == "__main__":
    main()