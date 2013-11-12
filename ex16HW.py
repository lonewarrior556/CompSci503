class Time(object):
    """ Represents the time of day.
    attributes: hour, minute, second """

time=Time()

time.hour=11
time.minute=59
time.second=30

# Exercise 16.1. Write a function called print_time that takes a Time object 
# and prints it in the form hour:minute:second. Hint: the format sequence 
# '%.2d' prints an integer using at least two digits, including a leading zero 
# if necessary.

def print_time(time):
    print '%.2d hours %.2d minutes and %.2d seconds' % (time.hour, time.minute, time.second)
    
# Exercise 16.2. Write a boolean function called is_after that takes two Time 
# objects, t1 and t2, and returns True if t1 follows t2 chronologically and 
# False otherwise. Challenge: don't use an if statement.

def is_after(t1,t2):
    a=3600*t1.hour+60*t1.minute+t1.second
    b=3600*t2.hour+60*t2.minute+t2.second
    return a>b

#Exercise 16.3. Write a correct version of increment that doesnt contain 
#any loops.

def increment(time,seconds):
    a=time.second+seconds
    b=time.minute+a/60
    time.hour+=b/60
    time.minute=b%60
    time.second=a%60

# Exercise 16.4. Write a "pure" version of increment that creates and returns 
# a new Time object rather than modifying the parameter.

def pureinc(time,seconds):
    import copy
    time2=copy.copy(time)
    increment(time2,seconds)
    return time2

#Exercise 16.5. Rewrite increment using time_to_int and int_to_time.
""" this was kinda done"""

def seconds(t1):
    return ((3600*t1.hour)+(60*t1.minute)+(t1.second))

def t2t(a):
    time=Time()
    time.hour=a/3600
    a=a%3600
    time.minute=a/60
    time.second=a%60
    return time


# Exercise 16.6. Write a function called mul_time that takes a Time object and 
# a number and returns a new Time object that contains the product of the 
# original Time and the number. Then use mul_time to write a function that takes 
# a Time object that represents the finishing time in a race, and a number that 
# represents the distance, and returns a Time object that represents the average 
# pace (time per mile).

def mul_time(t1,n):
    a=seconds(t1)*n
    return t2t(int(round(a)))
    
def pace(ftime, miles):
    return mul_time(ftime,1.0/miles)
    
    
# Exercise 16.7. The datetime module provides date and time objects that are 
# similar to the Date and Time objects in this chapter, but they provide a 
# rich set of methods and operators. 

# 1. Use the datetime module to write a program that gets the current date and 
# prints the day of the week.

# 2. Write a program that takes a birthday as input and prints the user's age 
# and the number of days, hours, minutes and seconds until their next birthday.

# 3. For two people born on different days, there is a day when one is twice as 
# old as the other. That's their Double Day. Write a program that takes two 
# birthdays and computes their DoubleDay.

# 4. For a little more challenge, write the more general version that computes 
# the day when one person is n times older than the other.
