#!/usr/local/bin/python3

import yate

print(yate.start_response('text/html'))
print(yate.do_form('add_timing_data_test.py', ['TimeValue'], text='Send'))