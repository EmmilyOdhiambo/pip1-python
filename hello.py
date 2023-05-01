#Write a Python function that takes two arguments (a and b) and returns their sum.
def total_numbers(a,b):
    add = a + b
    return add
ans = total_numbers(50,100)
print(ans)
#Write a Python function that takes a string as input and returns the string reversed.
def reversed_string(name):
    return name[::-1]
print(reversed_string("Emmily"))


#Write a Python function that takes a list of integers as input and returns
#  the sum of all the integers in the list.
def total_num(nums):
    sum = 0
    for i in nums:
        sum +=i
    return sum
print(total_num([11, 5, 17, 18, 23]))


   

#Write a Python function that takes a list of integers as input and returns a new list
#  with all the even numbers removed.  

def remove_even_nums(nums):
    answer = []
    for i in nums :
        if i%2!=0:
            answer.append(i)
    return answer
print(remove_even_nums([1,2,3,4,5]))


#Wrte a Python function that takes a list of integers as input and returns 
# the highest value in the list.
def high_number(numbers):
    num = max(numbers)
    return num
print(high_number([10,20,30,40,50]))


#Write a Python function that takes a list of strings as input and returns a new 
# list with all the strings capitalized.  
def capitalize_string(words):
    return[word.capitalize()for word in words]
print(capitalize_string(["joe","yuep","emmie"]))  