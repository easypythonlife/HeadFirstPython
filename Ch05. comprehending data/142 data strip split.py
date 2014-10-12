with open('james.txt') as jaf:
    james = jaf.readline().strip().split(',')

with open('julie.txt') as juf:
    julie = juf.readline().strip().split(',')

with open('mikey.txt') as mif:
    mikey = mif.readline().strip().split(',')

with open('sarah.txt') as saf:
    sarah = saf.readline().strip().split(',')

print(james)
print(julie)
print(mikey)
print(sarah)
