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
            james = line.strip().split(",")
            print(filename,'       ', james)
        cleaned_james = []
        for each in james:
            cleaned_james.append(each)
        print('clean',filename, cleaned_james)

        data.close()

    else:
        print('no file exist')

    return cleaned_james

sarah = get_coach_data('sarah2.txt')

sarah_data = {}
sarah_data['name'] = sarah.pop(0)
sarah_data['dob'] = sarah.pop(0)
sarah_data['time'] = sarah


print('sarah2.txt', sarah)
print('sarah_name = ', sarah_data['name'])
print('sarah_dob = ', sarah_data['dob'])
print('fast speed  = ' + str(sorted(set([sanitize(t) for t in sarah_data['time']]))[0:3]))




