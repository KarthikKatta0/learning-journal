if we use variables by reassigning etc., and some weird error occurs somewhere, we can restart the kernel in jupiter nb, and it will start fresh and we can start executing the cells from start to avoid errors and have consistent results.

For strings, the first letter index is always 0, if we refer string from reverse, it'll be -1
ex:   h  e  l  l  o
index:0  1  2  3  4
rev i:0 -4 -3 -2 -1

For slicing a string, we're telling Python to grab everything from 0 up to 3. It doesn't include the 3rd index. You'll notice this a lot in Python, where statements and are usually in the context of "up to, but not including". Exclusive
string[start:end(upto):step(jump)]

to reverse a string: string[::-1]

assign a string, let's say s = 'hhjhr', we can see the all the methods available in jupyter by clicking s.tab (string name.tab)

