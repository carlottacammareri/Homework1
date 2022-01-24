#HOMEWORK1 CARLOTTA CAMMARERI
#STRINGS

#sWAP cASE

def swap_case(s):
    return s.swapcase()

#WHAT'S YOUR NAME?

def print_full_name(first, last):
    
    last= last+"!"
    print ("Hello",first, last,"You just delved into python.")

#FINDASTRING

def count_substring(string, sub_string):
    count = 0 
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

#TEXTWRAP

import textwrap

def wrap(string, max_width):
    return "\n".join([string[i:i+max_width]for i in range(0, len(string),max_width)])