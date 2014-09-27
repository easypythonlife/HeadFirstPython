from sijon_nester import print_lol

try:
    with open('man_data.txt') as mdf:
        print(mdf.readline())
except IOError as err:
    print('File error:' + str(err))
