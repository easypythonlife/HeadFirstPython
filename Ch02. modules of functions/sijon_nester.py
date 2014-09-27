"""This is the "sijon_nester.py" module and it provides one function called print_lol() 
   which prints lists that may or may not include nested lists."""

import sys      # for sys.stdout

def print_lol(a_list, indent=False, level=0, fh=sys.stdout):
    """Prints each item in a list, recursively descending
       into nested lists (if necessary)."""

    for each_item in a_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for l in range(level):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)
