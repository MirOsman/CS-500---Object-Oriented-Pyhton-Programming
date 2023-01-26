
list = []
for n in range (100):
     component = input("Type your sequence of words: ")
     if component == 'exit':
        break
     if component not in list:
         list.append(component)
                
print('words after sorting :', sorted(list))
      

