# Estarta Python Training- Day 2
**Sequential Structure:**
**Conditional Structure:
-  if, elif,else
**Repetition Structure:
There are two types of loops in Python:
- `for` loop: The `for` loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
- `while` loop: The `while` loop is used to execute a block of code repeatedly as long as the condition is true.

Functions:
In Python a function is defined using the def keyword:
Calling a Function >>>To call a function, use the function name followed by parenthesis

Arguments Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.

Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments

Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:

Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

Recursion
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
----------------------------------------------------------------------------------------------------------
Python Modules
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
Create a Module >>> To create a module just save the code you want in a file with the file extension .py
Now we can use the module we just created, by using the import statement
Re-naming a Module >>> You can create an alias when you import a module, by using the as keyword


