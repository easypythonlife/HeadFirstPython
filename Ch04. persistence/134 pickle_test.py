"""
with open('mydata.pickle', 'wb') as mysavedata:
    pickle.dump([1,2,'three'], mysavedata)
with open('mydata.pickle', 'rb') as myrestoredata:
    a_list = pickle.load(myrestoredata) 
"""
import pickle
from nester import print_lol

man = []
other = []

try:
    with open('sketch.txt') as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                if role == 'Man':
                    man.append(line_spoken.strip())
                elif role == 'Other Man':
                    other.append(line_spoken.strip())
            except ValueError:
                pass
except IOError as err:
    print('File error:' + str(err))

try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File error:' + str(err))

try:
    with open('man_data.txt', 'rb') as man_file, open('other_data.txt', 'rb') as other_file:
        man = pickle.load(man_file)
        other = pickle.load(other_file)
except IOError as err:
    print('File error:' + str(err))
