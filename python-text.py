'''
Python Iterators:
	Iterators are objects that can be iterated upon. In this tutorial, you will learn how iterator works and how you can build your own iterator using __iter__ and __next__ methods.

Python Generators
	It is fairly simple to create a generator in Python. It is as easy as defining a normal function, but with a yield statement instead of a return statement.

	If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.

	The difference is that while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.

Python Closures
	Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.

Python Decorators
	A decorator takes in a function, adds some functionality and returns it

List Comprehension in Python
	As list comprehensions return lists, they consist of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.

Zip & Unzip:

	The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.
							mapped = zip(name, roll_no, marks) 

	Unzipping means converting the zipped values back to the individual self as they were. This is done with the help of “*” operator.
							namz, roll_noz, marksz = zip(*mapped)

Filter Funtion:
	The filter() function in Python takes in a function and a list as arguments.

	The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.
							new_list = list(filter(lambda x: (x%2 == 0) , my_list))

	The map() function in Python takes in a function and a list.

	The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.
							new_list = list(map(lambda x: x * 2 , my_list))



'''