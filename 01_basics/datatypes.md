## Object Types / Data Types

- Number : 1234, 3.14, 3+4j, 0b111, Decimal(). Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2. 'three'], 4.5, kist(range(10))]
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictonary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abd'), {'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True, False
- None : None
- Functions, modules, classes

- Advance : Decorators, Generators, Iterators, Metaprogramming

# Practical

- '*' - Multiplication
- ** - power
- math library
    - math.pi: 3.14...

- random.random - gives random number
- random.choice([1,2,3,4,5]) - gives random values fron the given list

- len(string_name)
- String is immutable, can't be changes
- string_name[1:3] : slice list from 1 to 2 index (it goes to n-1 index)

# Inner Working - Copy, Reference Counts, and Slice

- ref_count: Count all the reference in memory 
           : sys.getrefcount(24601)

- Variables in python does not have datatype
- But the value store in memory has datatype as string, integer, etc. (important)
- Garbage collector in python does not collect unused values immediately***

# copy()
- creates a copy of the same reference to which the variable is pointing in memory rather than pointing to that reference

# List
- List in python are mutable
    >>> a1 = [1,2,3]
    >>> a2 = a1
    >>> a1 = [1,2,3]
    >>> a2 = a1
    >>> a1[1] = 66
    >>> a1
    [1, 66, 3]
    >>> a2
    [1, 66, 3]

- Slicing and replacing elements in list
    >>> colors = ['blue', 'black', 'pink', 'green']
    >>> colors
    ['blue', 'black', 'pink', 'green']
    >>> print(colors)
    ['blue', 'black', 'pink', 'green']
    >>> print(colors[1:2])
    ['black']
    >>> colors[1:2] = "white"
    >>> print(colors)
    ['blue', 'w', 'h', 'i', 't', 'e', 'pink', 'green']  <!-- list treat this as an array -->
    >>> colors = ['blue', 'black', 'pink', 'green']
    >>> colors[1:2] = ["white"]
    >>> print(colors)
    ['blue', 'white', 'pink', 'green']
    >>> colors[1:3]
    ['white', 'pink']
    >>> colors[1:3] = ["red", "yellow"]
    >>> print(colors)
    ['blue', 'red', 'yellow', 'green']

- Example of printing individual items in a list
    >>> colors = ['blue', 'black', 'pink', 'green']
    >>> colors
    ['blue', 'black', 'pink', 'green']
    >>> for color in colors:
    ...     print(color)
    ...     
    blue
    black
    pink
    green

list2 = list1.copy  <!-- creates different reference in memory -->

- methods:
    1. pop() : deleted last element in a list
    2. remove("Black") : remove "Black" from list (if exist)
    3. insert(pos, value) : add value at pos position
    4. append(value) : add value at the end of the list

- Calculations inside list are allowed
    >>> squared_nums = [x**2 for x in range(10)]
    >>> squared_nums
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
- This is known as "List Comprehension"

- range() : gives range of number from 0 to 10

# Dictionary
- Contains pair of key and values
- NOT in an order an of list

# Tuple
- Immutable***
- Assignment operations are not allowed

# Slicing
  l1 = [1,2,3]
  l2 = l1[:]

# is operator
- Gives True when memory reference is same

# Numbers
- math()
    - math.floor() : towards closest lower number
    - math.trunc() : towards 0
    - Complex number
        >>> 2 + 1j
        (2+1j)
        >>> (2 + 1j) * 3
        (6+3j)
        >>> 
    - 0o20 : Octal number
    - oct()
    - 0xff : hexa decimal
    - hex()
    - 0b1000 : binary number
    - bin()
    # Example
        >>> int(64)
        64
        >>> int('64', 8)
        52
        >>> int('64', 16)
        100
        >>> int('10', 2)

- bitwise: 

- random.randint(1, 20)
- random.choice(): used with list
- random.shuffle(): used with list

- decimal library
    # Example
    -- Without decimal: 
        >>> 0.1 + 0.1 + 0.1
        0.30000000000000004
        >>> 0.1 + 0.1 + 0.1 - 0.3
        5.551115123125783e-17
    -- With decimal
    >>> from decimal import Decimal
    >>> Decimal('0.1') +  Decimal('0.1') +  Decimal('0.1')
    Decimal('0.3')
    >>> Decimal('0.1') +  Decimal('0.1') +  Decimal('0.1') - 0.3
    TypeError: unsupported operand type(s) for -: 'decimal.Decimal' and 'float'
    >>> Decimal('0.1') +  Decimal('0.1') +  Decimal('0.1') - Decimal('0.3')
    Decimal('0.0')

- DecimalContextManager

from fractions import Fractions

# Set
- '&' : intersection
- '|' : union
- '-' : difference
....

- x < y < z (is same as) x < y and y < z

# String
- repr, str(), and print() : differernce?

- converting list into list
    >>> animals = "Dog, Cat, Squirrals, Bat"
    >>> animals
    'Dog, Cat, Squirrals, Bat'
    >>> print(animals.split())
    ['Dog,', 'Cat,', 'Squirrals,', 'Bat']
    >>> animals
    'Dog, Cat, Squirrals, Bat'
    >>> print(animals.split(", "))
    ['Dog', 'Cat', 'Squirrals', 'Bat']

- converting list to string
    >>> chai_variety = ['lemon', 'masala', 'ginger']
    >>> chai_variety
    ['lemon', 'masala', 'ginger']
    >>> chai_variety_str = "".join(chai_variety)
    >>> chai_variety_str
    'lemonmasalaginger'
    >>> chai_variety_str = ", ".join(chai_variety)
    >>> chai_variety_str
    'lemon, masala, ginger'
    >>> print(chai_variety_str)
    lemon, masala, ginger

- \" : consider " as a string and print it as it is

- {} : placeholders in string which contain variables

- raw string in python
    >>> print(chai_variety_str)
    lemon, masala, ginger
    >>> path = "c:\local\dir"
    <python-input-128>:1: SyntaxWarning: invalid escape sequence '\l'
    >>> path = "c:\\local\\dir"
    >>> path
    'c:\\local\\dir'    <!-- This is nor the actual path -->
    >>> print(path)
    c:\local\dir
    >>> path = r"c:\local\dir"
    >>> print(path)
    c:\local\dir

# in keyword in python
- Tells wheather the given string or character is present in string or not


