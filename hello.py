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
def culculate_total(nums):
    total = 0
    # list1 = [11, 5, 17, 18, 23]
    for i in nums:
        sum +=i
    return sum
print(calculate_total([11, 5, 17, 18, 23]))


   

#Write a Python function that takes a list of integers as input and returns a new list
#  with all the even numbers removed.  

def remove_even_nums():
    answer = []
    for i in range(100,210):
        if i%2==0:
            answer.append(i)
        return answer


#Wrte a Python function that takes a list of integers as input and returns 
# the highest value in the list.
def high_number():
    x = [10,20,30,40,50]
    print(high_number(max(x)))


#Write a Python function that takes a list of strings as input and returns a new 
# list with all the strings capitalized.  
def capitalize_string(word):
    return[word.capitalize()for word in words]
print(capitalize_string(["joe","yuep"]))  