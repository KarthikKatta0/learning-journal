if we use variables by reassigning etc., and some weird error occurs somewhere, we can restart the kernel in jupiter nb, and it will start fresh and we can start executing the cells from start to avoid errors and have consistent results.

For strings, the first letter index is always 0, if we refer string from reverse, it'll be -1
ex:   h  e  l  l  o
index:0  1  2  3  4
rev i:0 -4 -3 -2 -1

For slicing a string, we're telling Python to grab everything from 0 up to 3. It doesn't include the 3rd index. You'll notice this a lot in Python, where statements and are usually in the context of "up to, but not including". Exclusive
string[start:end(upto):step(jump)]

to reverse a string: string[::-1]

assign a string, let's say s = 'hhjhr', we can see the all the methods available in jupyter by clicking s.tab (string name.tab)

NOTE: At this time, f-strings won't work! Udemy Coding Exercises use Python 3.5.2, and f-strings require Python 3.6 or higher.
--------------------------------------------------------------------------------------------------------------------------------------------------
In Jupyter notebook, we can create a file in the notebook at the starting itself in the first cell, %%writefile filename.txt
--------------------------------------------------------------------------------------------------------------------------------------------------
We use == for comparision because if we use single equal (=), Python is gonna think that we're assign a new variable there.
When comparing strings, Capitilization counts, which mean it's case-sensitive. For ex: 'Bye' == 'bye' --will return false as they aren't the same.
--------------------------------------------------------------------------------------------------------------------------------------------------
While using for loops, we don't always need to create a temporary placeholder for the loop to iterate items in a list/string. For example:
for jelly in myitems:
    print(jelly)                 --here we used item as placeholder for the loop to refer every item in myitems as jelly and print it.

but we can skip that placeholder and use underscore in the place of placeholder for some loops that just print the same data multiple times according to the condition. for example:
for _ in myitems:
    print('Cool')               --here, we used _ as a placeholder and the loop only prints Cool as the condition specifies. 

--------------------------------------------------------------------------------------------------------------------------------------------------
Tuples have a special quality when it comes to for loops. If you are iterating through a sequence that contains tuples, the item can actually be the tuple itself, this is an example of tuple unpacking. During the for loop we will be unpacking the tuple inside of a sequence and we can access the individual items inside that tuple!

list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)
(2, 4)
(6, 8)
(10, 12)
# Now with unpacking!
for (t1,t2) in list2:               --we can also remove parentheses and use it like this--   for t1,t2 in list2: 
    print(t1)                                                                                           print(t2)
2
6
10
Cool! With tuples in a sequence we can access the items inside of them through unpacking! The reason this is important is because many objects will deliver their iterables through tuples.
--------------------------------------------------------------------------------------------------------------------------------------------------

# Dictionary Unpacking
d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)
k1
k2
k3
Notice how this produces only the keys. So how can we get the values? Or both the keys and the values?

We're going to introduce three new Dictionary methods: .keys(), .values() and .items()

In Python each of these methods return a dictionary view object. It supports operations like membership test and iteration, but its contents are not independent of the original dictionary – it is only a view. Let's see it in action:

# Create a dictionary view object
d.items()
dict_items([('k1', 1), ('k2', 2), ('k3', 3)])
Since the .items() method supports iteration, we can perform dictionary unpacking to separate keys and values just as we did in the previous examples.

# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v) 
k1
1
k2
2
k3
3
If you want to obtain a true list of keys, values, or key/value tuples, you can cast the view as a list:

list(d.keys())
['k1', 'k2', 'k3']

Remember that dictionaries are unordered, and that keys and values come back in arbitrary order. You can obtain a sorted list using sorted():

sorted(d.values())
[1, 2, 3]

--------------------------------------------------------------------------------------------------------------------------------------------------

We can use x+ = 1 for x = x+1

--------------------------------------------------------------------------------------------------------------------------------------------------
for help for any method that we call, we can use builtin function for it.
for ex: help(mylist.insert) --this will return help regarding that method.
--------------------------------------------------------------------------------------------------------------------------------------------------         
there's a secrets module in python for cryptographic functions like random number generation etc
--------------------------------------------------------------------------------------------------------------------------------------------------
To check version of python in code:
from platform import python_version
print(python_version())

