>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False

--

>>> line.lower()
'have a nice day'
>>> line.lower().startswith('h')
True

print('Hi There'.lowe())
>>>hi there


---
**************
stuff = "Hello World"
>>> dir(stuff)
['capitalize', 'casefold', 'center', 'count', 'encode',
'endswith', 'expandtabs', 'find', 'format', 'format_map',
'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
'isidentifier', 'islower', 'isnumeric', 'isprintable',
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']
***********

---

>>> data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> atpos = data.find('@')
>>> print(atpos)
21

--

>>>greet = "Hello Bob"
>>>nstr = greet.replace("Bob","Onur")
>>>print(nstr)
Hello Onur
