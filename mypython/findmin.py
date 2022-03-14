nums = [672946,2749236,3947658,937648,465428,92644,463956,2890564,2145689,23223,47389,21355]
smallest = nums[0]
smallestIndex = 0;
for index, x in enumerate(nums):
   if (x < smallest):
       smallest = x 
       smallestIndex = index
print( smallest )
print( smallestIndex)