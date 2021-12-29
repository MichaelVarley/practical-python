import sys
import urllib.request
from xml.etree.ElementTree import parse
import csv


def ex_1_1():
    return (711.25 - 235.14) * 75


def ex_1_4():
    """
    How to download a URL.
    :return:
    """
    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
    doc = parse(u)
    for pt in doc.findall('.//pt'):
        print(pt.text)


"""
EX 1.5
A rubber ball is dropped from a height of 100 meters and each time it hits the ground, 
it bounces back up to 3/5 the height it fell. 
Write a program bounce.py that prints a table showing the height of the first 10 bounces.
"""


class Bounce:
    
    def __init__(self, initial_start_height, bounce_coefficient):
        self.start_height = initial_start_height
        self.bounce_coefficient = bounce_coefficient
        
    def find_height_after_n_bounces(self, n):
        assert n >= 0
        height_after_n = self.start_height * (self.bounce_coefficient ** n)
        return height_after_n
    
    def print_bounce_heights_up_to_n(self, n):
        
        current_height = self.start_height
        
        for i in range(n+1):
            print(round(current_height,4))
            current_height = current_height * self.bounce_coefficient


def ex_1_5():
    start_height = 100
    coeff = 0.6
    
    bouncer = Bounce(start_height, coeff)

    print(bouncer.find_height_after_n_bounces(10))
    bouncer.print_bounce_heights_up_to_n(10)


"""
Numbers

Important things to note. 
x + y      Add
x - y      Subtract
x * y      Multiply
x / y      Divide
x // y     Floor Divide
x % y      Modulo
x ** y     Power
abs(x)     Absolute Value


a = int(x)    # Convert x to integer
b = float(x)  # Convert x to float

a = 3.14159
int(a)
3
b = '3.14159' # It also works with strings containing numbers
float(b)
3.14159

"""

def ex_1_7(initial_amount, rate, standard_monthly_payment, additional_payment_start, additional_payment_end, additional_payment_value):
    """
    Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment,
    and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11.

    Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:
    """

    # Setup Variables
    principal = initial_amount
    interest_rate = rate
    monthly_payment = standard_monthly_payment

    # Tracker Variables
    total_payment = 0
    month_count = 1

    while principal > 0:

        current_payment = monthly_payment + additional_payment_value \
            if (additional_payment_start <= month_count <= additional_payment_end) \
            else monthly_payment

        principal = principal + (1 / 12 * (interest_rate) * principal) - current_payment
        total_payment = total_payment + current_payment
        month_count = month_count+1

    return total_payment


# Section 1.4

"""
s.endswith(suffix)     # Check if string ends with suffix
s.find(t)              # First occurrence of t in s
s.index(t)             # First occurrence of t in s
s.isalpha()            # Check if characters are alphabetic
s.isdigit()            # Check if characters are numeric
s.islower()            # Check if characters are lower-case
s.isupper()            # Check if characters are upper-case
s.join(slist)          # Join a list of strings using s as delimiter
s.lower()              # Convert to lower case
s.replace(old,new)     # Replace text
s.rfind(t)             # Search for t from end of string
s.rindex(t)            # Search for t from end of string
s.split([delim])       # Split string into list of substrings
s.startswith(prefix)   # Check if string starts with prefix
s.strip()              # Strip leading/trailing space
s.upper()              # Convert to upper case
"""

# STRINGS ARE IMMUTABLE IN PYTHON (so s[1]='a' won't work)

"""
A string of 8-bit bytes, commonly encountered with low-level I/O, is written as follows:

data = b'Hello World\r\n'

By putting a little b before the first quotation, you specify that it is a byte string as opposed to a text string.

Byte string. 

text = data.decode('utf-8') # bytes -> text
data = text.encode('utf-8') # text -> bytes

"""


"""
F Strings
A string with formatted expression substitution.

name = 'IBM'
shares = 100
price = 91.1
a = f'{name:>10s} {shares:10d} {price:10.2f}'
a
'       IBM        100      91.10'
b = f'Cost = ${shares*price:0.2f}'
b
'Cost = $9110.00'

Note: This requires Python 3.6 or newer. The meaning of the format codes is covered later.
"""

"""
One limitation of the basic string operations is that they don’t support any kind of advanced pattern matching. 
For that, you need to turn to Python’s re module and regular expressions. 
Regular expression handling is a big topic, but here is a short example:

text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
# Find all occurrences of a date
import re
re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
# Replace all occurrences of a date with replacement text
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'

"""

# File Management System 1.6

# Note:

"""
Files should be properly closed and it’s an easy step to forget. Thus, the preferred approach is to use the with statement like this.

with open(filename, 'rt') as file:
    # Use the file `file`
    ...
    # No need to close explicitly
...statements


Read an entire file all at once as a string.

with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` is a string with all the text in `foo.txt`

Read a file line-by-line by iterating.

with open(filename, 'rt') as file:
    for line in file:
        # Process the line


These exercises depend on a file Data/portfolio.csv. 
The file contains a list of lines with information on a portfolio of stocks. 
It is assumed that you are working in the practical-python/Work/ directory. 
If you’re not sure, you can find out where Python thinks it’s running by doing this:

import os
os.getcwd()
'/Users/beazley/Desktop/practical-python/Work' # Output vary

What if you wanted to read a non-text file such as a gzip-compressed datafile? 
The builtin open() function won’t help you here, 
but Python has a library module gzip that can read gzip compressed files.
>>> import gzip
>>> with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

... look at the output ...
>>>



"""

def ex_1_27():

    total_cost = 0
    counter = 0

    with open('../Data/portfolio.csv', 'rt') as f:
        headers = next(f)
        for line in f:
            line_array = line.split(",")
            shares = float(line_array[1])
            price = float(line_array[2])
            cost = shares * price
            total_cost = total_cost + cost


    return total_cost

"""
Errors:

Exceptions can be caught and handled.

To catch, use the try - except statement.

for line in f:
    fields = line.split()
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldn't parse", line)
    ...

The name ValueError must match the kind of error you are trying to catch.

It is often difficult to know exactly what kinds of errors might occur in advance depending on the operation being performed. For better or for worse, exception handling often gets added after a program has unexpectedly crashed (i.e., “oh, we forgot to catch that error. We should handle that!”).
Raising Exceptions

To raise an exception, use the raise statement.

raise RuntimeError('What a kerfuffle')

This will cause the program to abort with an exception traceback. Unless caught by a try-except block.

% python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <module>
    raise RuntimeError("What a kerfuffle")
RuntimeError: What a kerfuffle



"""

def ex_1_32():
    total_cost = 0
    counter = 0

    with open('../Data/portfolio.csv', 'rt') as f:
        my_csv_reader = csv.reader(f)
        headers = next(my_csv_reader)
        for line in my_csv_reader:
            shares = int(line[1])
            price = float(line[2])
            cost = shares * price
            total_cost = total_cost + cost

    return total_cost


if __name__ == "__main__":

    # print(ex_1_1())

    # ex_1_5()

    # print(ex_1_7(500000, 0.05, 2684.11, 61, 108, 1000))

    print(ex_1_32())