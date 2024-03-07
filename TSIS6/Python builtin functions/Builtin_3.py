# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def palindromecheck(s):
   t = s[::-1]
   if t == s:
      return f"Yes"
   return "No"

    
s = input()
print(palindromecheck(s))
