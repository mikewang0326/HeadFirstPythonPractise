import os
import pickle

os.getcwd()

os.chdir('./')

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

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_time=[]):
        list.__init__([])
        self.name = a_name
        self.dob=a_dob
        self.extend(a_time)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])

def get_coach_data(filename):
    if os.path.exists(filename):
        data = open(filename)
        for line in data:
            line_data = line.strip().split(",")
            print(filename, '  ', line_data)
        temp = []
        for each in line_data:
            temp.append(each)
        data.close()

    else:
        print('no file exist')


    return Athlete(temp.pop(0), temp.pop(0), str(sorted(set([sanitize(t) for t in temp]))[0:3]))

def put_to_store(files_list):
    all_athletes = {}
    for each in files_list:
        ath = get_coach_data(each)
        all_athletes[ath.name] = ath

    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print(ioerr)

    return all_athletes

def get_from_store():
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print(ioerr)

    return all_athletes

the_files = ['james2.txt', 'julie2.txt', 'mikey2.txt', 'sarah2.txt']
put_to_store(the_files)

print('---------------')

data_copy = get_from_store()
for each_copy in data_copy:
    print(data_copy[each_copy].name, ' ', data_copy[each_copy].dob)