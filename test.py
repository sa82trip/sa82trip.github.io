# very basic of python
# print("hello world with python!!!")

# a_float= 3.14
# a_boolean = False 
# a_none = None 
# print(type(a_numberr))
# print()


##   days = "Mon, Tue, Wed, Thur, Fri"

# array of python
##   dayss = ["Mon", "Tue", "Wed", "Thur", "Fri"]

##   print("Mon" in dayss)
##   print("Man" in dayss)

# mutating array
##   dayss[0] = "월요일"
##   dayss.append("Sat")
##   print(dayss)
##   dayss.reverse()
##   print(dayss)

# 만약 바꿀 수 없는 리스트를 갖고 싶을 때는 튜플을 만들면 됨 tuple
# daysss = ( "Mon", "Tue", "Wed", "Thur", "Fri" )
# print(type(daysss))
# 
# name = "joon"
# age  = 30
# korean = True
# fav_food = ["Kimchi", "Sashimi"]
# 
# # dictionary example
# joon = {
#     "name" : "joon",
#     "age"  : 30,
#     "korean" : True, 
#     "fav_food" : ["Kimchi", "Sashimi"]
#         }
# print(joon)
# joon["handsome"]  = True
# print(joon)
# 
# 

# type casting
# age = "30"
# n_age = int(age)
# print(type(age))
# print(type(n_age))
# print(n_age)


# how to define(make) function
def say_hello():
    print("hello")
    print("bye")
# remember to write "()"to execute a function
say_hello()

# define with argument
def say_hello_1(who):
    print("hello",who)
    print("bye")

# call the function with parameter
# if you forget to pass parameter then you will getr an error
say_hello_1("Joon")

# we can make default value for argument like 'b'
def plus(a, b=0):
    print(a + b)
# we don't get any error for this calling
# because this function has its default value 
plus (10)

# difference of printing and returing
def p_plus(a, b=0):
    print (a + b)

def r_plus(a, b=0):
    return a + b

print("print")
p_result = p_plus(2, 3)
print("return")
r_result = r_plus(2, 3)

# print if there is value in variables
print(p_result, r_result)

# keyworded Arguments
def say_hello(name, age):
    return f"Hello { name } you are { age } years old"

hello  = say_hello(name = "joon", age = 30)
print(hello)
