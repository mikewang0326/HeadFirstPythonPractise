import os

print("path " + os.path.abspath('.'))

os.getcwd()

os.chdir('../files')

os.getcwd()

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

    data.close()

else:
    print('no file exist')


os.chdir('../output')

os.getcwd()

try:

    out_provices = open('provices.data', 'w')
    out_citys = open('citys.data', 'w')

    out_provices.close()

    '''
        connect strings like this
    '''
    print('my', 'provices = ', provices, end="", file=out_provices)
    print('\n')
    print('my', 'citys = ', citys, end="", file=out_citys)

except Exception:
    print('Exception')

finally:
    out_provices.close()
    out_citys.close()

    print('python execute finished')


