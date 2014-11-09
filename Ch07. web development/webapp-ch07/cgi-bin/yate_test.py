from yate import *

print("============")
x = start_response()
print(x)
print("============")

x = include_header("Welcome to my home on the web!")
print(x)
print("============")

x = include_footer({'Home':'/index.html', 'Select':'/cgi-bin/select.py'})
print(x)
print("============")

x = start_form('/cgi-bin/process-athlete.py')
print(x)
print("============")

x = end_form()
print(x)
print("============")

x = radio_button('Name', 'Value')
print(x)
print("============")

x = u_list(['item1', 'item2'])
print(x)
print("============")

x = header('This is a header')
print(x)
print("============")

x = para('This is a paragraph')
print(x)
print("============")
