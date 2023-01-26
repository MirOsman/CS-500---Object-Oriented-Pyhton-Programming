nums = ["Even" if x % 2 == 0 else "Odd" for x in range(10) ]
#print(nums)

#Change the above statement so we can get a list of booleans. If the number can be divided
# by 4, it is True otherwise False

#[0,1,2,3,4,5,6,7,8,9]
#[True, False, False, False, True..........]
nums = [ True if x % 4 == 0 else False for x in range(10)]
#print(nums)

nums = [str(x) for x in range(10)]
#print(nums)


nums = {x : "Even" if x % 2 == 0 else "Odd" for x in range(10) }
print(nums)