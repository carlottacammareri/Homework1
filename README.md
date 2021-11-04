# STRINGS-PYTHON
homework 1 pcs2021

sWAP cASE

      def swap_case(s):
          return s.swapcase()
    
WHAT'S YOUR NAME? 
 
       def print_full_name(first, last):
          # Write your code here
          last= last+"!"
          print ("Hello",first, last,"You just delved into python.")
    
 
 FIND A STRING
 
       def count_substring(string, sub_string):
          count = 0 
          for i in range(len(string)):
              if string[i:].startswith(sub_string):
                  count += 1
          return count

TEXT WRAP

      import textwrap

      def wrap(string, max_width):
          return "\n".join([string[i:i+max_width]for i in range(0, len(string),max_width)])

