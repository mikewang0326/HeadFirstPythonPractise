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


def get_coach_data(filename):
    if os.path.exists(filename):
        data = open(filename)
        for line in data:
            line_data = line.strip().split(",")
            print(filename,'  ', line_data)
        temp = []
        for each in line_data:
            temp.append(each)
        data.close()

    else:
        print('no file exist')

    return ({'name': temp.pop(0), 'dob': temp.pop(0), 'time': str(sorted(set([sanitize(t) for t in temp]))[0:3])})

sarah_data = get_coach_data('sarah2.txt')

print('sarah_name = ', sarah_data['name'])
print('sarah_dob = ', sarah_data['dob'])
print('fast time  = ', sarah_data['time'])
