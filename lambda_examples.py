#Write a Python program to create a lambda function that adds 15 to a given number passed in as
# an argument, also create a lambda function that multiplies argument x with argument y and
# print the result.

# multi=lambda x,y:x*y
# print(multi(30,40))

#Write a Python program to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number.

# func=lambda x:x*15
# print(func(5))
# print(func(15))
# print(func(25))

#Write a Python program to sort a list of tuples using Lambda.
#
# lst=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print(sorted(lst,key=lambda x:x[1])) #sort by marks
# print(sorted(lst,key=lambda x:x[0])) #sort by subjects

#Write a Python program to sort a list of dictionaries using Lambda.
# models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
#
# print(sorted(models,key=lambda x:x['make'])) #sorting by make
#
# print(sorted(models,key=lambda x:x['color'])) #sorting by make

#Write a Python program to filter a list of integers using Lambda.

# lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(list(filter(lambda x:x%2==0,lst)))
#
# print(list(filter(lambda x:x%2!=0,lst)))
#
# Write a Python program to square and cube every number in a given list of integers using Lambda
#
# print(list(map(lambda x:x**2,[i for i in range(1,20)])))
#
# print(list(map(lambda x:x**3,[i for i in range(1,20)])))
#
# Write a Python program to find whether a given string starts with a given character using Lambda.

# starts_with=lambda x:True if x.startswith('P') else False
# print(starts_with('Python'))
# print(starts_with('python'))
#
# #Write a Python program to extract year, month, date and time using Lambda.
#
# import datetime
# now=datetime.datetime.now()
# print(now)
#
# year=lambda x:x.year
# month=lambda x:x.month
# day=lambda x:x.day
# time=lambda x:x.time()
# print(year(now))
# print(month(now))
# print(day(now))
# print(time(now))
#

#Write a Python program to check whether a given string is number or not using Lambda.
#
# is_num = lambda q: q.replace('.','',1).isdigit()
# print(is_num('26587'))
# print(is_num('4.2365'))
# print(is_num('-12547'))
# print(is_num('00'))
# print(is_num('A001'))
# print(is_num('001'))
# print("\nPrint checking numbers:")
# is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
# print(is_num1('-16.4'))
# print(is_num1('-24587.11'))

#Write a Python program to create Fibonacci series upto n using Lambda.
#
# from functools import reduce
#
# fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
#                               range(n - 2), [0, 1])
#
# print("Fibonacci series upto 2:")
# print(fib_series(2))
# print("\nFibonacci series upto 5:")
# print(fib_series(5))
# print("\nFibonacci series upto 6:")
# print(fib_series(6))
# print("\nFibonacci series upto 9:")
# print(fib_series(9))

# Write a Python program to find intersection of two given arrays using Lambda.

# intersection=lambda x,y:set(x).intersection(set(y))
# print(intersection([1,2,3,4,5,6],[7,8,9,1,2,3]))
# print(sorted(list(intersection([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]))))
#
# lst1=[1, 2, 3, 5, 7, 8, 9, 10]
# lst2=[1, 2, 4, 8, 9]
# intersection=list(filter(lambda x:x in lst1,lst2))
# print(intersection)
#
# #Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
#
# lst=[-1, 2, -3, 5, 7, 8, 9, -10]
# print(list(filter(lambda x:x>0,lst))+list(filter(lambda x:x<0,lst)))
#
# #Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
# lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(list(filter(lambda x:x%2==0,lst))+list(filter(lambda x:x%2!=0,lst)))
#

#Write a Python program to filter a given list whether the values in the
# list are having length of 6 using Lambda

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# print(list(filter(lambda x:x if len(x)==6 else '',weekdays)))
#
# print([i for i in weekdays if len(i)==6])
#
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# result=list(map(lambda x,y:x+y,nums1,nums2))
# print(result)
#
# Write a Python program to find numbers divisible by nineteen or thirteen from
# a list of numbers using Lambda.
# lst=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# print(list(filter(lambda x:(x%19==0 or x%13==0),lst)))

#Write a Python program to find palindromes in a given list of strings using Lambda

# lst=[str(i) for i in range(1,200)]
# #lst=[str(i) for i in lst]
# print(list(filter(lambda x:x==x[::-1],lst)))
#
# #Write a Python program to find all anagrams of a string in a given list of strings using lambda.
# str1='abcd'
# words=["bcda", "abce", "cbda", "cbea", "adcb"]
# print(list(filter(lambda x:sorted(str1)==sorted(x),words)))

#Write a Python program to find the numbers of a given string and store them in a list,
# display the numbers which are bigger than the length of the list in sorted form.
# Use lambda function to solve the problem.

# str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
# words=str1.split()
# nums=[int(i) for i in words if i.isdigit()]
# print(sorted(nums))

#Write a Python program that multiply each number of given list with a
# given number using lambda function. Print the result
#
# lst=[1,2,3,4,5,6,7,8,9]
# print(list(map(lambda x:x*8,lst)))

#Write a Python program that sum the length of the names of a given list of names after removing the names
# that starts with an lowercase letter. Use lambda function.

lst=['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
print([list(filter(lambda x:x[0].islower(),lst))])

print([list(filter(lambda x:x[0].isupper(),lst))])

#Write a Python program that removes the positive numbers from a given list of numbers. Sum the negative numbers and print
# the absolute value using lambda function. Print the result

lst=[2, 4, -6, -9, 11, -12, 14, -5, 17]
print((sum(list(filter(lambda x:x>0,lst)))))
print(abs(sum(list(filter(lambda x:x<0,lst)))))
