# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print(f"Your username is: {user_name} ")
user_name=input("Enter your username")
hello_name(user_name)
    
# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    n=0
    for n in range (1,101):
        if n%2 !=0:
            print (n)
first_odds()
                
  
  

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

 

def max_num_in_list(a_list):
    max_number=a_list[0]    
    for i in range(len(a_list)):
        if a_list[i]>max_number:
            max_number=a_list[i]

    return max_number
a_list=[99,33,22,1000,4]
print(max_num_in_list(a_list))



#     Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

 
def is_leap_year(a_year):
    if a_year % 4 ==0:
        return True
    elif a_year%100!=0:
        return False
    elif a_year%400==0:
        return True
a_year=int(input("Enter the year") )
print(is_leap_year(a_year))
                
  

# Question 5D
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    for i in range(len(a_list)):
        if a_list[i]+1==a_list[i+1] or a_list[i]-1==a_list[i+1]:
            return True
        else:
            return False
a_list=[2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list=[1,2,4,5]
print(is_consecutive(a_list))