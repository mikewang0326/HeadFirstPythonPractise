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

    def addTime(self, _time):
        self.time.append(_time)

    def addTimes(self, _time=[]):
        self.time.extend(_time)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self.time]))[0:3])

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

    return Athlete(temp.pop(0), temp.pop(0), str(sorted(set([sanitize(t) for t in temp]))[0:3]))


def printInfo(athlete):
    print("info", athlete.name, "--", athlete.dob, '--', athlete.time)

sarah_data = get_coach_data('sarah2.txt')

test = Athlete('Mike')
test.addTime('6.89')
test.addTime('9.23')
test.addTimes(['1.25', '3.45'])
printInfo(test)

print('top3 = ', test.top3())

# sarah_data.addTime('6.89')

printInfo(sarah_data)

