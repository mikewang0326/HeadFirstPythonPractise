import os

print("path " + os.path.abspath('.'))

os.getcwd()

os.chdir('./')

os.getcwd()

class Athlete:
    def __init__(self, a_name, a_dob=None, a_time=[]):
        self.name = a_name
        self.dob = a_dob
        self.time = a_time

sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')

print(type(sarah))
print(type(james))
print(james.name)

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

# sarah_data = get_coach_data('sarah2.txt')

# def printInfo(info):
#     print("info", info['name'], "--", info['dob'], '--', info['time'])
#
# printInfo(sarah_data)

