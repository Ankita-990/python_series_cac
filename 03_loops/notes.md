# Loops in Python

- Iteration tool
    1. for
    2. comprehension

- Iterable Onjects
    - list
    - file

- __next__ or next()
- readline()

- file has its own iterable tool - i.e. open() which list does not have

- iter()
    """ >>> mylist = [1,2,3,4]
    """ >>> listItr = iter(mylist)
    """ >>> listItr
    """ <list_iterator object at 0x00000244FB35EA70> 

    - 0x00000244FB35EA70 is a memory location of the first object in the list
    - iter() gives the location of first element in a list
    - even after using __next__() to point to the next location the iter object (in our case listItr) points to the first reference variable
    - open() function in file operation already has iter() built-in in it

    - File example:
        >>> f = open('chai.py')
        >>> iter(f) is f
        True
        >>> iter(f) is f.__iter__()
        True

    - List example:
        >>> list = [1,2,3,4,5]
        >>> iter(list) is list
        False
    
    - Dictionary is also an iteratable object

    - range() is also iteratable