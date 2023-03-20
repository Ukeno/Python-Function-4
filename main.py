#Write a Python function called max_num() to find maximum of three numbers.
  #keyword | function | (parameters):
def max_num(num1, num2, num3):
    return max([num1, num2, num3])

print(max_num(101, 82, 593))

#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(lst):
    #if empty list, return 0
    #comparison operator (==), also known as the equality operator (==)
    #len() length
    if len(lst) == 0:
     return 0
  #product starts with first element of list
    prod = lst[0]

  #go through list elements and multiply them together
    if len(lst) > 1:
     for i in lst[1:]:
      prod = prod * i

     return prod
    
print(mult_list([101, 82, 593]))

# Write a Python function called rev_string() to reverse a string.
  
def rev_string(my_str):
  return my_str[::-1]

print(rev_string("python"))
print(rev_string("function practice"))

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,2,4))     
print(num_within(10,2,5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal(9) 