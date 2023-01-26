def main():
    print("Find the time x minutes before and after the input time")
    timestring = input("Enter a time(hh:mm): ")
    shiftMins = int(input("Enter a time shift in mins: "))
    
    timeArray = timestring.split(":")
    hours = int(timeArray[0])
    mins = int(timeArray[1])
    
    print("You entered: {0:02d} : {1:02d}". format(hours, mins))
    totalMins = hours * 60 + mins
    #Find the time before
    timebeforeInMins = totalMins - shiftMins
    hoursbefore = timebeforeInMins // 60 % 24
    minsbefore = timebeforeInMins % 60
    print("Before: {0:02d} : {1:02d}". format(hoursbefore, minsbefore))
    
    #Find the time after
    timeafterInMins = totalMins + shiftMins
    hoursafter = timeafterInMins // 60 % 24
    minsafter = timeafterInMins % 60
    print("after: {0:02d} : {1:02d}". format(hoursafter, minsafter))
    
    
if __name__=="__main__":
        main()