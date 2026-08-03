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
-----------------------------------------------------------------------------------------------------------------------------------------------
Search and Replace
code:
text = 'The cat sat'
print(text.replace('cat', 'dog'))   # The dog sat
print(text.count('a'))              # 2
print(text.startswith('The'))       # True
print('cat' in text)                # True
-----------------------------------------------------------------------------------------------------------------------------------------------
Split and Join
split() breaks a string into a list; join() glues a list back into a string. This pair is everywhere in real code:
code:
sentence = 'apple,banana,cherry'
fruits = sentence.split(',')
print(fruits)

back = ' - '.join(fruits)
print(back)

o/p:
['apple', 'banana', 'cherry']
apple - banana - cherry
-----------------------------------------------------------------------------------------------------------------------------------------------
Notes on split() and join()
split(sep) breaks a string into a list of substrings using sep as the separator, e.g. 'apple,banana,cherry'.split(',') → ['apple', 'banana', 'cherry'].

If you call split() with no argument, it splits on any whitespace, e.g. 'apple banana cherry'.split() → ['apple', 'banana', 'cherry'].

sep.join(list_of_strings) takes a list of strings and joins them into one string, putting sep between each element, e.g. ' '.join(['apple', 'banana', 'cherry']) → 'apple banana cherry'.

To join with no separator, use an empty string: ''.join(chars) → joins characters directly like 'a' 'p' 'p' 'l' 'e' → 'apple'.

To split into individual characters, use list(text) or [ch for ch in text], then rejoin with ''.join(...) or another separator like '-'.join(...).
-----------------------------------------------------------------------------------------------------------------------------------------------Checchecking Contents
These return True or False, which is handy for validation:
code:
print('12345'.isdigit())   # True
print('abc'.isalpha())     # True
print('Secret1'.isalnum()) # True (letters and digits)
-----------------------------------------------------------------------------------------------------------------------------------------------
Chaining Methods
Because each method returns a new string, you can chain them. This one line cleans and standardizes a name:
code:
raw = '   John SMITH  '
clean = raw.strip().title()
print(f'|{clean}|')  # |John Smith|

o/p:
|John Smith|
-----------------------------------------------------------------------------------------------------------------------------------------------
1. Simple item loop (strings or lists)
Use when you only need each element itself.

python
text = "Karthik"
for ch in text:          # ch is each character
    print(ch)

nums = [10, 20, 30]
for n in nums:           # n is each number
    print(n)
2. Index loop (need positions or neighbors)
Use when you need i, i+1, or to assign back into the list.

python
nums = [3, 1, 3, 3]
for i in range(len(nums) - 1):   # i is 0..len-2
    if nums[i] == 3 and nums[i+1] == 3:
        print("Found 3 next to 3")
For modifying:

python
s = "KaRtHiK"
chars = list(s)
for i in range(len(chars)):
    if chars[i].isupper():
        chars[i] = chars[i].lower()
    else:
        chars[i] = chars[i].upper()
result = ''.join(chars)
3. enumerate (item + index together)
Use when you want both the value and its position, but in a clean way.

python
names = ["ram", "shyam", "karthik"]
for i, name in enumerate(names):   # i=index, name=item
    print(i, name)
Typical use: updating by index but writing clearer code.

python
chars = list("abc")
for i, ch in enumerate(chars):
    if ch == "b":
        chars[i] = "B"
result = ''.join(chars)
4. zip (pairing two iterables)
Use when you want to loop over two lists (or a list and a slice) in parallel.

python
nums = [3, 1, 3, 3]
for a, b in zip(nums, nums[1:]):   # pairs (nums[i], nums[i+1])
    if a == 3 and b == 3:
        print("Found 3 next to 3")
Another example:

python
first = ["ram", "shyam"]
last  = ["kumar", "verma"]
for f, l in zip(first, last):
    print(f, l)   # ram kumar, shyam verma
5. List comprehension (compact item loop)
Use when you’re transforming every element into a new list or string.

python
text = "KaRtHiK"
swapped_chars = [
    ch.lower() if ch.isupper() else ch.upper()
    for ch in text
]
result = ''.join(swapped_chars)
For numbers:

python
nums = [1, 2, 3, 4]
squares = [n*n for n in nums]   # [1, 4, 9, 16]
-----------------------------------------------------------------------------------------------------------------------------------------------
1. in — membership test
Use when you want to know if a value is present in a list, tuple, string, etc.

python
nums = [3, 5, 11]
11 in nums        # True
7 in nums         # False

text = "karthik"
"a" in text       # True
"z" in text       # False
Typical use in your blackjack problem:

python
if 11 in (a, b, c):
    ...
2. any() — “at least one True?”
Use when you have a bunch of boolean conditions and you want to know if any of them is True.

Syntax: any(iterable_of_booleans)

python
nums = [0, 0, 5]
any(nums)              # True (because 5 is truthy)
any([False, False])    # False
any([False, True])     # True
With conditions:

python
nums = [3, 10, 20]
conditions = [n > 10 for n in nums]   # [False, False, True]
any(conditions)                       # True (there is at least one > 10)
Pattern to remember:

python
any(cond(x) for x in items)
Example:

python
nums = [3, 11, 9]
has_eleven = any(n == 11 for n in nums)   # True
3. all() — “are all True?”
Use when you have a bunch of booleans and want to know if every single one is True.

python
nums = [2, 4, 6]
conditions = [n % 2 == 0 for n in nums]   # [True, True, True]
all(conditions)                           # True

nums2 = [2, 3, 4]
all(n % 2 == 0 for n in nums2)            # False (3 is odd)
4. Quick rules to avoid confusion
“Is this value present among these?” → use in
11 in (a, b, c)

“At least one of these conditions is true?” → use any()
any(n == 11 for n in [a, b, c])

“All of these conditions are true?” → use all()
all(n < 21 for n in [a, b, c])

Don’t compare any() or all() to numbers (like any(...) == 11), because they return True/False, not one of your items.
-----------------------------------------------------------------------------------------------------------------------------------------------