--------------------------------------------------------------------------------------------------------------------------------------------------
In python function naming convention, we follow snake-casing, where the name of the function is all small letters and the words of sepearted by _
for ex: def name_of_the_function():

--------------------------------------------------------------------------------------------------------------------------------------------------
docstring (multiple line comment) is  called as ''' nsbcbvhsvhvxdvhusv '''

--------------------------------------------------------------------------------
in print statement, we can use sep and end keywords
sep controls what goes between items. end controls what goes after the line (the default is a new line):
print('a', 'b', 'c')            # Default: space
print('a', 'b', 'c', sep='-')   # a-b-c
print('2025', '01', '15', sep='/')  # a date

print('Hello', end=' ')
print('World')  # stays on the same line

-----------------------------------------------------------------------------------------------------------------------------------------------
Multiple Assignment and Swapping
Python lets you assign several variables in one line, and swap two values without a temporary variable:
a, b, c = 1, 2, 3
print(a, b, c)

# Swap a and b
a, b = b, a
print('After swap:', a, b)
-----------------------------------------------------------------------------------------------------------------------------------------------
Rounding and Formatting
price = 19.876
print(round(price, 2))   # 19.88

# f-strings can format decimals directly
print(f'${price:.2f}')   # $19.88

The :.2f format shows exactly two decimal places, which is exactly what money needs. You will use it in the tip calculator next.
-----------------------------------------------------------------------------------------------------------------------------------------------
Creating Strings
Use single or double quotes. Triple quotes hold multi-line text:
code:
name = 'Alice'
message = "Hello, World!"
poem = '''Roses are red,
Violets are blue'''

print(name)
print(message)
print(poem)

Output: 
Alice
Hello, World!
Roses are red,
Violets are blue
-----------------------------------------------------------------------------------------------------------------------------------------------
f-strings can format numbers too. This is how you show clean decimals, percentages, and thousands separators:
code:
pi = 3.14159
big = 1234567
ratio = 0.856

print(f'{pi:.2f}')    # 3.14  (2 decimals)
print(f'{big:,}')     # 1,234,567  (thousands)
print(f'{ratio:.1%}') # 85.6%  (percentage)

op:
3.14
1,234,567
85.6%
-----------------------------------------------------------------------------------------------------------------------------------------------
# Python f-String Number Formatting Cheat Sheet

Based on examples from FreeAcademy's **Strings and f-Strings** lesson.[1]

## Basic float and precision

```python
pi = 3.14159
```

- `f"{pi}"` -> `3.14159` — default float representation.[1]
- `f"{pi:.2f}"` -> `3.14` — 2 decimal places, fixed-point.[1]
- `f"{pi:.3f}"` -> `3.142` — 3 decimal places, fixed-point.
- `f"{pi:.2e}"` -> `3.14e+00` — scientific notation.
- `f"{pi:.3g}"` -> `3.14` — 3 significant digits; Python chooses fixed-point or scientific notation automatically.

## Thousands separators

```python
big = 1234567
```

- `f"{big:,}"` -> `1,234,567` — comma as thousands separator.[1]
- `f"{big:_.0f}"` -> `1_234_567` — underscore separator, 0 decimal places.

## Percentages

```python
ratio = 0.856
```

- `f"{ratio:.1%}"` -> `85.6%` — 1 decimal place, percentage.[1]
- `f"{ratio:.2%}"` -> `85.60%` — 2 decimal places, percentage.

## Pattern to remember

```python
f"{value:[alignment][width][,][.precision][type]}"
```

The last character is usually the **type**, such as `f`, `e`, `g`, or `%`. For strings, there may be no type at all.[1]
-----------------------------------------------------------------------------------------------------------------------------------------------
Strings Are Immutable
You cannot change a character in place, but you can build a new string:
code:
text = 'Hello'
# text[0] = 'J'  would be an error
text = 'J' + text[1:]
print(text)  # Jello
