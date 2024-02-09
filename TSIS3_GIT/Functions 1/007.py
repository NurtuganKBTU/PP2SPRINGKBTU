def Agent007(nums):
   string = ""
   for i in nums:
      if i == 0 or i == 7:
         string += str(i)
   if string.find("007") >= 0:
      return True
   return False
print(Agent007([1,2,4,0,0,7,5]))