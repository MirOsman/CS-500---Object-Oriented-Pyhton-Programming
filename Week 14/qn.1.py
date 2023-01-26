class Solution:
   #defining function twoSum() with two parameters 
   def twoSum(self,nums,target):
       #using nested for loop, checking elements in the list
       for item in range(len(nums)):
               for items in range(item+1,len(nums)):
                   #checking sum of two elements in the list is equal to target
                   #if yes, return the index of both elements in the list
                   if target == nums[item]+nums[items]:
                       return [item,items]
#creating list nums1 
nums1 = [2,7,11,15]
#setting target1 as 9
target1 = 9
#creating object for the class Solution
obj = Solution()
#invoking function twoSum() by passing nums1 and target1 as arguments
#and display the result on the console
print(obj.twoSum(nums1,target1)) 
#creating list nums2 
nums2 = [3,2,4]
#setting target2 as 6
target2 = 6
#invoking function twoSum() by passing nums2 and target2 as arguments
#and display the result on the console
print(obj.twoSum(nums2,target2)) 
#creating list nums3
nums3 = [3,3]
#setting target3 as 6
target3 = 6
#invoking function twoSum() by passing nums3 and target3 as arguments
#and display the result on the console
print(obj.twoSum(nums3,target3)) 