# Write a program whose input is two integers, and whose output is the first integer and
# subsequent increments of 5 as long as the value is less than or equal to the second integer.
# Ex. If the input is: -15 10 The output is: -15 -10 -5 0 5 10
# Ex. If the second integer is less than the first. The output is: Second integer can't be less than the first.

# start = int(input())
# end = int(input())
# if start > end:
#     print("Second integer can't be less than the first.")
# else:
#     while start <= end:
#         print(start, end=' ') # this keeps getting new line errors when outputting
#         start += 5


# start = int(input())
# end = int(input())
# 
# if start > end:
#     print("Second integer can't be less than the first.")
# else:
#     while start <= end:
#         print(start, end=' ')
#         start += 5

# start = int(input().strip())
# end = int(input().strip())
# 
# if start > end:
#     print("Second integer can't be less than the first.")
# else:
#     while start <= end:
#         print(start, end=' ')
#        start += 5
        


# Prints the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.
#   Args:
#     start: The first integer.
#     end: The second integer.

def print_increments(start, end):
  
  if start > end:
    print("Second integer can't be less than the first.")
  else:
    for num in range(start, end + 1, 5):
      print(num, end=" ")  # Print without newline

# Example usage (without input)
print_increments(-15, 10)  