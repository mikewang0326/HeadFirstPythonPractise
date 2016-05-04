import os

cleese = {}
palin = dict()
print('cleese type is ', type(cleese))
print('palin type is ', type(palin))

cleese['Name'] = 'John Cleese'
cleese['Ocupations'] = ['actor', 'comedian', 'wirter', 'film producer']

palin = {'Name':'Michael Palin', 'Ocupations':['comedian', 'actor', 'writer', 'tv']}

print('cleese name = ' + cleese['Name'])
print('palin name = ' + palin['Name'])

print('cleese ocupations -1 = ' + cleese['Ocupations'][-1])

palin['Birthplace'] = 'Broomhill, Sheffield, England'

cleese['Birthplace'] = 'Weston-super-Mare, North Somerset, England'


