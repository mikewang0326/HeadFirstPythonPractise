import os

provices = []
citys = []

if os.path.exists('city_list_4.txt'):
    data = open('city_list_4.txt')

    for line in data:
        try:
            (provice, city) = line.split(":", 1)
            if provice != '':
               provices.append(provice)
               citys.append(city.strip())
        except ValueError:
            print('ValueError')
            pass
        except:
            print("in except")
        pass
    '''
    connect strings like this
    '''
    print('my', 'provices = ', provices, end="")
    print('\n')
    print('my', 'citys = ', citys, end="")
    data.close()

else:
    print('no file exist')


