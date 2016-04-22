import os

print("path " + os.path.abspath('.'))

os.getcwd()

os.chdir('../files')

os.getcwd()

if os.path.exists('city_list.txt'):
    data = open('city_list.txt')

    print(data.readline(), end='')

    data.seek(0)

    for line in data:
        try:
            (provice, city) = line.split(":", 1)
            print(provice, end="")
            print("'s captical is : " + city)
        except ValueError:
            print('ValueError')
            pass
        except:
            print("in except")
        pass
    data.close()

else:
    print('no file exist')


