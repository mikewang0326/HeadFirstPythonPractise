import os

print("path " + os.path.abspath('.'))

os.getcwd()

os.chdir('../files')

os.getcwd()

provices = []
citys = []

if os.path.exists('city_list_4.txt'):
    try:
        with open('city_list_4.txt')  as data:

            for line in data:
                (provice, city) = line.split(":", 1)
                if provice != '':
                 provices.append(provice)
                 citys.append(city.strip())
    except FileNotFoundError as error:
            print("FileNotFoundError error = " + str(error))
    except ValueError:
        print('ValueError')
        pass
    except:
        print("in except")
        pass
else:
    print('no file exist')


print('provices = ', provices, end="")




