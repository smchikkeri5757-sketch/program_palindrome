
import sys
if len(sys.argv)==3:
  string_name1 = sys.argv[1]
  string_name2 = sys.argv[2]
else:
  string_name1 = "gadag"
  string_name2 = "malayalam"
if string_name1 == string_name1[::-1]:
  print(f"is a palindrome")
else:
  print(f"is not a palindrome")
if string_name2 == string_name2[::-1]:
  print(f"is a palindrome")
else:
  print(f"is not a palindrome")