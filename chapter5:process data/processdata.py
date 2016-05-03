import os

print("path " + os.path.abspath('.'))

os.getcwd()

os.chdir('./')

os.getcwd()

def sanitize(time_string):
    if ("-" in time_string):
        splitter = '-'
        (mins, seconds) = time_string.split(splitter)
        return mins + "." + seconds
    elif (':' in time_string):
        splitter = ":"
        (mins, seconds) = time_string.split(splitter)
        return mins + "." + seconds
    else:
        return time_string

if os.path.exists('james.txt'):
    data = open('james.txt')
    for line in data:
        james = line.strip().split(",")
        print('james       ', james)
    cleaned_james = []
    for each in james:
        cleaned_james.append(sanitize(each))
    print('clean_james ', cleaned_james)

    '''列表推导 list comprehension '''
    quick_clean_james = [sanitize(each_t) for each_t in james]
    print('quick_clean_james', quick_clean_james)

    sorted_james = sorted(cleaned_james)
    print('sorted_james', sorted_james)

    data.close()

else:
    print('no file exist')


if os.path.exists('julie.txt'):
    data = open('julie.txt')
    for line in data:
        julie = line.strip().split(",")
        print('julie       ', julie)
        sorted_julie = sorted(julie)
        print('sorted_julie', sorted_julie)

    data.close()

else:
    print('no file exist')

if os.path.exists('mikey.txt'):
    data = open('mikey.txt')
    for line in data:
        mikey = line.strip().split(",")
        print('mikey       ', mikey)
        sorted_mikey = sorted(mikey)
        print('sorted_mikey', sorted_mikey)
    data.close()

else:
    print('no file exist')




